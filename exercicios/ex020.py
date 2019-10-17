print('Exercício 20 - Sorteando uma ordem')
from random import shuffle
aluno1 = input('Primeiro Aluno: ')
aluno2 = input('Segundo Aluno: ')
aluno3 = input('Terceiro Aluno: ')
aluno4 = input('Quarto Aluno: ')
lista = [aluno1,aluno2,aluno3,aluno4]
shuffle(lista)
print('A ordem de apresentação será ')
print(lista)