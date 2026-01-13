CREATE TABLE aluno (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    data_nascimento DATE NOT NULL,
    matricula TEXT NOT NULL UNIQUE,
    curso TEXT NOT NULL,
    data_cadastro DATE NOT NULL
);

CREATE TABLE servidor (
    id_servidor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    senha TEXT NOT NULL,
    cargo TEXT NOT NULL,
    data_cadastro DATE NOT NULL
);

CREATE TABLE notificacao (
    id_notificacao INTEGER PRIMARY KEY AUTOINCREMENT,
    mensagem TEXT NOT NULL,
    data_envio DATE NOT NULL,
    lida BOOLEAN NOT NULL,
    id_aluno INTEGER,
    id_servidor INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES aluno(id_aluno),
    FOREIGN KEY (id_servidor) REFERENCES servidor(id_servidor)
);
