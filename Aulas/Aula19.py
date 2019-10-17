print('Aula: 19 - Dicionários')
pessoas={'nome':'Luciano','Sexo':'M','Idade':48}
print(pessoas)
print(pessoas['nome'])
print(pessoas['Idade'])
print(f'O {pessoas["nome"]} tem {pessoas["Idade"]} anos.')
print('Utilizando dicionários (Keys, Values e Items')
print('pessoas.keys(): ', pessoas.keys())
print('pessoas.values(): ', pessoas.values())
print('pessoas.items(): ', pessoas.items())
print('Utilizando um Laço')
for k in pessoas.keys():
    print(k)
for k in pessoas.values():
    print(k)
for k,v in pessoas.items():
    print(f'{k} = {v}')
print('Apagar Elementos')
del pessoas['Sexo']
for k,v in pessoas.items():
    print(f'{k} = {v}')
print('Alterar um Elemento')
pessoas['nome']='Márcia'
for k,v in pessoas.items():
    print(f'{k} = {v}')
print('Adicionando um Elemento')
pessoas['peso']=95.1
for k,v in pessoas.items():
    print(f'{k} = {v}')
print('-='*30)
print('Listas e Dicionários')
brasil=[]
estado1={'uf':'Rio de Janeiro','sigla':'RJ'}
estado2={'uf':'São Paulo','sigla':'SP'}
brasil.append(estado1)
brasil.append(estado2)
print(estado1)
print(estado2)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['uf'])
print(brasil[1]['sigla'])
print('-='*30)
estado=dict()
brasil=list()
for c in range(0,3):
    estado['uf']=str(input('Unidade Federativa: '))
    estado['sigla']=str(input('Sigla do Estado: '))
    brasil.append(estado.copy())
print(brasil)
for e in brasil:
    print(e)
for e in brasil:
    for k,v in e.items():
        print(f'O campo {k} tem valor {v}')