print ('Exercício 17 - Catetos e Hipotenusa')
from math import hypot
ca = float(input('Comprimento do cateto adjacente: '))
co = float(input('Comprimento do cateto oposto: '))
# hi = (co**2+ca**2)**(1/2)
# print ('A hipotenusa vai medir {:.2f}'.format(hi))
print ('A hipotenusa vai medir {:.2f}'.format(hypot(ca,co)))