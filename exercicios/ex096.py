print('Exercícios:096 - Função que calcula área')
def area(larg , comp):
    a = (larg * comp)
    print(f'A área de um terreno {larg}x{comp} é de {a}m2.')


# Programa Principal
print(' Controle de Terrenos ')
print('-' * 20)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))
area(l , c)