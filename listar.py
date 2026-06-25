from psycopg2 import Error
from rich.console import Console
from rich.table import Table
from conexao import conectar

console = Console()

def listar():
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("SELECT id, nome, selecao, valor FROM apostas ORDER BY nome")
        apostas = cursor.fetchall()

        if not apostas:
            console.print("[yellow]Nenhuma aposta cadastrada ainda.[/]")
            return

        tabela = Table(title="Apostas da Copa do Mundo 2026")
        tabela.add_column("ID", style="cyan")
        tabela.add_column("Nome", style="magenta")
        tabela.add_column("Seleção", style="yellow")
        tabela.add_column("Valor (R$)", style="green")

        for aposta in apostas:
            tabela.add_row(str(aposta[0]), aposta[1], aposta[2], f"{aposta[3]:.2f}")

        console.print(tabela)
    except Error as erro:
        console.print(f"[bold red]Erro ao listar: {erro}[/]")
    finally:
        cursor.close()
        conexao.close()
