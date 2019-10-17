print('Exercício: 029 - Radar Eletrônico')
velocidade = float(input('Qual a velocidade atual do carro: '))
permitido = 80
if velocidade > permitido:
   print('\033[31m' + 'MULTADO: Você excedeu a o limite de velocidade permitida que é 80 km/h')
   multa = (velocidade-permitido)*7
   print('E foi multado em R$ {:.2f}'.format(multa)+ '\033[0;0m')

print('Tenha um Bom dia ... Dirija com segurança')
