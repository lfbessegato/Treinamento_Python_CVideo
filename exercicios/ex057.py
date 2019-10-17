print('Exercícios:057 - Validação dos Dados')

sexo = str(input('Informe seu sexo: [M/F]: ')).strip().upper()[0]
while sexo not in 'MnFf':
    sexo=str(input('Dados inválidos, Por favor informe seu sexo [M/F]: ')).strip().upper()[0]
print('Sexo {} registrado com sucesso'.format(sexo))