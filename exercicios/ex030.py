print('Exercício: 030 - Par ou Impar')
numero = int(input('Digite um número qualquer: '))
resultado = numero % 2
if (resultado == 0):
    print ('O número {} é Par'.format(numero))
else:
    print('O número {} é impar'.format(numero))