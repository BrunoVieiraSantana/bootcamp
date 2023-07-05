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


def criar_conta(contas, agencia, usuarios):
    while True:
        print('Digite o CPF do Titular da Nova Conta')
        cpf = (input('CPF (somente números): '))
        usuario = None
        for i, numero in enumerate(usuarios):
            if cpf == (numero['cpf']):
                usuario = usuarios[i]
        try:
            if len(usuario) != 0:
                break
        except:
            print('CPF não cadastrado')

    numero_conta = len(contas)+1
    contas.append({"agencia": agencia, "numero_conta": numero_conta, "usuario": usuario, "saldo": 0, "numero_saque":0, "extrato":""})
    limpar_tela()
    print('Conta criada com sucesso!\n' )

def definir_usuario_conta(usuarios, contas):
    print("Digite o número referente ao usuário")
    for i, nome in enumerate(usuarios):
        print(f"    {i+1} - {nome['nome']}")
    escolha = int(input('> '))
    usuario_selecionado = usuarios[escolha-1]

    print("Digite o número referente a conta")
    for conta in contas:
        if usuario_selecionado['cpf'] == (conta['usuario']['cpf']):
            print(f"Conta: {conta['numero_conta']} - Saldo: {conta['saldo']}")
    escolha_conta = int(input('> '))
    for i, conta in enumerate(contas):
        if escolha_conta == (conta['numero_conta']):
            return [conta, i]




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

def depositar(conta, saldo, extrato, /):
    print('Digite o valor do deposito:')
    valor = float(input('> '))
    if valor > 0:
        
        extrato+= f"Depósito: R$ {valor:.2f}\n"
        saldo+=valor
        conta['extrato'] = extrato
        conta['saldo'] = saldo

        os.system('cls')
        print('Operação realizada com sucesso!\n')
    else:
        print('Digite um valor válido\n')

def saque(*, conta, saldo, extrato, limite, numero_saques):
    if numero_saques >= 3:
        os.system('cls')
        print('Número máximo de saques excedido') 
    elif numero_saques < 3:
        print('Digite o valor do saque:')
        valor = float(input('> '))
        if valor > 0 and valor < limite:
            extrato+= f"Saque: R$ {valor:.2f}\n"
            saldo-=valor
            numero_saques+=1

            conta['extrato'] = extrato
            conta['saldo'] = saldo
            conta['numero_saque'] = numero_saques

            os.system('cls')
            print('Operação realizada com sucesso!\n')
        else:
            print('Digite um valor válido, que não ultrapasse os R$ 500,00\n')

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
    limpar_tela()
    print('Sistema Bancário')
    while True:
        escolha_principal = menu_principal()
        if escolha_principal == "1":
            criar_usuario(usuarios)

        elif escolha_principal == "2":
            criar_conta(contas, agencia, usuarios)

        elif escolha_principal == "3":
            limpar_tela()
            login = definir_usuario_conta(usuarios, contas)
            limpar_tela()
            while True:
                escolha = menu_operacoes()
                if escolha == "1":
                    depositar(contas[login[1]],login[0]['saldo'], login[0]['extrato'])

                elif escolha == "2":
                    saque(conta=contas[login[1]], saldo=login[0]['saldo'], extrato=login[0]['extrato'], limite=limite, numero_saques=login[0]['numero_saque'])

                elif escolha == "3":
                    exibir_extrato(login[0]['saldo'], extrato=login[0]['extrato'])

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