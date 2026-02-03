from database.database import Database

def criar_tabela_faltante():
    print("--- Verificando Banco de Dados ---")
    db = Database()
    
    # SQL para criar a tabela Comentario
    sql_create = """
    CREATE TABLE IF NOT EXISTS Comentario (
        id_comentario INTEGER PRIMARY KEY AUTOINCREMENT,
        texto TEXT NOT NULL,
        data_comentario TEXT,
        id_aluno INTEGER,
        id_postagem INTEGER,
        FOREIGN KEY(id_aluno) REFERENCES Aluno(id_aluno),
        FOREIGN KEY(id_postagem) REFERENCES Postagem(id_postagem)
    );
    """
    
    try:
        db.execute(sql_create)
        # Força o commit para garantir que salve no disco
        if hasattr(db, 'conn'):
            db.conn.commit()
        print("✅ Tabela 'Comentario' criada com sucesso!")
    except Exception as e:
        print(f"❌ Erro ao criar tabela: {e}")

if __name__ == "__main__":
    criar_tabela_faltante()