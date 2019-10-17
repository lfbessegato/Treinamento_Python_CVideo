print('Aula: 11 - Cores no Terminal')
print('\033[1;31;43mOlá Mundo!\033[m')
print('\033[4;30;45mOlá Mundo!\033[m')
print('\033[7;30mOlá Mundo!\033[m')
print('\033[7;33;44mOlá Mundo!\033[m')

a = 3
b = 5
print('Os Valores são \033[32m{}\033[m e \033[31m{}\033[m !!!'.format(a,b))

nome = 'Luciano'
print('Olá muito prazer em te conhecer !!! {}{}{}'.format('\033[4;34m',nome,'\033[m'))