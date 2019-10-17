print('Exercício: 034 - Aumentos Múltiplos')
sl = float(input('Qual é o salário do Funcionário? R$ '))
if sl <= 1250:
    novo = sl + (sl * 15 / 100)
else:
    novo = sl + (sl * 10 / 100)

print ('Quem ganhava R$ {:.2f} passa a ganhar R$ {:.2f}'.format(sl, novo))