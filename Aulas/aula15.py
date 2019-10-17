print('Aula 15: Interrupção do While')
n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
print('A soma vale {}'.format(s))
print('utilizando f´s strings')
print(f'A soma vale {s}')

print('Exemplo de F´string')
nome = 'José'
idade = 33
salario = 987.3
print(f'O {nome} tem {idade} anos e ganha R$ {salario:.2f}')