SELECT a.nome, n.mensagem
FROM aluno a
INNER JOIN notificacao n ON a.id_aluno = n.id_aluno;

SELECT s.nome, n.mensagem
FROM servidor s
INNER JOIN notificacao n ON s.id_servidor = n.id_servidor;

SELECT a.nome, s.nome
FROM aluno a
INNER JOIN notificacao n ON a.id_aluno = n.id_aluno
INNER JOIN servidor s ON s.id_servidor = n.id_servidor;


SELECT a.nome, n.mensagem
FROM aluno a
LEFT JOIN notificacao n ON a.id_aluno = n.id_aluno;

SELECT s.nome, n.mensagem
FROM servidor s
LEFT JOIN notificacao n ON s.id_servidor = n.id_servidor;


SELECT a.nome, n.mensagem
FROM aluno a
LEFT JOIN notificacao n ON a.id_aluno = n.id_aluno

UNION

SELECT a.nome, n.mensagem
FROM notificacao n
LEFT JOIN aluno a ON a.id_aluno = n.id_aluno;
