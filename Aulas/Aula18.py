print('Aula:18 - Listas - Parte 2')
teste = list()
teste.append('Gustavo')
teste.append(40)
print(f'Lista Teste: {teste}')
galera=list()
galera.append(teste[:])
print(f'Lista galera: {galera}')
teste[0]='Maria'
teste[1]=22
galera.append(teste[:])
print(f'Lista galera: {galera}')
print('-='*30)
galera=[['João',19],['Ana',33],['Joaquim',13],['Maria',45]]
print(f'Lista galera: {galera}')
print(f'Lista galera[0]: {galera[0]}')
print(f'Lista galera[0][0]: {galera[0][0]}')
print(f'Lista galera[2][1]: {galera[2][1]}')
for p in galera:
    print(f'{p[0]} tem {p[1]} anos de idade')
print('-='*30)
galera=list()
dado = list()
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()
print(galera)
print('-='*30)
galera=list()
dado = list()
totmai = totmen = 0
for c in range(0,3):
    dado.append(str(input('Nome: ')))
    dado.append(int(input('Idade: ')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
print(f'Temos {totmai} maiores e {totmen} menores de idade')