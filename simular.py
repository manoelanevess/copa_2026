from psycopg2 import Error
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.prompt import Prompt
from conexao import conectar

console = Console()

def simular():
    console.print(Panel("[bold cyan]Simular Resultado da Copa 2026[/]"))
    selecao_campeã = Prompt.ask("Qual seleção foi campeã?")

    conexao = conectar()
    cursor = conexao.cursor()
    try:
        # busca todos que apostaram na seleção campeã
        cursor.execute(
            "SELECT nome, valor FROM apostas WHERE LOWER(selecao) = LOWER(%s)",
            (selecao_campeã,)
        )
        vencedores = cursor.fetchall()

        # total apostado por todos
        cursor.execute("SELECT SUM(valor) FROM apostas")
        total_geral = cursor.fetchone()[0] or 0

        if not vencedores:
            console.print(f"[yellow]Nenhuma aposta foi feita na seleção [bold]{selecao_campeã}[/]. Ninguém ganhou![/]")
            console.print(f"[dim]Total em jogo: R$ {total_geral:.2f}[/]")
            return

        total_vencedores = sum(v[1] for v in vencedores)

        tabela = Table(title=f"Vencedores - Campeã: {selecao_campeã.upper()}")
        tabela.add_column("Nome", style="magenta")
        tabela.add_column("Apostado (R$)", style="yellow")
        tabela.add_column("% do total", style="cyan")
        tabela.add_column("Recebe (R$)", style="bold green")

        for vencedor in vencedores:
            nome = vencedor[0]
            valor_apostado = float(vencedor[1])
            proporcao = valor_apostado / float(total_vencedores)
            valor_recebe = proporcao * float(total_geral)
            percentual = proporcao * 100
            tabela.add_row(
                nome,
                f"{valor_apostado:.2f}",
                f"{percentual:.1f}%",
                f"{valor_recebe:.2f}"
            )

        console.print(tabela)
        console.print(f"[bold]Total em jogo: R$ {total_geral:.2f}[/]")
    except Error as erro:
        console.print(f"[bold red]Erro ao simular: {erro}[/]")
    finally:
        cursor.close()
        conexao.close()
