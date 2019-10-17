print('Exercício:064 - Tratamento de Valores v1.0')
n = qtd = soma = 0
while n != 999:
    n = int(input('Digite um número [999 para PARAR]: '))
    if n != 999:
        soma += n
        qtd += 1
print('Você digitou {} números e a soma entre eles foi {}'.format(qtd,soma))