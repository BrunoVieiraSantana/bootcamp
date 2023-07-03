import os

# Código utilizado para limpar o terminal
os.system('cls')

# Variável com as opções   
menu= """
Digite o número referente a opção desejada:

    [1] Depositar
    [2] Sacar
    [3] Extrato
    [0] Sair
"""
# Variáveis utilizadas para armazenar e definir limites 
saldo = 0
limite = 500
extrato = ""
numero_saques = 0
limite_saque = 3

# Loop de repetição, que exibe menu e opções que serão apresentadas ao usuário
while True:
    print('Sistema Bancário')
    print (menu)
    escolha = input('> ')

    if escolha == "1":
        valor = float(input("Informe o valor do depósito: "))

        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            os.system('cls')
            print("Operação realizada com sucesso!\n")


        else:
            os.system('cls')
            print("Operação falhou! O valor informado é inválido.\n")

    elif escolha == "2":
        valor = float(input("Informe o valor do saque: "))

        excedeu_saldo = valor > saldo

        excedeu_limite = valor > limite

        excedeu_saques = numero_saques >= limite_saque

        if excedeu_saldo:
            os.system('cls')
            print("Operação falhou! Você não tem saldo suficiente.\n")

        elif excedeu_limite:
            os.system('cls')
            print("Operação falhou! O valor do saque excede o limite.\n")

        elif excedeu_saques:
            os.system('cls')
            print("Operação falhou! Número máximo de saques excedido.\n")

        elif valor > 0:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            os.system('cls')
            print("Operação realizada com sucesso!\n")

        else:
            os.system('cls')
            print("Operação falhou! O valor informado é inválido.\n")

    elif escolha == "3":
        os.system('cls')
        print("\n================ EXTRATO ================")
        print("Não foram realizadas movimentações." if not extrato else extrato)
        print(f"\nSaldo: R$ {saldo:.2f}")
        print("==========================================\n")

    elif escolha == "0":
        print("Agradecemos a preferência! Até mais!!!")
        break

    else:
        os.system('cls')
        print("Operação inválida, por favor selecione novamente a operação desejada.\n")