num = int(input('Digite um número e veja o fatorial dele: '))
fator = 1
c = num
while c > 1:
    fator = fator * c
    c = c - 1
print('O fatorial de {} é igual a {}'.format(num, fator))
