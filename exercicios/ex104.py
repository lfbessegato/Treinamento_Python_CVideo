print('Exercício:104 - Validando entrada de dados no Python')
def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = n
            ok = True
        else:
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')
        if ok:
            break
    return valor

# Programa Principal
print('-' * 40)
n = leiaInt('Digite um número inteiro: ')
print(f'Você acabou de digitar o número {n}')