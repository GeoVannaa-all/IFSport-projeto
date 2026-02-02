-- telefone = '9' || telefone
-- (a) UPDATE todos os registros
UPDATE aluno SET curso = 'Curso Atualizado';

-- (b) UPDATE condição simples
UPDATE aluno SET curso = 'Informática' WHERE id_aluno = 1;

-- (c) UPDATE condição composta
UPDATE aluno SET curso = 'Edificações'
WHERE curso = 'Informática' AND id_aluno > 2;

-- (d) UPDATE dois campos
UPDATE servidor
SET cargo = 'Supervisor', senha = 'nova123'
WHERE id_servidor = 1;

-- (e) UPDATE usando valor antigo
UPDATE aluno SET matricula = '9' || matricula;

-- (f) UPDATE usando função
UPDATE servidor SET nome = UPPER(nome);

-- (g) DELETE todos os registros
DELETE FROM notificacao;

-- (h) DELETE condição simples
DELETE FROM aluno WHERE id_aluno = 5;

-- (i) DELETE condição composta
DELETE FROM aluno WHERE curso = 'Mecânica' AND id_aluno < 4;

-- (j) DELETE com função agregada
DELETE FROM aluno
WHERE id_aluno = (SELECT MAX(id_aluno) FROM aluno);
