print ('Exercício 06 - Mostre o Dobro, Triplo e a Raiz Quadrada')
n = float(input('Digite um número: '))
print ('Analisando o número {} \n O Dobro é {}, \n O triplo é {} \n e a Raiz Quadrada é {:.2f}'.format(n,(n*2),(n*3),(n**(1/2))))
print('A Raiz Quadrada também pode ser executada com a função pow {:.2f}'.format(pow(n,1/2)))