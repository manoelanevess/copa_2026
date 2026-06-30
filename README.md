# Apostas da Copa do Mundo 2026

Sistema feito em Python para gerenciar apostas entre amigos sobre quem vai ser campeão da Copa do Mundo de 2026. O projeto usa PostgreSQL (banco hospedado no Neon) e a biblioteca Rich pra deixar o terminal mais organizado.

Trabalho feito pra faculdade (ADS - UniSenac Pelotas).

## O que dá pra fazer

- Cadastrar aposta (nome da pessoa, seleção escolhida e valor apostado)
- Listar todas as apostas cadastradas
- Alterar uma aposta existente
- Excluir uma aposta
- Simular o resultado da Copa: você informa qual seleção foi campeã e o sistema calcula quanto cada pessoa que apostou nela vai receber, dividindo o total arrecadado proporcionalmente entre os vencedores

## Tecnologias usadas

- Python
- PostgreSQL (Neon)
- psycopg2
- Rich (interface no terminal)

## Estrutura do projeto

```
menu.py      -> menu principal, chama as outras funções
conexao.py   -> conexão com o banco e criação da tabela
incluir.py   -> cadastra uma nova aposta
listar.py    -> lista as apostas em tabela
alterar.py   -> edita uma aposta existente
excluir.py   -> remove uma aposta (com confirmação)
simular.py   -> simula o resultado e calcula o quanto cada um recebe
```

## Como rodar

1. Clone o repositório
2. Instale as dependências:
```
pip install rich psycopg2-binary
```
3. Configure a string de conexão do banco no `conexao.py` (a sua, não a que tá no repositório)
4. Rode o sistema:
```
python menu.py
```

Na primeira execução a tabela `apostas` é criada automaticamente no banco.

## Como funciona a simulação

A regra é simples: todo o dinheiro apostado (de todo mundo, em todas as seleções) forma um "pote". Quando a seleção campeã é informada, esse pote inteiro é dividido entre quem apostou nela, proporcional ao valor que cada um apostou. Quem apostou mais, recebe mais. Se ninguém apostou na campeã, ninguém recebe nada.

## Observação

A aposta mínima é R$ 10,00 — o sistema não deixa cadastrar ou alterar pra um valor menor que isso.
