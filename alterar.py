from psycopg2 import Error
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from conexao import conectar
from listar import listar

console = Console()

def alterar():
    console.print(Panel("[bold cyan]Alterar Aposta[/]"))
    listar()

    id_aposta = Prompt.ask("Digite o ID da aposta que deseja alterar")

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT id, nome, selecao, valor FROM apostas WHERE id = %s", (id_aposta,))
        aposta = cursor.fetchone()

        if not aposta:
            console.print("[bold red]Aposta não encontrada.[/]")
            return

        console.print(f"[yellow]Aposta atual: {aposta[1]} | {aposta[2]} | R$ {aposta[3]:.2f}[/]")
        console.print("[dim]Deixe em branco para manter o valor atual.[/]")

        nome = Prompt.ask("Novo nome", default=aposta[1])
        selecao = Prompt.ask("Nova seleção", default=aposta[2])

        while True:
            valor_str = Prompt.ask("Novo valor (R$)", default=str(aposta[3]))
            valor = float(str(valor_str).replace(",", "."))
            if valor < 10:
                console.print("[bold red]O valor mínimo é R$ 10,00.[/]")
            else:
                break

        comando = """
            UPDATE apostas
            SET nome = %s, selecao = %s, valor = %s
            WHERE id = %s
        """
        cursor.execute(comando, (nome, selecao, valor, id_aposta))
        conexao.commit()
        console.print("[bold green]Aposta alterada com sucesso! :heavy_check_mark:[/]")
    except Error as erro:
        console.print(f"[bold red]Erro ao alterar: {erro}[/]")
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()
