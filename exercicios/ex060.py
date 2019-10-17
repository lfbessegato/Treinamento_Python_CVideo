print('Exercício:060 - Calculando o Fatorial')
n=int(input('Digite um número para Calcular seu fatorial: '))
c = n
f = 1
print('Calculando {}! = '.format(n),end='')
while c > 0:
      print('{}'.format(c),end='')
      print(' x ' if c > 1 else ' = ', end='')
      f *= c
      c -= 1
print('{}'.format(f))