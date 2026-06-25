from psycopg2 import Error
from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from conexao import conectar

console = Console()

def incluir():
    console.print(Panel("[bold cyan]Nova Aposta[/]"))
    nome = Prompt.ask("Seu nome")
    selecao = Prompt.ask("Seleção que vai ser campeã")
    
    while True:
        valor_str = Prompt.ask("Valor da aposta (mínimo R$ 10,00)")
        valor = float(valor_str.replace(",", "."))
        if valor < 10:
            console.print("[bold red]O valor mínimo é R$ 10,00. Tente novamente.[/]")
        else:
            break

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        comando = """
            INSERT INTO apostas (nome, selecao, valor)
            VALUES (%s, %s, %s)
            RETURNING id
        """
        cursor.execute(comando, (nome, selecao, valor))
        id_aposta = cursor.fetchone()[0]
        conexao.commit()
        console.print(f"[bold green]Aposta cadastrada com sucesso! ID: {id_aposta} :heavy_check_mark:[/]")
    except Error as erro:
        console.print(f"[bold red]Erro ao incluir: {erro}[/]")
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()
