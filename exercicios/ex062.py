print('Exercícios:062 - Progressão Aritmética - v3.0')
print('='*20)
print(' 10 Termos de uma PA')
print('='*20)
pr_termo=int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
termo = pr_termo
cont = 1
total = 0
mais = 10
while mais !=0:
    total = total + mais
    while cont <= total:
        print('{} -> '.format(termo),end='')
        termo += razao
        cont += 1
    print('Pausa.')
    mais = int(input('Quantos termos você quer mostrar a mais? '))
print('Progressão finalizada com {} termos mostrados.'.format(total))