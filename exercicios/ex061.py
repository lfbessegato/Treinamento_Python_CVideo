print('Exercícios:061 - Progressão Aritmética - v2.0')
print('='*20)
print(' 10 Termos de uma PA')
print('='*20)
pr_termo=int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = pr_termo
cont = 1
while cont <= 10:
    print('{} -> '.format(termo),end='')
    termo += razao
    cont += 1
print('ACABOU.')
