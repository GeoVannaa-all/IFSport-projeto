SELECT
    a.id_aluno,
    a.nome AS aluno,
    a.curso,
    -- Dados de Inscrição
    i.id_inscricao,
    i.status AS status_inscricao,
    m.nome AS modalidade,
    -- Dados de Notificação
    n.mensagem AS notificacao,
    -- Contagens
    COUNT(DISTINCT c.id_curtida) AS total_curtidas_dadas,
    COUNT(DISTINCT cm.id_comentario) AS total_comentarios_feitos
FROM Aluno a
LEFT JOIN Inscricao i ON a.id_aluno = i.id_aluno
LEFT JOIN Modalidade m ON i.id_modalidade = m.id_modalidade
LEFT JOIN Notificacao n ON a.id_aluno = n.id_aluno
LEFT JOIN Curtida c ON a.id_aluno = c.id_aluno
LEFT JOIN Comentario cm ON a.id_aluno = cm.id_aluno -- Note que corrigi o JOIN para ligar ao aluno
GROUP BY a.id_aluno, i.id_inscricao, n.id_notificacao;