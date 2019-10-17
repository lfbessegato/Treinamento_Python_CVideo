from ex112.utilidadescev import moeda
from ex112.utilidadescev import dado

print('Exercício:112 - Entrada de dados monetários')
p = dado.leiaDinheiro('Digite o preço: R$ ')
moeda.resumo(p,20,12)