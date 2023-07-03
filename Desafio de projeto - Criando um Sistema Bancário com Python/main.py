import os

# Código utilizado para limpar o terminal
os.system('cls')

# Variável com as opções   
menu= """
Digite o número referente à opção desejada:

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
        print('Digite o valor do deposito:')
        valor = float(input('> '))
        if valor > 0:
            extrato+= f"Depósito: R$ {valor:.2f}\n"
            saldo+=valor
            os.system('cls')
            print('Operação realizada com sucesso!\n')
        else:
            print('Digite um valor válido\n')


    elif escolha == "2":

        if numero_saques > 3:
            os.system('cls')
            print('Número máximo de saques excedido') 
        elif valor > 0:
            print('Digite o valor do saque:')
            valor = float(input('> '))
            extrato+= f"Saque: R$ {valor:.2f}\n"
            saldo-=valor
            numero_saques+=1
            os.system('cls')
            print('Operação realizada com sucesso!\n')
        else:
            print('Digite um valor válido\n')


    elif escolha == "3":
        if len(extrato) == 0:
            os.system('cls')
            print('Nenhuma operação realizada.\n')
        else:
            os.system('cls')
            print(f"{' - '*4}Extrato{' - '*4}")
            print(extrato)
            print(f"Saldo: R$ {saldo:.2f}")
            print(f"{' - '*10}\n")


    elif escolha == "0":
        os.system('cls')
        print("Agradecemos a preferência! Até mais!")
        break


    else:
        os.system('cls')
        print('Operação invalida, tente novamente.')