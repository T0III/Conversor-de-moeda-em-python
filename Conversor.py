##dolar = R$5,19 (utilizar cotação atual)

valor = float(input('Quanto você tem na carteira? R$'))
dolar = valor / 5.19

## Dividir o valor input pelo valor da moeda que quer converter.

print('Com R${:.2f} você pode comprar em dólares o total de: US${:.2f}'.format(valor, dolar))





