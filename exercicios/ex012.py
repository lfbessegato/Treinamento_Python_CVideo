print('Exercício 12: Calculando Desconto de 5%')
preco = float(input('Preço do Produto R$ '))
desconto = preco * 5/100
pr_atual = preco - desconto
print('O preço do produto é R$ {:.2f}, com o desconto de 5% sai por R${:.2f}'.format(preco,pr_atual))