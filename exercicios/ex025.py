print('Exercício: 025 - Procurando uma string dentro da outra')
nome = str(input("Digite seu nome completo: ")).strip()
print("O {} tem Silva no Nome? ".format(nome.title()),("silva" in nome.lower()))
