print('Exercício:068 - Jogo do Par ou Impar')
from random import randint
print('=-'*15)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-'*15)
total = vit = 0
while True:
    jogador = int(input('Diga um valor: '))
    computador = randint(0,10)
    total = jogador + computador
    tipo = ' '
    while tipo not in 'PI':
        tipo = str(input('Par ou Ímpar [P/I]: ')).strip().upper()[0]
    print('-'*65)
    print(f'Você jogou {jogador} e o computador jogou {computador}. O total de {total}. ', end='')
    print('DEU PAR' if total % 2 == 0 else 'DEU IMPAR')
    print('-'*65)
    if tipo == 'P':
        if total % 2 == 0:
            print('Você VENCEU!')
            vit += 1
        else:
            print ('Você PERDEU"')
            break
    elif tipo == 'I':
        if total % 2 == 1:
            print ('Você VENCEU!')
            vit += 1
        else:
            print ('Você PERDEU!')
            break
    print('Vamos jogar novamente ...')
print(f'GAME OVER! Você venceu {vit} vezes')