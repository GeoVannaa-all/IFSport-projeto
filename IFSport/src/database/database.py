import sqlite3
import os
import time

class Database:
    def __init__(self, db_name="sistema_esportivo.db"):
        self.base_dir = os.path.dirname(os.path.abspath(__file__))
        db_path = os.path.join(self.base_dir, db_name)
        sql_file_path = os.path.join(self.base_dir, "create_tables.sql")

        # FIX 1: Adicionamos 'timeout=30'. 
        # Se o banco estiver ocupado, ele espera até 30 segundos antes de dar erro.
        self.connection = sqlite3.connect(db_path, check_same_thread=False, timeout=30)
        
        # FIX 2: Ativar modo WAL (Write-Ahead Logging).
        # Isso permite leitura e escrita simultâneas e reduz drasticamente os travamentos.
        self.connection.execute("PRAGMA journal_mode=WAL")
        self.connection.execute("PRAGMA foreign_keys = ON")
        
        self.init_db(sql_file_path)
        self.criar_admin_padrao()

    def init_db(self, sql_file_path):
        if os.path.exists(sql_file_path):
            try:
                with open(sql_file_path, 'r', encoding='utf-8') as f:
                    sql_script = f.read()
                    cursor = self.connection.cursor()
                    cursor.executescript(sql_script)
                    self.connection.commit()
                    cursor.close() # Boa prática: fechar cursor
            except sqlite3.Error as e:
                print(f"Erro ao criar tabelas: {e}")
        else:
            print(f"ERRO CRÍTICO: Arquivo SQL não encontrado em: {sql_file_path}")

    def criar_admin_padrao(self):
        try:
            sql = """
            INSERT OR IGNORE INTO Servidor (id_servidor, nome, email, senha, cargo) 
            VALUES (1, 'Admin', 'admin@if.edu.br', '123456', 'Coordenador')
            """
            cursor = self.connection.cursor()
            cursor.execute(sql)
            self.connection.commit()
            cursor.close()
        except sqlite3.Error as e:
            print(f"Aviso admin: {e}")

    def execute(self, query, params=()):
        """
        Executa query e retorna o cursor.
        """
        # Cria um cursor novo para esta operação específica
        cursor = self.connection.cursor()
        try:
            cursor.execute(query, params)
            
            # Se for comando de escrita (INSERT, UPDATE, DELETE), faz commit
            if query.strip().upper().startswith(("INSERT", "UPDATE", "DELETE")):
                self.connection.commit()
            
            return cursor
        except sqlite3.Error as e:
            # Em caso de erro, tenta desfazer (rollback) e fecha o cursor
            self.connection.rollback()
            cursor.close()
            print(f"Erro na query: {query}")
            raise e

    def close(self):
        self.connection.close()