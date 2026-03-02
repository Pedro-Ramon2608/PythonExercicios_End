num = int(input('Digite um número para ver o fatorial dele: '))
fator = 1
for c in range(num, 0, -1):
    fator = fator * c
print('O fatorial de {} é igual a {}'.format(num, fator))
