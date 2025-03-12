import re

saldo = 0
extrato = []
numero_saque = 0
limites_saque = 3
limite = 500
usuarios = []  # Lista para armazenar os usuários
contas = []  # Lista para armazenar as contas
numero_conta_atual = 1  # Variável para gerar números de conta sequenciais
AGENCIA = "0001"

def validar_cpf(cpf):
  
    cpf = re.sub(r'\D', '', cpf)  # Remove caracteres não numéricos
    if len(cpf) != 11:
        return False
    if cpf == cpf[0] * 11:  # Verifica se todos os dígitos são iguais
        return False
    # Cálculo do primeiro dígito verificador
    soma = 0
    for i in range(9):
        soma += int(cpf[i]) * (10 - i)
    resto = soma % 11
    digito1 = 0 if resto < 2 else 11 - resto
    if int(cpf[9]) != digito1:
        return False
    # Cálculo do segundo dígito verificador
    soma = 0
    for i in range(10):
        soma += int(cpf[i]) * (11 - i)
    resto = soma % 11
    digito2 = 0 if resto < 2 else 11 - resto
    if int(cpf[10]) != digito2:
        return False
    return True

def criar_usuario():
   
    nome = input("Digite o nome do usuário: ")
    cpf = input("Digite o CPF do usuário: ")
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            print("Já existe um usuário cadastrado com este CPF.")
            return
    endereco = input("Digite o endereço do usuário (Logradouro, numero - bairro - cidade/sigla estado): ")
    usuario = {'nome': nome, 'cpf': cpf, 'endereco': endereco}
    usuarios.append(usuario)
    print("Usuário cadastrado com sucesso!")

def criar_conta():
   
    global numero_conta_atual
    cpf = input("Digite o CPF do usuário para vincular a conta: ")
    usuario = None
    for u in usuarios:
        if u['cpf'] == cpf:
            usuario = u
            break
    if usuario is None:
        print("Usuário não encontrado.")
        return

    conta = {
        'agencia': AGENCIA,
        'numero': numero_conta_atual,
        'usuario': cpf,
        'saldo': 0,
        'extrato': []
    }
    contas.append(conta)
    print(f"Conta corrente criada com sucesso! Número da conta: {numero_conta_atual}")
    numero_conta_atual += 1

def Depositar(valor, numero_conta):

    if not validar_cpf:
        return "Erro: CPF inválido!"

    if valor > 0:
        for conta in contas:
            if conta['numero'] == numero_conta:
                conta['saldo'] += valor
                conta['extrato'].append(f"Depósito: R$ {valor:.2f}")
                print("Depósito realizado com sucesso!")

def sacar(valor, numero_conta):
  
    global numero_saque  # Indica que estamos usando a variável global

    if valor > 0:
        for conta in contas:
            if conta['numero'] == numero_conta:
                if valor > conta['saldo']:
                    print("Saldo insuficiente!")
                elif valor > limite:
                    print("Valor do saque excede o limite!")
                elif numero_saque >= limites_saque:
                    print("Número máximo de saques excedidos!")
                else:
                    conta['saldo'] -= valor
                    conta['extrato'].append(f"Saque: R$ {valor:.2f}")
                    print("Saque realizado com sucesso!")
                    numero_saque += 1
                    return
        print("Conta não encontrada para este número de conta.")
    else:
        print("Valor do saque inválido")

def exibir_extrato(numero_conta):
 
    for conta in contas:
        if conta['numero'] == numero_conta:
            print("\nExtrato:")
            if conta['extrato']:
                for transacao in conta['extrato']:
                    print(transacao)
            else:
                print("Não foram realizadas transações.")
            print(f"Saldo atual: R$ {conta['saldo']:.2f}")
            return

def usuario_existe(cpf):
 
    for usuario in usuarios:
        if usuario['cpf'] == cpf:
            return True
    return False

while True:
    print("\nOpções:")
    print("1. Cadastrar Usuário")
    print("2. Criar Conta Corrente")
    print("3. Depositar")
    print("4. Sacar")
    print("5. Extrato")
    print("6. Sair")

    opcao = input("Digite a opção desejada: ")

    if opcao == "1":
        criar_usuario()
    elif opcao == "2":
        criar_conta()
    elif opcao == "3":
        numero_conta = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor do depósito: "))
        Depositar(valor, numero_conta)
    elif opcao == "4":
        numero_conta = int(input("Digite o número da conta: "))
        valor = float(input("Digite o valor do saque: "))
        sacar(valor, numero_conta)
    elif opcao == "5":
        numero_conta = int(input("Digite o número da conta: "))
        print("\n-------------EXTRATO----------------")
        exibir_extrato(numero_conta)
        print("--------------------------------------")
    elif opcao == "6":
        break
    else:
        print("Opção inválida")