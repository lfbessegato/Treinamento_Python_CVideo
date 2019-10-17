print('Exercício: 031 - Custo da Viagem')
viagem=float(input('Qual é a distancia de sua viagem? '))
print('Você está prestes a começar uma viagem de {} Km'.format(viagem))
preco = viagem * 0.50 if viagem <=200 else viagem * 0.45
''''if (viagem <= 200):
    preco = viagem*0.50
else:
    preco = viagem*0.45'''

print('E o preço da passagem será de R$ {:.2f}'.format(preco))