INSERT INTO Aluno (nome, email, senha, data_nascimento, matricula, curso, data_cadastro) VALUES
('Ana Silva','ana@ifrn.edu','123','2002-05-10','2021001','Informática','2024-01-10'),
('Bruno Lima','bruno@ifrn.edu','123','2001-08-20','2021002','Edificações','2024-01-11'),
('Carlos Souza','carlos@ifrn.edu','123','2000-03-15','2021003','Eletrotécnica','2024-01-12'),
('Daniela Rocha','daniela@ifrn.edu','123','2003-09-01','2021004','Informática','2024-01-13'),
('Eduardo Alves','edu@ifrn.edu','123','2002-12-30','2021005','Mecânica','2024-01-14');

-- Inserindo Servidores/Admins pré-definidos (Sem nome pessoal)
INSERT INTO Servidor (nome, email, senha, cargo, data_cadastro) VALUES
('Coordenação Geral', 'admin@ifsport.edu.br', '123', 'Coordenador', '2024-01-01'),
('Diretoria de Esportes', 'diretoria@ifsport.edu.br', '123', 'Diretoria', '2024-01-01'),
('Secretaria', 'secretaria@ifsport.edu.br', '123', 'Secretaria', '2024-01-01');

INSERT INTO Notificacao (mensagem, data_envio, lida, id_aluno, id_servidor) VALUES
('Inscrição aprovada','2024-02-01',0,1,1),
('Nova modalidade disponível','2024-02-02',0,2,2),
('Documentação pendente','2024-02-03',1,3,3),
('Horário alterado','2024-02-04',0,4,4),
('Evento esportivo amanhã','2024-02-05',1,5,5);