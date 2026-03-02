dados = list()
principal = list()
maior = menor = 0
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    if len(principal) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    principal.append(dados[:])
    dados.clear()
    r = ' '
    while r not in 'SN':
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r in 'N':
        break
print('-=' * 20)
print(f'Ao todo você cadastrou {len(principal)} pessoas.')
print(f'O maior peso foi de {maior}Kg. Peso de ', end='')
for p in principal:
    if p[1] == maior:
        print(f'[{p[0]}] ', end='')
print(f'\nO menor peso foi de {menor}Kg. Peso de ', end='')
for p in principal:
    if p[1] == menor:
        print(f'[{p[0]}] ', end='')
