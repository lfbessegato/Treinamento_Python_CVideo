print('Exercício: 036 - Aprovando Empréstimo')
vl_casa=float(input('valor da Casa R$ '))
vl_salr=float(input('Salário do Comprador R$ '))
qtd_anos=int(input('Quantos anos de financiamento: '))
minimo = vl_salr * 30 / 100
vlr_presta=vl_casa/(qtd_anos*12)
print('Para pagar uma casa de R$ {:.2f} em {} anos a prestação será de R$ {:.2f}'.format(vl_casa,qtd_anos,vlr_presta))
if vlr_presta > minimo:
    print('Empréstimo NEGADO')
else:
    print('Empréstimo CONCEDIDO')