print('Exercício:081 - Extraindo dados de uma lista')
valores = []
while True:
    valores.append(int(input('Digite um valor: ')))
    resp = str(input('Quer continuar? [S/N] '))
    if resp in 'Nn':
        break
print('-='*30)
print(f'Você digitou {len(valores)} elementos')
valores.sort(reverse=True)
print(f'os valores em ordem descrescente são {valores}')
if 5 in valores:
    print('O valor 5 faz parte da lista!')
else:
    print('O valor 5 não foi encontrado na lista!')