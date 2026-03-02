num = [[], []]
for c in range(1, 8):
    n = int(input(f'Digite o {c}° valor: '))
    if n % 2 == 0:
        num[0].append(n)
    elif n % 2 == 1:
        num[1].append(n)
print(f'Os valores PARES digitados foram: {sorted(num[0])}')
print(f'Os valores IMPARES digitados foram: {sorted(num[1])}')
