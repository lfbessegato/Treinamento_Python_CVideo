print ('Exercício 16 - Quebrando um número')
# import math
from math import trunc
num = float(input('Digite um número Real: '))
# novo = math.trunc(num)
novo = trunc(num)
print ('o número digitado foi {} e sua porção inteira é {}'.format(num,novo))