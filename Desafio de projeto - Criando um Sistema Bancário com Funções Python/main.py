import os

def criar_usuario(usuarios):
    print('Digite os dados necessarios')
    nome = input('Nome: ')

    # Verificação de CPF formado apenas por números, contendo 11 dígitos e que não possam existir duplicatas
    while True:
        cpf = (input('CPF (somente números): '))
        try:
            cpf_teste = int(cpf)
            teste = 0
            if len(cpf) == 11:
                for i in usuarios:
                    if cpf == (i['cpf']):
                        teste+= 1
                if teste > 0:
                    print('CPF já cadastrado')
                elif teste == 0:
                    break
            else:
                print('O CPF deve conter 11 números.')
        except:
            limpar_tela()
            print('Digite apenas números')


    data_nascimento = input('Data de Nascimento: (formato dd/mm/aaa): ')
    print('Endereço')
    rua = input('Rua: ')
    numero = input('Número: ')
    bairro = input('Bairro: ')
    cidade = input('Cidade: ')
    estado = input('Estado (ex: CE): ')
    endereco = f"{rua}, {numero}, {bairro}, {cidade} - {estado}"
    usuarios.append({"nome": nome, "data_nascimento": data_nascimento, "cpf": cpf, "endereco": endereco})
    limpar_tela()
    print('Usúario criado com sucesso!\n' )
    print(usuarios)


def criar_conta(contas, agencia, numero_conta, usuarios):
    print('Digite o CPF do Titular da Nova Conta')
    cpf = input('CPF: ')
    while True:
        cpf = (input('CPF (somente números): '))
        try:
            cpf_teste = int(cpf)
            teste = 0
            if len(cpf) == 11:
                for i, numero in enumerate(usuarios):
                    if cpf == (numero['cpf']):
                        usuario = usuarios[i]
                if teste > 0:
                    print('CPF já cadastrado')
                elif teste == 0:
                    break
            else:
                print('O CPF deve conter 11 números.')
        except:
            limpar_tela()
            print('Digite apenas números')
    print(usuario)
    numero_conta+= 1
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario})
    print(contas)
    print('Conta criada com sucesso!\n' )


def menu_principal():
    menu= """
Digite o número referente à opção desejada:

    [1] Criar Usuario
    [2] Vincular conta
    [3] Operações
    [0] Sair
"""
    print (menu)
    escolha = input('> ')
    return escolha

def menu_operacoes():
    menu= """
Digite o número referente à opção desejada:

    [1] Depósito
    [2] Saque
    [3] Extrato
    [0] Sair
"""
    print (menu)
    escolha = input('> ')
    return escolha

def limpar_tela():
    os.system('cls')

def depositar(saldo, valor, extrato, /):
    print('Digite o valor do deposito:')
    valor = float(input('> '))
    if valor > 0:
        extrato+= f"Depósito: R$ {valor:.2f}\n"
        saldo+=valor
        os.system('cls')
        print('Operação realizada com sucesso!\n')
    else:
        print('Digite um valor válido\n')

def saque(*, saldo, valor, extrato, limite, numero_saques, limite_saques):
    if numero_saques >= 3:
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

def exibir_extrato(saldo, /, *, extrato):
    if len(extrato) == 0:
        os.system('cls')
        print('Nenhuma operação realizada.\n')
    else:
        os.system('cls')
        print(f"{' - '*4}Extrato{' - '*4}")
        print(extrato)
        print(f"Saldo: R$ {saldo:.2f}")
        print(f"{' - '*10}\n")

def main():
    agencia = '0001'
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    limite_saque = 3
    usuarios = []
    contas = []
    numero_conta = 0
    limpar_tela()
    print('Sistema Bancário')
    while True:
        escolha_principal = menu_principal()
        if escolha_principal == "1":
            criar_usuario(usuarios)

        elif escolha_principal == "2":
            criar_conta(contas, agencia, numero_conta, usuarios)

        elif escolha_principal == "3":
            os.system('cls')
            escolha = menu_operacoes()
            if escolha == "1":
                saque()

            elif escolha == "2":
                depositar()

            elif escolha == "3":
                exibir_extrato()

            elif escolha == "0":
                limpar_tela()
                print("Agradecemos a preferência! Até mais!")
                break

            else:
                limpar_tela()
                print('Operação invalida, tente novamente.')

        elif escolha_principal == "0":
            limpar_tela()
            print("Agradecemos a preferência! Até mais!")
            break

        else:
            limpar_tela()
            print('Operação invalida, tente novamente.')
        


main()