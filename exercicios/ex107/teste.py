from ex107 import moeda

print('Exercício:107 - Formatando moedas com o Python')
p = float (input('Digite o preço: R$ '))
print(f'A metade de R${p} é R${moeda.metade(p)}')
print(f'O dobro de R${p} é R${moeda.dobro(p)}')
print(f'Aumentando 10%, temos R${moeda.aumentar(p,10)}')