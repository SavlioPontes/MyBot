import sqlite3
from pathlib import Path

DB_PATH = Path(__file__).resolve().parent / "assistant.db"


def conectar(): 
    return sqlite3.connect(DB_PATH)


def inicializar_banco():
    with conectar() as conexao:
        conexao.execute("""
            CREATE TABLE IF NOT EXISTS links (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL UNIQUE,
                url TEXT NOT NULL
            )
        """)
        conexao.execute(""")
            CREATE TABLE IF NOT EXISTS eventos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                data TEXT NOT NULL,
                hora TEXT NOT NULL
            )
        """)