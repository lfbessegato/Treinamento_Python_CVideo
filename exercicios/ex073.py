print('Exercício:073 - Tuplas com Times de Futebol')
times=('Palmeiras', 'Flamengo', 'Internacional', 'Grêmio', 'São Paulo',
       'Atlético Mineiro', 'Atlético Paranaense', 'Cruzeiro', 'Botafogo', 'Santos',
       'Bahia', 'Corinthians', 'Fluminense', 'Vasco da Gama',
       'Ceará', 'Chapecoense', 'Sport', 'América', 'Vitória', 'Paraná')

print('-='*30)
print(f'LISTA DE TIMES DO BRASILEIRÃO 2018: {times}')
print('-='*30)
print(f'OS 5 PRIMEIROS COLOCADOS SÃO: {times[0:5]}')
print('-='*30)
print(f'OS 4 ÚLTIMOS COLOCADOS: {times[-4:]}')
print('-='*30)
print(f'TIMES EM ORDEM ALFABÉTICA: {sorted(times)}')
print('-='*30)
print(f'O Chapecoense está na {times.index("Chapecoense")+1}ª posição')