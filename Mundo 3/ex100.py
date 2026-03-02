from random import randint
from time import sleep
numeros = list()
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='')
    for c in range(0, 5):
        numeros.append(randint(0, 10))
        print(f'{numeros[c]} ', end='')
        sleep(0.5)
    print('PRONTO!')


def somapar(lista):
    soma = 0
    for c in lista:
        if c % 2 == 0:
            soma += c
    print(f'Somando os valores PARES de {lista}, temos {soma}')


sorteia(numeros)
somapar(numeros)
