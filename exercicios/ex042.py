print('Exercício: 042 - Analisador de Triângulo v2.0')
print('-=-' * 20)
print('ANALISADOR DE TRIANGULO V2.0')
print('-=-' * 20)
r1 = float(input('Primeiro segmento: '))
r2 = float(input('Segundo Segmento: '))
r3 = float(input('Terceiro Segmento: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r2 + r1:
    print ('Os segmentos acima PODEM FORMAR um Triângulo. ',end='')
    if r1 == r2 == r3:
        print('EQUILÁTERO !')
    elif r1 != r2 != r3 != r1:
        print('ESCALENO !')
    else:
        print('ISÓSELES !')
else:
    print ('Os segmentos acima NÃO PODEM FORMAR Triângulo')