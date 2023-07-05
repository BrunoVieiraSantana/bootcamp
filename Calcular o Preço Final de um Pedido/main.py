valorHamburguer = float(input())
quantidadeHamburguer = int(input())
valorBebida = float(input())
quantidadeBebida = int(input())
valorPago = float(input())
total = (valorHamburguer*quantidadeHamburguer)+(valorBebida*quantidadeBebida)
troco = valorPago-total

print("O preço final do pedido é R$ {:.2f}. Seu troco é R$ {:.2f}.".format (total, troco))