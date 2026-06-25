import psycopg2
from psycopg2 import Error

def conectar():
    conexao = psycopg2.connect(
        "postgresql://neondb_owner:npg_y2vm3kJwoALV@ep-muddy-cell-ac630g3s-pooler.sa-east-1.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
    )
    return conexao

def criar_tabela():
    conexao = conectar()
    cursor = conexao.cursor()
    try:
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS apostas (
                id SERIAL PRIMARY KEY,
                nome VARCHAR(100) NOT NULL,
                selecao VARCHAR(100) NOT NULL,
                valor NUMERIC(10,2) NOT NULL
            )
        """)
        conexao.commit()
    except Error as erro:
        print(f"Erro ao criar tabela: {erro}")
        conexao.rollback()
    finally:
        cursor.close()
        conexao.close()
