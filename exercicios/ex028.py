print('Exercício: 028 - Jogo da Advinhação v.1.0')
from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador Pensar
print('-=-' * 20)
print('Vou pensar em um número entre 0 e 5. Tente advinhar ... ')
print('-=-' * 20)
jogador = int(input('Em que número eu pensei? ')) # Jogador tenta advinhar
print('PROCESSANDO ...')
sleep(3)
if jogador == computador:
    print ('PARABÉNS ... você conseguiu me vencer ...')
else:
    print ('GANHEI ... Eu pensei no número {} e não no {}!'.format(computador,jogador))
