num = []
pares = []
impares = []
while True:
    n = int(input('Digite um valor: '))
    num.append(n)
    if n % 2 == 0:
        pares.append(n)
    elif n % 2 == 1:
        impares.append(n)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30)
print(f'Os valores digitados foram {num}')
print(f'Os valores PARES digitados foram {pares}')
print(f'Os valores IMPARES digitado foram {impares}')
