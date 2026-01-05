# Caso de Uso: Realizar Cadastro (CDU01)

## Atores Envolvidos

* Usuário (Estudante / Servidor)

## Pré-condições

* O usuário não possui cadastro no sistema.
* O sistema está disponível.

## Pós-condições

* Uma nova conta é criada e armazenada no banco de dados.
* O usuário passa a estar apto a realizar login no sistema.

## Fluxo Principal

1. O usuário acessa a opção de cadastro.
2. O usuário informa seus dados pessoais (nome, e-mail, senha e demais dados solicitados).
3. O sistema valida os dados informados.
4. O sistema registra o usuário no banco de dados.

## Fluxo de Exceção

* **2a.** Caso algum dado esteja incorreto ou incompleto, ou se o e-mail informado já estiver cadastrado, o sistema solicita a correção das informações antes de prosseguir com o cadastro.
