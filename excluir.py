from psycopg2 import Error
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from conexao import conectar
from listar import listar

console = Console()

def excluir():
    console.print(Panel("[bold cyan]Excluir Aposta[/]"))
    listar()

    id_aposta = Prompt.ask("Digite o ID da aposta que deseja excluir")

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT nome, selecao FROM apostas WHERE id = %s", (id_aposta,))
        aposta = cursor.fetchone()

        if not aposta:
            console.print("[bold red]Aposta não encontrada.[/]")
            return

        confirmar = Prompt.ask(
            f"Confirmar exclusão da aposta de [bold]{aposta[0]}[/] na seleção [bold]{aposta[1]}[/]?",
            choices=["s", "n"]
        )

        if confirmar == "s":
            cursor.execute("DELETE FROM apostas WHERE id = %s", (id_aposta,))
            conexao.commit()
            console.print("[bold green]Aposta excluída com sucesso! :heavy_check_mark:[/]")
        else:
            console.print("[yellow]Exclusão cancelada.[/]")
    except Error as erro:
        console.print(f"[bold red]Erro ao excluir: {erro}[/]")
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()
