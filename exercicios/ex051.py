print('Exercícios:051 - Progressão Aritmética')
print('='*20)
print(' 10 Termos de uma PA')
print('='*20)
pr_termo=int(input('Primeiro Termo: '))
razao = int(input('Razão: '))
decimo = pr_termo + (10-1)*razao

for c in range(pr_termo,decimo + razao,razao):
    print('{}'.format(c),'-> ',end='')
print('ACABOU.')
