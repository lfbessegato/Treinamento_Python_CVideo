print ('Aula 12: Condições Aninhadas')
nome = str(input('Qual é o seu Nome: '))
if nome == 'Gustavo':
    print('Que nome bonito!')
elif nome == 'Pedro' or nome == 'Paulo' or nome == 'Maria':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Jessica Marcia Ana Claudia':
    print ('Belo nome feminino')
else:
    print('Seu nome é bem normal.')
print ('Tenha um bom dia, {}!'.format(nome))