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
        pass

    elif escolha == "2":
        pass
    elif escolha == "3":
        pass

    elif escolha == "0":
        print("Agradecemos a preferência! Até mais!!!")
        break

    else:
        os.system('cls')
        print('Operação invalida, tente novamente.')