def moeda(n=0, mod='R$'):
    """
    -> conversor para moeda
    :param n: recebe o valor que o usuario quer transformar em moeda
    :param mod: recebe o símbolo da moeda
    :return: retorn o valor da moeda modificada de acordo com as requisições
    """
    return f'{mod}{n:.2f}'.replace('.', ',')


def metade(n=0, mod=False):
    """
    -> calcula a metade do valor
    :param n: recebe o valor que o usuario quer transformar em metade
    :param mod: recebe se esse valor vai ser moeda
    :return: retorna o resultado da operação
    """
    if mod:
        return moeda(int(n / 2))
    else:
        return n / 2


def dobro(n=0, mod=False):
    """
    -> calcula o dobro do valor
    :param n: recebe o valor que o usuario quer transformar em dobro
    :param mod: recebe se esse valor vai ser moeda
    :return: retorna o resultado do dobro
    """
    if mod:
        return moeda(n * 2)
    else:
        return n * 2


def aumentar(n=0, taxa=0, mod=False):
    """
    -> calcula o aumento do valor
    :param n: recebe o valor que o usuario quer transformar em aumento
    :param taxa: recebe a taxa que esse valor vai ser aumentado
    :param mod: recebe se esse valor vai ser moeda
    :return: retorna o resultado do aumento
    """
    valor = n + (n*taxa/100)
    if mod:
        return moeda(int(valor))
    else:
        return valor


def diminuir(n=0, taxa=0, mod=False):
    """
    -> calcula a diminuição do valor
    :param n: recebe o valor que o usuário quer diminuir
    :param taxa: recebe a taxa que esse valor vai ser diminuir
    :param mod: recebe se esse valor vai ser moeda
    :return: retorna o resultado da diminuição
    """
    valor = n - (n*taxa/100)
    if mod:
        return moeda(int(valor))
    else:
        return valor
