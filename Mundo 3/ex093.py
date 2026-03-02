desempenho = dict()
gol = list()
totgols = 0

desempenho['nome'] = str(input('Nome do Jogador: '))
totpar = int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
for c in range(1, totpar + 1):
    gol.append(int(input(f'    Quantos gols na {c}ª partida? ')))
desempenho['gols'] = gol.copy()
desempenho['total de gols'] = sum(gol)

print('-='*30)
print(desempenho)
print('-='*30)

for k, v in desempenho.items():
    print(f'O campo {k} tem o valor {v}')
print('-='*30)

print(f'O jogador {desempenho["nome"]} jogou {totpar} partidas.')
for i, v in enumerate(desempenho['gols']):
    print(f'    => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {desempenho["total de gols"]} gols.')
