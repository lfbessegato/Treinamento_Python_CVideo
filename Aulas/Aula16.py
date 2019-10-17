print('Aula 16 - Variáveis Compostas - Tupla')
lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim')
print(lanche)

print(lanche[1])
print(lanche[-2])
print(lanche[1:3])
print(lanche[1:])
print(lanche[:3])
print(lanche[-3:])

for comida in lanche:
    print(f'Eu vou comer {comida}')
print ('Comi para caramba.')

print('Outra forma de executar o For')
for cont in range(0, len(lanche)):
    print(lanche[cont])

print('função enumerate()')
# com o enumerate é possível mostrar a posição e o dado
for pos, comida in enumerate(lanche):
    print(f'Vou comer {comida}, na posição {pos}')

print('Sorted - mostra a Tupla organizada')
print(sorted(lanche))
print(lanche)

print('Concatenar Tuplas')
a = (2,5,4)
b = (5,8,1,2)
c = a + b
print(c)
print('Função index')
print(c.index(8))