print ('Exercício 10: Coonversão de Moeda')
real = float(input('Quantidade em dinheiro na carteira? R$: '))
dollar = 3.64
euro = 4.25
conversao = real / dollar
print ('Com R${:.2f} você pode comprar US${:.2f}'.format(real,conversao))
conversao = real /euro
print ('Com R${:.2f} você pode comprar EUR${:.2f}'.format(real,conversao))