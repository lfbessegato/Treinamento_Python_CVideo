print('Exercício:043 - Calculo do IMC')
peso = float(input('Qual é o seu peso? (kg): '))
altura = float(input('Qual é a sua altura? (m): '))
imc = peso / (altura**2)
print('O IMC dessa pessoa é {:.1f}'.format(imc))
if imc < 18.5:
    print('Você está ABAIXO do Peso normal.')
elif 18.5 <= imc < 25:
    print ('PARABÉNS, você está na faixa de PESO NORMAL.')
elif 25 <= imc < 30:
    print('Você está em SOBREPESO.')
elif 30 <= imc <40:
    print('Você está em OBESIDADE.')
else:
    print('Você está em OBESIDADE MÓRBIDA, cuidado!')