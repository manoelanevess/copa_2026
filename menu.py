from rich.console import Console
from rich.panel import Panel
from rich.prompt import Prompt
from conexao import criar_tabela
from incluir import incluir
from listar import listar
from alterar import alterar
from excluir import excluir
from simular import simular

console = Console()

criar_tabela()

while True:
    console.print(Panel("[bold blue]Apostas da Copa do Mundo 2026 :trophy:[/]"))
    console.print("[1] Incluir aposta")
    console.print("[2] Listar apostas")
    console.print("[3] Alterar aposta")
    console.print("[4] Excluir aposta")
    console.print("[5] Simular resultado")
    console.print("[0] Sair")

    opcao = Prompt.ask("\nEscolha uma opção", choices=["0", "1", "2", "3", "4", "5"])

    if opcao == "1":
        incluir()
    elif opcao == "2":
        listar()
    elif opcao == "3":
        alterar()
    elif opcao == "4":
        excluir()
    elif opcao == "5":
        simular()
    elif opcao == "0":
        console.print("[bold magenta]Saindo... até mais! :wave:[/]")
        break
