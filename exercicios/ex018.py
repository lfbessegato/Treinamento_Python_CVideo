print ('Exercício 18: Seno, Coseno e Tangente')
from math import sin, cos, tan,radians
angulo = float(input('Digite o ângulo: '))
seno = sin(radians(angulo))
cosseno = cos(radians(angulo))
tangente = tan(radians(angulo))
print('O ângulo de {}º o SENO é {:.2f} '.format(angulo,seno))
print('O ângulo de {}º o COSSENO é {:.2f} '.format(angulo,cosseno))
print('O ângulo de {}º a TANGENTE é {:.2f} '.format(angulo,tangente))