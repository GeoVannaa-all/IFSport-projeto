# 📚 Dicionário de Dados — IFSPORT

Este documento descreve detalhadamente a estrutura do banco de dados do sistema **IFSPORT**. Abaixo estão listadas todas as tabelas, seus atributos, tipos de dados e chaves (Primárias e Estrangeiras).

---

## 1. Tabela: ALUNO
Armazena as informações dos estudantes cadastrados no sistema.

| Campo | Tipo | Descrição | Chave |
| :--- | :--- | :--- | :--- |
| **id_aluno** | `INTEGER` | Identificador único do aluno (Auto-incremento) | **PK** |
| nome | `TEXT` | Nome completo do aluno | |
| email | `TEXT` | E-mail institucional do aluno | **UK** |
| senha | `TEXT` | Hash da senha de acesso | |
| matricula | `TEXT` | Número da matrícula acadêmica | **UK** |
| curso | `TEXT` | Curso em que o aluno está matriculado | |
| data_nascimento | `TEXT` | Data de nascimento do aluno | |
| data_cadastro | `TEXT` | Data de registro no sistema | |

---

## 2. Tabela: SERVIDOR
Armazena os dados dos funcionários e professores com acesso administrativo.

| Campo | Tipo | Descrição | Chave |
| :--- | :--- | :--- | :--- |
| **id_servidor** | `INTEGER` | Identificador único do servidor (Auto-incremento) | **PK** |
| nome | `TEXT` | Nome completo do servidor | |
| email | `TEXT` | E-mail institucional do servidor | **UK** |
| senha | `TEXT` | Hash da senha de acesso | |
| cargo | `TEXT` | Função exercida (ex: Coordenador, Treinador) | |
| data_cadastro | `TEXT` | Data de registro no sistema | |

---

## 3. Tabela: MODALIDADE
Representa os esportes e atividades disponíveis no campus.

| Campo | Tipo | Descrição | Chave |
| :--- | :--- | :--- | :--- |
| **id_modalidade** | `INTEGER` | Identificador único da modalidade | **PK** |
| nome | `TEXT` | Nome do esporte (ex: Futsal, Vôlei) | |
| descricao | `TEXT` | Detalhes sobre treinos e regras | |
| vagas | `INTEGER` | Quantidade total de vagas ofertadas | |
| status | `TEXT` | Situação atual (ex: Aberta, Fechada, Em Análise) | |

---

## 4. Tabela: INSCRICAO
Registra o vínculo de interesse de um aluno em uma modalidade.

| Campo | Tipo | Descrição | Chave |
| :--- | :--- | :--- | :--- |
| **id_inscricao** | `INTEGER` | Identificador único da inscrição | **PK** |
| data_inscricao | `TEXT` | Data em que o aluno solicitou a vaga | |
| status | `TEXT` | Estado da inscrição (Pendente, Aprovado, Recusado) | |
| id_aluno | `INTEGER` | Aluno que realizou a inscrição | **FK** |
| id_modalidade | `INTEGER` | Modalidade desejada | **FK** |

---

## 5. Tabela: SELETIVA
Armazena os eventos de seleção para times ou competições específicas.

| Campo | Tipo | Descrição | Chave |
| :--- | :--- | :--- | :--- |
| **id_seletiva** | `INTEGER` | Identificador único da seletiva | **PK** |
| data | `TEXT` | Data e hora da realização do evento | |
| local | `TEXT` | Local da seletiva (ex: Ginásio, Campo) | |
| criterio | `TEXT` | Critérios técnicos que serão avaliados | |
| id_modalidade | `INTEGER` | Modalidade à qual a seletiva pertence | **FK** |

---

## 6. Tabela: RESULTADO_SELETIVA
Registra o desempenho e a aprovação dos alunos que participaram de seletivas.

| Campo | Tipo | Descrição | Chave |
| :--- | :--- | :--- | :--- |
| **id_seletiva** | `INTEGER` | Identificador da seletiva realizada | **PK, FK** |
| **id_aluno** | `INTEGER` | Identificador do aluno avaliado | **PK, FK** |
| resultado | `TEXT` | Parecer final (ex: Aprovado, Lista de Espera) | |
| observacao | `TEXT` | Notas ou comentários técnicos do treinador | |

---

## 7. Tabela: POSTAGEM
Armazena as notícias, avisos e comunicados do feed.

| Campo | Tipo | Descrição | Chave |
| :--- | :--- | :--- | :--- |
| **id_postagem** | `INTEGER` | Identificador único da postagem | **PK** |
| titulo | `TEXT` | Manchete da notícia | |
| conteudo | `TEXT` | Corpo do texto da postagem | |
| imagem | `TEXT` | Caminho ou string Base64 da imagem ilustrativa | |
| data_postagem | `TEXT` | Data de publicação | |
| id_servidor | `INTEGER` | Servidor autor da postagem | **FK** |

---

## 8. Tabela: CURTIDA
Registra as interações (likes) dos alunos nas postagens.

| Campo | Tipo | Descrição | Chave |
| :--- | :--- | :--- | :--- |
| **id_curtida** | `INTEGER` | Identificador único da curtida | **PK** |
| id_aluno | `INTEGER` | Aluno que curtiu | **FK** |
| id_postagem | `INTEGER` | Postagem que recebeu a curtida | **FK** |

---

## 9. Tabela: NOTIFICACAO
Armazena mensagens enviadas diretamente aos alunos.

| Campo | Tipo | Descrição | Chave |
| :--- | :--- | :--- | :--- |
| **id_notificacao** | `INTEGER` | Identificador único da notificação | **PK** |
| mensagem | `TEXT` | Conteúdo do aviso | |
| data_envio | `TEXT` | Data de envio da notificação | |
| lida | `INTEGER` | Status de leitura (0 = Não lida, 1 = Lida) | |
| id_aluno | `INTEGER` | Aluno destinatário | **FK** |
| id_servidor | `INTEGER` | Servidor remetente (opcional) | **FK** |

---

### Legenda:
* **PK:** Primary Key (Chave Primária)
* **FK:** Foreign Key (Chave Estrangeira)
* **UK:** Unique Key (Chave Única - não permite valores repetidos)
* **Tipos:** Os tipos (`TEXT`, `INTEGER`) refletem a implementação em SQLite, onde datas são armazenadas como texto.