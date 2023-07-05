numPedidos = int(input())

for i in range(1, numPedidos + 1):
    prato = input()
    calorias = int(input())
    resposta = input()
    if resposta == 'n':
        tipo = 'Nao-vegano'

    elif resposta == 's':
        tipo = 'Vegano'

    print('Pedido {}: {} ({}) - {:.0f} calorias'.format(i, prato, tipo, calorias))

