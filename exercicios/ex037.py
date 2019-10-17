print('Exercício: 037 - Conversor de Bases Numéricas')
num = int(input('Digite um número Inteiro: '))
print('''Escolha uma das bases para conversão
[ 1 ] - Converter para BINÁRIO'
[ 2 ] - Converter para OCTAL'
[ 3 ] - Converter para HEXADECIMAL''')
opcao = int(input('Sua opção: '))
if opcao == 1:
    print('{} convertido para BINÁRIO é igual a {}'.format(num,bin(num)[2:]))
elif opcao == 2:
    print('{} convertido para OCTAL é igual a {}'.format(num, oct(num)[2:]))
elif opcao == 3:
    print('{} convertido para HEXADECIMAL é igual a  {}'.format(num, hex(num)[2:]))
else:
    print('A opção {} é inválida, favor digitar os valores 1,2 ou 3'.format(opcao))