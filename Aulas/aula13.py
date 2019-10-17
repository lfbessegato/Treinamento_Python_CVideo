print('Aula: 13 - Estrutura de Repetição for')
for c in range(6, 0, -1):
    print(c)
print('FIM - Contando para tras')


n = int(input('Digite um número: '))
for c in range(0,n+1):
    print(c)
print ('FIM - Numero digitado')

for c in range(0,7,2):
    print(c)
print('FIM-Pulando de 2 em 2')

i = int(input('Inicio: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i,f+1,p):
    print(c)
print('FIM - Contagem interativa')

s = 0
for c in range(0,4):
    n = int(input('Digite um número: '))
    s += n
print('O Somatório de todos os números foi {}'.format(s))