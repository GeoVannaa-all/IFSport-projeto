# Dicionário de Dados — IFSPORT

Este dicionário descreve todas as tabelas do modelo relacional do sistema IFSPORT, incluindo seus atributos, tipos de dados, chaves primárias (PK) e chaves estrangeiras (FK).

---

## 1. Tabela: USUARIO

Armazena os dados dos usuários do sistema, incluindo alunos e servidores.

| Campo | Tipo | Descrição | Chave |
|------|-----|---------|------|
| id_usuario | INT | Identificador único do usuário | PK |
| nome | VARCHAR | Nome completo do usuário | |
| email | VARCHAR | E-mail do usuário | |
| senha | VARCHAR | Senha criptografada | |
| tipo | VARCHAR | Indica se é aluno ou servidor | |
| telefone | VARCHAR | Telefone para contato | |
| data_cadastro | DATE | Data de criação da conta | |

---

## 2. Tabela: MODALIDADE

Representa as modalidades esportivas disponíveis.

| Campo | Tipo | Descrição | Chave |
|------|-----|---------|------|
| id_modalidade | INT | Identificador da modalidade | PK |
| nome | VARCHAR | Nome do esporte | |
| descricao | VARCHAR | Descrição da modalidade | |

---

## 3. Tabela: SELETIVA

Armazena processos seletivos ligados a uma modalidade.

| Campo | Tipo | Descrição | Chave |
|------|-----|---------|------|
| id_seletiva | INT | Identificador da seletiva | PK |
| nome | VARCHAR | Nome da seletiva | |
| data_seletiva | DATE | Data de realização | |
| id_modalidade | INT | Modalidade associada | FK |

---

## 4. Tabela: INSCRICAO_MODALIDADE

Registra a inscrição de usuários em modalidades esportivas.

| Campo | Tipo | Descrição | Chave |
|------|-----|---------|------|
| id_inscricao | INT | Identificador da inscrição | PK |
| id_usuario | INT | Usuário inscrito | FK |
| id_modalidade | INT | Modalidade escolhida | FK |
| data_inscricao | DATE | Data da inscrição | |
| status | VARCHAR | Situação da inscrição (pendente, aprovada, recusada) | |

---

## 5. Tabela: INSCRICAO_SELETIVA

Registra a participação do usuário em uma seletiva.

| Campo | Tipo | Descrição | Chave |
|------|-----|---------|------|
| id_inscricao | INT | Identificador da inscrição | PK |
| id_usuario | INT | Usuário participante | FK |
| id_seletiva | INT | Seletiva associada | FK |
| status | VARCHAR | Situação da inscrição | |

---

---

## 6. Tabela: POSTAGEM

Armazena notícias e comunicados publicados por servidores.

| Campo | Tipo | Descrição | Chave |
|------|-----|---------|------|
| id_postagem | INT | Identificador da postagem | PK |
| titulo | VARCHAR | Título da postagem | |
| conteudo | TEXT | Conteúdo da postagem | |
| data_publicacao | DATE | Data de publicação | |
| id_servidor | INT | Servidor responsável | FK |

---

## 7. Tabela: NOTIFICACAO

Armazena notificações criadas pelos servidores.

| Campo | Tipo | Descrição | Chave |
|------|-----|---------|------|
| id_notificacao | INT | Identificador da notificação | PK |
| titulo | VARCHAR | Título da notificação | |
| mensagem | TEXT | Conteúdo da notificação | |
| data_envio | DATE | Data de envio | |
| id_servidor | INT | Servidor emissor | FK |

---

## 8. Tabela: USUARIO_NOTIFICACAO

Tabela intermediária que relaciona usuários e notificações recebidas.

| Campo | Tipo | Descrição | Chave |
|------|-----|---------|------|
| id_usuario | INT | Usuário que recebeu a notificação | PK, FK |
| id_notificacao | INT | Notificação recebida | PK, FK |
| lida | BOOLEAN | Indica se a notificação foi visualizada | |

---
