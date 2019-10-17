print('Aula: 21 - Funções - Parte 2')
def contador (i,f,p):
    """
    -> Faz uma contagem e mostra na tela
    :param i: inicio da contagem
    :param f: fim da contagem
    :param p: passo da contagem
    :return: sem retorno
    """
    c = i
    while c <= f:
        print(f'{c} ',end='')
        c += p
    print('FIM!')
def somar(a=0,b=0,c=0):
    """
    -> Faz a soma de três valores e mostra na tela.
    :param a: o primeiro valor
    :param b: o segundo valor
    :param c: o terceiro valor
    :return: nenhum retorno
    """
    s = a + b + c
    print(f'A soma é {s}')

def teste():
    x = 8
    print(f'Na função teste n vale {n}')
    print(f'Na função teste x vale {x}')

def funcao():
    n1 = 4
    print(f'N1 dentro vale {n1} ')

def somar_retorno(a=0,b=0,c=0):
    s = a + b + c
    return s

def fatorial(num=1):
    f = 1
    for c in range(num, 0, -1):
        f *= c
    return f

# Programa Principal
n = 2

print(f'No programa principal n vale {n}')
teste()
contador(2,10,2)
help(contador)
somar(8,4)
help(somar)

# Exemplo de Escopo Global e Local (exemplo N1 no Principal e N1 na função
n1 = 2
print(f'N1 fora vale {n1}')
funcao()

# exemplo de chamada da função com o retorno
r1 = somar_retorno(3,2,5)
r2 = somar_retorno(2,2)
r3 = somar_retorno(6)
print(f'Meus cáluclos deram {r1},{r2},{r3}')

f1 = fatorial(5)
f2 = fatorial(4)
f3 = fatorial()
print(f'Os resultados são {f1},{f2} e {f3}')