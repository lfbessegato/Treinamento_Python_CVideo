print('Exercício:101 - Funções para votação')


def voto(ano):
    ## Escopo de importação
    from datetime import date
    atual = date.today().year
    idade = atual - ano

    if idade < 16:
        return f'Com {idade} anos: NÃO VOTA.'
    elif 16 <= idade < 18 or idade > 65:
        return f'Com {idade} anos: VOTO OPCIONAL.'
    else:
        return f'Com {idade} anos: VOTO OBRIGATÓRIO.'

# Programa Principal
print('-' * 30)
nasc = int(input('Em que ano você nasceu? '))
print(voto(nasc))