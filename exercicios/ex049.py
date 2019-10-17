print('Exercício:049 - Tabauada versão 2.0')
num = int(input('Digite um número para saber sua tabuada: '))
print('-='*6)
for c in range(0,11):
    print('{:2} x {:2}'.format(num,c,num*c))
