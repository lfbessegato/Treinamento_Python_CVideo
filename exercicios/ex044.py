print('Exercícios: 044 - Gerenciador de Pagamentos')
print('{:=^40}'.format(' LOJAS BESSEGATO '))
compra = float(input('Preço das Compras R$: '))
print('''FORMAS DE PAGAMENTO
[ 1 ] à vista Dinheiro/Cheque
[ 2 ] à vista no Cartão
[ 3 ] 2x cartão
[ 4 ] 3x ou mais no Cartão''')
opcao=int(input('Qual a opção de pagamento?: '))

if opcao == 1:
    total = compra - (compra * 10 /100)
elif opcao == 2:
    total = compra - (compra * 5 / 100)
elif opcao == 3:
    total = compra
    parcela = total / 2
    print ('Sua compra será parcelada em 2x de R${:.2f} SEM JUROS'.format(parcela))
elif opcao == 4:
    total = compra + (compra * 20 / 100)
    totalparc = int(input('Quantas parcelas?: '))
    parcelas = total / totalparc
    print('Sua compra será parcelada em {}x de R${:.2f} COM JUROS'.format(totalparc,parcelas))
else:
    total = compra
    print('\033[00;31;40m OPÇÂO INVÁLIDA DE PAGAMENTO.Tente Novamente...')
print ('Sua compra de R${:.2f} vai custar R${:.2f} no final.'.format(compra,total))

