from random import randint
from time import sleep
sorte = list()
dados = list()
print('-' * 30)
print(f'{"MEGA SENA":^30}')
print('-' * 30)
jogos = int(input('Quantos jogos deseja que eu sorteie? '))
print(f'-=-=-=-=-=-= SORTEANDO {jogos} JOGOS -=-=-=-=-=-=')
for c in range(0, jogos):
    sleep(1)
    for n in range(0, 6):
        dados.append(randint(1, 60))
        if dados in sorte:
            dados.pop()
            dados.append(randint(1, 60))
        sorte.append(dados[:])
        dados.clear()
    print(f'Jogo {c+1}: {sorte}')
    sorte.clear()
print('-=-=-=-=-=-=-= < BOA SORTE > -=-=-=-=-=-=-=')
