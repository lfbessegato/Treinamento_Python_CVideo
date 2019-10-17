print('Exercício: 040 - Aquele clássico de Média')
n1 = float(input('Primeira Nota: '))
n2 = float(input('Segunda Nota: '))
media = (n1 + n2) / 2
print ('Tirando nota {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(n1,n2,media))
if 7 > media >= 5:
    print('\033[1;33m o aluno está de RECUPERAÇÃO')
elif media < 5:
    print('\033[1;31m o aluno está REPROVADO')
else:
    print ('\033[1;34m o aluno está APROVADO')