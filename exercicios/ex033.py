print('Exercício: 033 - Menor e Maior Valor')
n1 = int(input('Primeiro Valor: '))
n2 = int(input('Segundo Valor: '))
n3 = int(input('Terceiro Valor: '))

# Verificando quem é o menor
menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

#Verificando quem é o maior
maior = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

print('O menor valor digitado foi {}'.format(menor))
print('O maior valor digitado foi {}'.format(maior))