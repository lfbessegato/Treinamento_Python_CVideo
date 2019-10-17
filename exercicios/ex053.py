print('Exercícios:053 - Detector de Palídromo')
frase=str(input('Digite uma frase: ')).strip().upper()
palavras=frase.split()
junto=''.join(palavras)
#inverso = ''
inverso = junto[::-1]
'''for letra in range(len(junto)-1,-1,-1):
    inverso += junto[letra]'''
print('O inverso de {} é {}'.format(junto,inverso))
if inverso == junto:
    print('Temos um Palíndromo')
else:
    print('A frase digitada não é um Palíndromo')
