CREATE TABLE IF NOT EXISTS Aluno (
    id_aluno INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT UNIQUE NOT NULL,
    senha TEXT NOT NULL,
    data_nascimento TEXT,
    matricula TEXT,
    curso TEXT,
    data_cadastro TEXT
);

-- TABELA SERVIDOR
CREATE TABLE IF NOT EXISTS Servidor (
    id_servidor INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    email TEXT NOT NULL,
    senha TEXT NOT NULL,
    cargo TEXT,
    data_cadastro TEXT
);

-- TABELA MODALIDADE
CREATE TABLE IF NOT EXISTS Modalidade (
    id_modalidade INTEGER PRIMARY KEY AUTOINCREMENT,
    nome TEXT NOT NULL,
    descricao TEXT,
    vagas INTEGER,
    status TEXT
);

-- TABELA INSCRICAO
CREATE TABLE IF NOT EXISTS Inscricao (
    id_inscricao INTEGER PRIMARY KEY AUTOINCREMENT,
    data_inscricao TEXT,
    status TEXT,
    id_aluno INTEGER,
    id_modalidade INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_modalidade) REFERENCES Modalidade(id_modalidade)
);

-- TABELA SELETIVA
CREATE TABLE IF NOT EXISTS Seletiva (
    id_seletiva INTEGER PRIMARY KEY AUTOINCREMENT,
    data TEXT,
    local TEXT,
    criterio TEXT,
    id_modalidade INTEGER,
    FOREIGN KEY (id_modalidade) REFERENCES Modalidade(id_modalidade)
);

-- TABELA RESULTADO_SELETIVA
CREATE TABLE IF NOT EXISTS Resultado_Seletiva (
    id_seletiva INTEGER,
    id_aluno INTEGER,
    resultado TEXT,
    observacao TEXT,
    PRIMARY KEY (id_seletiva, id_aluno),
    FOREIGN KEY (id_seletiva) REFERENCES Seletiva(id_seletiva),
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

-- TABELA POSTAGEM
CREATE TABLE IF NOT EXISTS Postagem (
    id_postagem INTEGER PRIMARY KEY AUTOINCREMENT,
    titulo TEXT NOT NULL,
    conteudo TEXT NOT NULL,
    imagem BLOB,
    data_postagem TEXT,
    id_servidor INTEGER,
    FOREIGN KEY (id_servidor) REFERENCES Servidor(id_servidor)
);

-- TABELA NOTIFICACAO
CREATE TABLE IF NOT EXISTS Notificacao (
    id_notificacao INTEGER PRIMARY KEY AUTOINCREMENT,
    mensagem TEXT,
    data_envio TEXT,
    lida INTEGER,
    id_aluno INTEGER,
    id_servidor INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_servidor) REFERENCES Servidor(id_servidor)
);
CREATE TABLE IF NOT EXISTS Curtida (
    id_curtida INTEGER PRIMARY KEY AUTOINCREMENT,
    id_aluno INTEGER,
    id_postagem INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_postagem) REFERENCES Postagem(id_postagem),
    UNIQUE (id_aluno, id_postagem)
);


CREATE TABLE IF NOT EXISTS Comentario (
    id_comentario INTEGER PRIMARY KEY AUTOINCREMENT,
    texto TEXT NOT NULL,
    data TEXT,
    id_aluno INTEGER,
    id_postagem INTEGER,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_postagem) REFERENCES Postagem(id_postagem)
);
