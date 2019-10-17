print('Exercícios:054 - Grupo de Maioridade')
from datetime import date
totmaior = 0
totmenor = 0
for pessoa in range(1,8):
    ano_nasc=int(input('Em que ano a {}ª pessoa nasceu?: '.format(pessoa)))
    ano_atual=date.today().year
    idade = ano_atual - ano_nasc
    if idade >= 21:
        totmaior += 1
    else:
        totmenor += 1
print('Ao todo tivemos {} pessoas maiores de idade'.format(totmaior))
print('E também tivemos {} pessoas menores de idade'.format(totmenor))
