print('Exercício: 039 - Alistamento Militar')
from datetime import date
atual = date.today().year
nasc = int(input('Ano de Nascimento: '))
idade = atual - nasc
print ('Quem nasceu em {} tem {} anos em {}'.format(nasc,idade,atual))
if idade == 18:
    print('tem que se alistar IMEDIATAMENTE')
elif idade < 18:
    saldo = 18 - idade
    ano = saldo + atual
    print('Ainda faltam {} anos para seu alistamento'.format(saldo))
    print('Seu alistamento será em {}'.format(ano))
else:
    saldo = idade - 18
    ano = atual - saldo
    print('Você já deveria ter se alistado há {} anos.'.format(saldo))
    print('Seu alistamento foi em {}'.format(ano))