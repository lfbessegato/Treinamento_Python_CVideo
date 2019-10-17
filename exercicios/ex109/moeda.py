def aumentar(preço=0, taxa=0, formato=False):
    """
    Aumentar -> Função para calcular o aumento de preço
    :param preço: preço
    :param taxa: taxa
    :param formato: True mostra a formatação da Moeda (R$), False mostra o padrão do Python
    :return: res
    """
    res = preço + (preço * taxa/100)
    return res if formato is False else moeda(res)


def diminuir(preço=0, taxa=0, formato=False):
    """
    Dimunuir -> Função para calcular a diminuição do preço
    :param preço: Preço
    :param taxa: Taxa
    :param formato: True mostra a formatação da Moeda (R$), False mostra o padrão do Python
    :return: res
    """
    res = preço - (preço * taxa/100)
    return res if formato is False else moeda(res)


def dobro(preço=0, formato=False):
    """
    Dobro -> Função para calcular o dobro
    :param preço: preço
    :param formato: True mostra a formatação da Moeda (R$), False mostra o padrão do Python
    :return: res
    """
    res = preço * 2
    return res if not formato else moeda(res)


def metade(preço=0, formato=False):
    """
    Metade -> Função para calcular a metade
    :param preço: preço
    :param formato: True mostra a formatação da Moeda (R$), False mostra o padrão do Python
    :return: res
    """
    res = preço / 2
    return res if not formato else moeda(res)


def moeda(preço=0, moeda='R$'):
    """
    Moeda -> Função para formatar a moeda
    :param preço: preço
    :param moeda: tipo da Moeda (R$
    :return: moeda formata (f'{moeda}{preço:>.2f}'.replace('.', ','))
    """
    return f'{moeda}{preço:>.2f}'.replace('.', ',')