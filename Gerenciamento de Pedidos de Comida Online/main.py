def main():
    n = int(input())
 
    total = 0
 
    for i in range(1, n + 1):
        pedido = input().split(" ")
        nome = pedido[0]
        valor = float(pedido[1])
        total += valor
 
    cupom = input()
    if cupom == '10%':
        total_cupom =  total - (10*total/100)
    elif cupom == '20%':
        total_cupom =  total - (20*total/100)

    print('Valor total: {:.2f}'.format(total_cupom))
 
if __name__ == "__main__":
    main()