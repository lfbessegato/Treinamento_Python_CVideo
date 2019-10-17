print('Exercício:097 - Um Print especial')
def escreva(msg):
    tam = len(msg)+4
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)

# Programa Principal
escreva('Luciano Bessegato')
escreva('Curso de Python no Youtube')
escreva('CeV')