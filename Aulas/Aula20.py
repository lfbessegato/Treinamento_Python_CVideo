print('Aula: 20 - Funções (Parte 1)')
def titulo(msg):
    print('-='*30)
    print(msg)
    print('-='*30)


def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(f'A soma de A + B = {s}')

def contador(* núm):
    for valor in núm:
        print(f'{valor} ', end='')
    print('FIM!')

    tam = len(núm)
    print(f'Recebi os valores {núm} e são ao todo {tam}')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] *= 2
        pos += 1

# PROGRAMA PRINCIPAL
titulo('CADASTRO')
titulo('APRENDA PYTHON')
titulo('EXEMPLOS')
soma(4, 5)
soma(8, 9)
soma(2, 1)
titulo('Exemplo de parâmetros empacotadas')
contador(2, 1, 7)
contador(8, 0)
contador(4, 4, 7, 6, 2)
titulo('Exemplo de parâmetros como Listas')
valores= [6, 3, 9, 1, 0, 2]
dobra(valores)
print(valores)