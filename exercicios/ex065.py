print('Exercício:065 - Maior e Menor Valor')
resp = 'S'
total = soma = media = maior = menor = 0
while resp in 'Ss':
    n = int(input('Digite um número: '))
    resp=str(input('Quer Continuar [S/N]: ')).upper().strip()[0]
    total += 1
    if total == 1:
        maior = n
        menor = n
    else:
        if n > maior:
            maior = n
        if n < menor:
            menor = n
    soma += n
media = soma / total
print('Você digitou {} números e a média foi {}'.format(total,media))
print('O Maior valor foi {} e o Menor valor foi {}.'.format(maior,menor))


