print ('Aula 7 - Operadores Aritméticos')
n1 = int(input('Digite um valor: '))
n2 = int(input('Digite outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
su = n1 - n2
di = n1 // n2
e = n1 ** n2
print ('A soma é {}, \n o produto é {}, \n a divisão é {:.3f}, a subtração é {}'.format(s, m, d, su),end=' >>> ')
print ('A Divisão Inteira {}, a Potência {}'.format(di, e))