tabela = ('Palmeiras', 'São Paulo', 'Fluminense', 'Bahia', 'Athletico-PR',
          'Bragantino', 'Chapecoense', 'Mirassol', 'Coritiba', 'Flamengo',
          'Botafogo', 'Corinthians', 'Grêmio', 'EC Vitória', 'Atlético-MG',
          'Remo', 'Vasco da Gama', 'Santos', 'Internacional', 'Cruzeiro')
print('-='*23)
print('Tabela dos 5 primeiros colocados do Brasileirão')
for pos, time in enumerate(tabela[0: 5]):
    print(pos+1, '° ', time)

print('-='*23)
print('Tabela dos 4 últimos colocados do Brasileirão')
for pos, time in enumerate(tabela[16:]):
    print(f'{pos+17}° {time}')
print('-='*23)
print('Times do Brasileirão em ordem alfabetica')
for pos, time in enumerate(sorted(tabela)):
    print(time)
print('-='*23)
print(f'O time da Chapecoense está na {tabela.index('Chapecoense')+1}ª posição')
