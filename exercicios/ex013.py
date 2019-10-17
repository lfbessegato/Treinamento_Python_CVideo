print('Exercício 13: Calculando o Reajuste de 15%')
salario = float(input('Salário Atual R$'))
salario_novo = salario + (salario*15/100)
print ('O Salário atual de R${:.02f} com o ajuste de 15% ficou em R${:.2f}'.format(salario,salario_novo))