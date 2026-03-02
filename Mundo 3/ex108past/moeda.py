def metade(n=0):
    return n / 2

def dobro(n=0):
    return n * 2

def aumentar(n=0, taxa=0):
    valor = n + (n*taxa/100)
    return valor

def diminuir(n=0, taxa=0):
    valor = n - (n*taxa/100)
    return valor

def moeda(n=0, moeda='R$'):
    return f'{moeda}{n:.2f}'.replace('.', ',')
