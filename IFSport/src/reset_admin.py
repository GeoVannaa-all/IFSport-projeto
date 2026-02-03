from database.database import Database

def consertar_admin():
    db = Database()
    
    print("--- INICIANDO DIAGNÓSTICO DO ADMIN ---")
    
    # 1. Limpa a tabela Servidor para evitar duplicatas ou lixo
    db.execute("DELETE FROM Servidor")
    print("1. Tabela Servidor limpa.")

    # 2. Insere o Admin com certeza absoluta dos dados
    # Email: admin@ifsport.edu.br
    # Senha: 123
    sql_insert = """
    INSERT INTO Servidor (nome, email, senha, cargo, data_cadastro) 
    VALUES ('Coordenação Geral', 'admin@ifsport.edu.br', '123', 'Coordenador', '2024-02-01')
    """
    db.execute(sql_insert)
    # Importante: Commit para salvar no arquivo .db
    if hasattr(db, 'conn'):
        db.conn.commit()
    
    print("2. Admin reinserido com sucesso.")
    print("--------------------------------------")
    print("RESUMO PARA LOGIN:")
    print("📧 Email: admin@ifsport.edu.br")
    print("🔑 Senha: 123")
    print("--------------------------------------")

    # 3. Verifica se gravou mesmo
    cursor = db.execute("SELECT email, senha FROM Servidor")
    admins = cursor.fetchall()
    print(f"3. Verificação no banco: Encontrados {len(admins)} admins.")
    for a in admins:
        print(f"   -> Banco diz: {a}")

if __name__ == "__main__":
    consertar_admin()