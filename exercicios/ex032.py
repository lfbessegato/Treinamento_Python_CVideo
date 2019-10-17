from datetime import date
print('Exercício: 032 - Ano Bissexto')
ano=int(input('Que ano quer analisar? Coloque 0 para analisar o Ano Atual: '))

if (ano ==0):
    ano = date.today().year

if (ano%4==0 and ano % 100 != 0 or ano % 400 ==0):
    print('O Ano {} é BISSEXTO'.format(ano))
else:
    print('O Ano {} Não é BISSEXTO'.format(ano))

