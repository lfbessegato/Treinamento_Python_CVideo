print('Exercícios:052 - Números Primos')
numero=int(input('Digite um número: '))
qtd = 0
for c in range(1,numero+1):
    if numero % c == 0:
        print('\033[00;33m',end=' ')
        qtd += 1
    else:
        print('\033[00;31m', end=' ')
    print('{}'.format(c), end=' ')
print('\n\033[mO número {} foi divísivel {} vezes'.format(numero,qtd))
if qtd == 2:
    print('por isso ele é PRIMO')
else:
    print('por isso ele NÃO É PRIMO')
