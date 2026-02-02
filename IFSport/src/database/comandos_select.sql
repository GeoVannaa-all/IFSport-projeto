SELECT
    a.id_aluno,
    a.nome AS aluno,
    a.curso,
    
    i.id_inscricao,
    i.data_inscricao,
    i.status AS status_inscricao,

    m.nome AS modalidade,
    m.status AS status_modalidade,

    s.id_seletiva,
    s.data AS data_seletiva,
    s.local,
    s.criterio,

    rs.resultado,
    rs.observacao,

    n.mensagem AS notificacao,
    n.data_envio,
    n.lida,

    p.titulo AS postagem,
    p.data_postagem,

    sv.nome AS servidor_autor,

    COUNT(DISTINCT c.id_curtida) AS total_curtidas,
    COUNT(DISTINCT cm.id_comentario) AS total_comentarios

FROM Aluno a

LEFT JOIN Inscricao i
    ON a.id_aluno = i.id_aluno

LEFT JOIN Modalidade m
    ON i.id_modalidade = m.id_modalidade

LEFT JOIN Seletiva s
    ON m.id_modalidade = s.id_modalidade

LEFT JOIN Resultado_Seletiva rs
    ON s.id_seletiva = rs.id_seletiva
   AND a.id_aluno = rs.id_aluno

LEFT JOIN Notificacao n
    ON a.id_aluno = n.id_aluno

LEFT JOIN Curtida c
    ON a.id_aluno = c.id_aluno

LEFT JOIN Postagem p
    ON c.id_postagem = p.id_postagem

LEFT JOIN Comentario cm
    ON p.id_postagem = cm.id_postagem

LEFT JOIN Servidor sv
    ON p.id_servidor = sv.id_servidor

GROUP BY
    a.id_aluno,
    i.id_inscricao,
    m.id_modalidade,
    s.id_seletiva,
    p.id_postagem;

-- Para garantir que o aluno apareça mesmo que ainda não tenha inscrição, resultado, postagem ou curtida.