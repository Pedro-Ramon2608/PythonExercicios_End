num = []
totn = 0
while True:
    n = int(input('Digite um valor: '))
    totn += 1
    num.append(n)
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-=' * 20)
print(f'Foram digitados {totn} valores')
print(f'Os valores digitados em ordem decrescente são {sorted(num, reverse=True)}')
if 5 in num:
    print('O valor 5 foi encontrado na lista')
else:
    print('o valor 5 não foi encontrado na lista')
