desempenho = dict()
lista = list()
gol = list()
totgols = 0

while True:
    print('-'*30)
    desempenho['nome'] = str(input('Nome do Jogador: '))
    totpar = int(input(f'Quantas partidas {desempenho["nome"]} jogou? '))
    for c in range(1, totpar + 1):
        gol.append(int(input(f'    Quantos gols na {c}ª partida? ')))
    desempenho['gols'] = gol.copy()
    desempenho['total de gols'] = sum(gol)
    lista.append(desempenho.copy())
    gol.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

print('-='*30)
print(f'{"Cod":<3}  {"Nome":<15} {"Gols":<20} {"Total":^9}')
print('-'*52)
for i, v in enumerate(lista):
    print(f'{i+1:^3}  {lista[i]["nome"]:<15} {str(lista[i]["gols"]):<20} {lista[i]["total de gols"]:^9}')

while True:
    print('-' * 52)
    mostrar = int(input('Mostrar dados de qual jogador? (999 para parar) '))
    if mostrar == 999:
        break
    if mostrar > len(lista):
        print(f'ERRO! Não existe jogador com código {mostrar}! Tente novamente.')
    elif mostrar <= 0:
        print(f'ERRO! Não existe jogador com código {mostrar}! Tente novamente.')
    else:
        if mostrar <= len(lista):
            print(f'-- LEVANTAMENTO DO JOGADOR {lista[mostrar-1]["nome"]}:')
            for i, v in enumerate(lista[mostrar-1]["gols"]):
                print(f' >> No jogo {i+1} fez {v} gols.')
print('>> ENCERRADO <<')
