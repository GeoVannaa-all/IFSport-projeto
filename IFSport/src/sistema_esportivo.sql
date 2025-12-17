
CREATE DATABASE IF NOT EXISTS sistema_esportivo;
USE sistema_esportivo;


CREATE TABLE Aluno (
    id_aluno INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    data_nascimento DATE,
    matricula VARCHAR(30),
    curso VARCHAR(100),
    data_cadastro DATE
);

CREATE TABLE Servidor (
    id_servidor INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    senha VARCHAR(100) NOT NULL,
    cargo VARCHAR(50),
    data_cadastro DATE
);

CREATE TABLE Modalidade (
    id_modalidade INT AUTO_INCREMENT PRIMARY KEY,
    nome VARCHAR(100) NOT NULL,
    descricao TEXT,
    vagas INT,
    status VARCHAR(30)
);

CREATE TABLE Inscricao (
    id_inscricao INT AUTO_INCREMENT PRIMARY KEY,
    data_inscricao DATE,
    status VARCHAR(30),
    id_aluno INT,
    id_modalidade INT,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_modalidade) REFERENCES Modalidade(id_modalidade)
);

CREATE TABLE Seletiva (
    id_seletiva INT AUTO_INCREMENT PRIMARY KEY,
    data DATE,
    local VARCHAR(100),
    criterio TEXT,
    id_modalidade INT,
    FOREIGN KEY (id_modalidade) REFERENCES Modalidade(id_modalidade)
);

CREATE TABLE Resultado_Seletiva (
    id_seletiva INT,
    id_aluno INT,
    resultado VARCHAR(50),
    observacao TEXT,
    PRIMARY KEY (id_seletiva, id_aluno),
    FOREIGN KEY (id_seletiva) REFERENCES Seletiva(id_seletiva),
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno)
);

CREATE TABLE Postagem (
    id_postagem INT AUTO_INCREMENT PRIMARY KEY,
    titulo VARCHAR(150),
    conteudo TEXT,
    data_postagem DATE,
    id_servidor INT,
    FOREIGN KEY (id_servidor) REFERENCES Servidor(id_servidor)
);

CREATE TABLE Notificacao (
    id_notificacao INT AUTO_INCREMENT PRIMARY KEY,
    mensagem TEXT,
    data_envio DATE,
    lida BOOLEAN,
    id_aluno INT,
    id_servidor INT,
    FOREIGN KEY (id_aluno) REFERENCES Aluno(id_aluno),
    FOREIGN KEY (id_servidor) REFERENCES Servidor(id_servidor)
);
