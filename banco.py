import sqlite3
import time

conexao = sqlite3.connect("jogo.db")   # abre (ou cria) o arquivo
cursor = conexao.cursor()              # o "ponteiro" que executa comandos

cursor.execute("""
    CREATE TABLE IF NOT EXISTS jogador (
        id INTEGER PRIMARY KEY,
        ouro REAL NOT NULL,
        ultima_att REAL NOT NULL
    )
""")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS inventario (
        jogador_id INTEGER NOT NULL,
        item_id TEXT NOT NULL,
        quantidade INTEGER NOT NULL DEFAULT 0,
        PRIMARY KEY (jogador_id, item_id)
    )
""")

cursor.execute(
    "INSERT OR IGNORE INTO jogador (id, ouro, ultima_att) VALUES (1, 10, ?)",
    (time.time(),)
)

for item in ["peixe_palhaco", "anemonas", "corais"]:
    cursor.execute(
        "INSERT OR IGNORE INTO inventario (jogador_id, item_id, quantidade) VALUES (1, ?, 0)",
        (item,)
    )

conexao.commit()   # só aqui as mudanças são gravadas de verdade

cursor.execute("SELECT * FROM jogador")
print(cursor.fetchall())
cursor.execute("SELECT * FROM inventario")
print(cursor.fetchall())

conexao.close()