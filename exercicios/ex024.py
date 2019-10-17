print('Exercício: 024 - Primeiras letras de uma String - Cidade com o nome Santo')
cid = str(input('Digite o nome da Cidade: ')).strip()
print("A cidade {} tem Santo no Nome? ".format(cid.title()),cid[:5].upper() == "SANTO")