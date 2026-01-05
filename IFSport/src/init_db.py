import sqlite3

with open("sistema_esportivo.sql", "r") as f:
    sql = f.read()

conn = sqlite3.connect("sistema_esportivo.db")
cursor = conn.cursor()
cursor.executescript(sql)
conn.commit()
conn.close()

print("Banco criado com sucesso!")
