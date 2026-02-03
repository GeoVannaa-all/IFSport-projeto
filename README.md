# 🏅 IFSPORT

**IFSPORT – Sistema de Inscrições e Informações Esportivas do IFRN**

---

## 👥 Integrantes do Grupo

* **Deyvid Jhonatan**
* **Francisco Davi**
* **Geovanna Ludmila**
* **Jaziel Marcelo**

---

## 🎯 Objetivo do Sistema

O **IFSPORT** tem como objetivo oferecer à comunidade do **IFRN – Campus Natal Central (CNAT)** um sistema digital que facilite o acesso às atividades esportivas da instituição.

A aplicação permite que alunos acompanhem notícias, eventos esportivos, realizem inscrições em modalidades e participem de seletivas, enquanto servidores podem gerenciar postagens, notificações e validar inscrições.

---

## 🧭 Instruções Básicas de Navegação do Repositório

A estrutura do repositório está organizada da seguinte forma:

```
IFSport/
│   
|      
├── docs/          
 (documentos do sistema)
|      └── casos-de-uso/
|      └── diagrama_relacional/
|      └── diagrama-de-classes/
|      └── requisitos/
|      └── visao-do-produto/
|
├── scr/               
 (codigo do sistema)
│   └── dao/
│   └── database/
│   └── models/
|   └── templates/
|   └── venv/
|   └── views/
|   └── main.py
|   └── fix_db.py
|   └── reset_admin.py
|    
└── README.md              
```
### ▶️ Como executar o projeto

1. Acesse a pasta do projeto:

   ```bash
   cd IFSport/src
   ```
2. ative o venv:

   ```bash
   source venv/bin/activate
   ```
3. Execute o arquivo principal:

   ```bash
   streamlit run main.py
   ```

---

## 🛠 Tecnologias Utilizadas

* **Python 3** – Linguagem principal do projeto
* **SQLite** – Banco de dados 
* **Draw.io**
* **ERDplus**

---

## 🎨 Estilização da Página

A proposta visual do sistema segue uma identidade simples e objetiva, voltada ao contexto educacional e esportivo:

* Cores institucionais e esportivas
* Layout limpo e organizado
* Ênfase na usabilidade e clareza das informações
* Interface pensada para fácil acesso às inscrições, notificações e notícias

A estilização foi planejada para garantir uma boa experiência ao usuário, priorizando acessibilidade e organização visual.

---

## 📄 Observações Finais

Este projeto foi desenvolvido com fins **acadêmicos**, como parte das atividades da disciplinas de POO, Banco de Dados e APOO.

---

✨ *Projeto desenvolvido pela equipe*
