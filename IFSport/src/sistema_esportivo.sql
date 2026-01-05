CREATE TABLE IF NOT EXISTS Aluno (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    data_nascimento DATE,
    matricula TEXT,
    curso TEXT,
    data_cadastro DATE
);

CREATE TABLE IF NOT EXISTS Servidor (
    id_servidor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    cargo TEXT,
    data_cadastro DATE
);

CREATE TABLE IF NOT EXISTS Modalidade (
    id_modalidade INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    vagas INTEGER,
    status TEXT
);

CREATE TABLE IF NOT EXISTS Inscricao (
    id_inscricao INTEGER PRIMARY KEY AUTOINCREMENT,
    data_inscricao DATE,
    status TEXT,
    id_aluno INTEGER,
    id_modalidade INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_modalidade) REFERENCES Modalidade(id_modalidade)
);

CREATE TABLE IF NOT EXISTS Postagem (
    id_postagem INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT,
    conteudo TEXT,
    data_postagem DATE,
    id_servidor INTEGER,
    FOREIGN KEY (id_servidor) REFERENCES Servidor(id_servidor)
);

CREATE TABLE IF NOT EXISTS Notificacao (
    id_notificacao INTEGER PRIMARY KEY AUTOINCREMENT,
    mensagem TEXT,
    data_envio DATE,
    lida INTEGER,
    id_aluno INTEGER,
    id_servidor INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_servidor) REFERENCES Servidor(id_servidor)
);
