# Sistema Bancário Simples em Python

Este projeto implementa um sistema bancário simples em Python, permitindo a criação de usuários, contas correntes, depósitos, saques e visualização de extratos.

## Funcionalidades

-   **Cadastro de Usuários**: Permite cadastrar novos usuários com nome, CPF e endereço.
-   **Criação de Contas Correntes**: Permite criar contas correntes vinculadas a usuários existentes.
-   **Depósitos**: Permite realizar depósitos em contas correntes.
-   **Saques**: Permite realizar saques de contas correntes, com limites de valor e número de saques diários.
-   **Extrato**: Permite visualizar o extrato de uma conta corrente, mostrando todas as transações e o saldo atual.
-   **Validação de CPF**: Valida o CPF dos usuários para garantir a integridade dos dados.

## Como Usar

1.  **Clone o repositório**:

    ```bash
    git clone [https://github.com/techjoaopedro/Projeto_Banc-rio_Python_Completo.git](https://github.com/techjoaopedro/Projeto_Banc-rio_Python_Completo.git)
    ```

2.  **Execute o script**:

    ```bash
    python projetocompleto.py
    ```

3.  **Siga as instruções do menu**:

    -      Digite o número da opção desejada e pressione Enter.
    -      Siga as instruções para cada opção, fornecendo os dados necessários.

## Requisitos

-      Python 3.x

## Estrutura do Código

-   **`validar_cpf(cpf)`**: Função para validar o CPF.
-   **`criar_usuario()`**: Função para cadastrar um novo usuário.
-   **`criar_conta()`**: Função para criar uma nova conta corrente.
-   **`Depositar(valor, numero_conta)`**: Função para realizar um depósito.
-   **`sacar(valor, numero_conta)`**: Função para realizar um saque.
-   **`exibir_extrato(numero_conta)`**: Função para exibir o extrato de uma conta.
-   **`usuario_existe(cpf)`**: Função para verificar se um usuário já existe.
-   **Loop principal**: Exibe o menu de opções e executa as funções correspondentes.

## Melhorias Futuras

-   Implementar persistência de dados (arquivos ou banco de dados).
-   Adicionar mais validações de entrada.
-   Melhorar a interface do usuário.
-   Implementar transferências entre contas.
-   Implementar uma função para o usuário poder alterar seu endereço e nome.
-   Implementar uma função para o usuário poder excluir sua conta.
-   Modularizar o código em funções menores.

## Contribuição

Contribuições são bem-vindas! Sinta-se à vontade para abrir issues e pull requests para melhorar este projeto.