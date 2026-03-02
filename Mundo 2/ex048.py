soma = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
print('A soma dos números IMPARES entre 1 e 500, múltiplos de 3 é {}'.format(soma))