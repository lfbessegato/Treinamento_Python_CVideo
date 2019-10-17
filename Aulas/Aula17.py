print('Aula:17 - Lista - Parte 1')
num = [2,5,9,1]
print(num)
num[2]=3
print(num)
num.append(7)
print(num)
num.insert(2,0)
print(num)
num.sort()
print(num)
num.sort(reverse=True)
print(num)
print(f'Essa lista tem {len(num)} elementos')
num.pop(2)
print(num)
print(f'Essa lista tem {len(num)} elementos')
if 4 in num:
    num.remove(4)
else:
    print('Não achei o número 4')
print('-='*20)
valores=[]
valores.append(9)
valores.append(5)
valores.append(4)
for v in valores:
    print(f'{v}...')

for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da Lista.')

print('-='*20)
valores=[]
for cont in range(0,6):
    valores.append(int(input('Digite um Valor: ')))
for c,v in enumerate(valores):
    print(f'Na posição {c} encontrei o valor {v}...')
print('Cheguei ao final da Lista.')

print('-='*20)
a = [2,3,4,5]
b = a
print(f'Lista A {a}')
print(f'Lista B {b}')
b[2]=19
print(f'Lista A {a}')
print(f'Lista B {b}')

print('-='*20)
a = [2,3,4,5]
b = a[:]
print(f'Lista A {a}')
print(f'Lista B {b}')
b[2]=19
print(f'Lista A {a}')
print(f'Lista B {b}')
