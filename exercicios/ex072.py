print('Exercício:072 - Número por Extenso')
extenso=('Zero','Um','Dois','Três','Quatro','Cinco','Seis','Sete','Oito','Nove','Dez',
         'Onze','Doze','Treze','Quatorze','Quinze','Dezeseis','Dezesete','Dezoito','Dezenove','Vinte')

while True:
    numero = int(input('Digite um número entre 0 e 20: '))
    if 0<= numero <= 20:
        break
    print('Tente novamente. ',end='')

print(f'Você digitou o número {extenso[numero]}')
