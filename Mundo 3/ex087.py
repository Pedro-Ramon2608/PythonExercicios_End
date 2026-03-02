matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma = somaterc = maior = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('-=' * 20)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end=' ')
        if matriz[l][c] % 2 == 0:
            soma += matriz[l][c]
        if c == 2:
            somaterc += matriz[l][c]
        if l == 1 and c == 0:
            maior = matriz[l][c]
        else:
            if l == 1 and matriz[l][c] > maior:
                maior = matriz[l][c]
    print()
print('-=' * 20)
print(f'A soma de todos os valores PARES digitados foi {soma}.')
print(f'A soma dos valores da Terceira Coluna foi {somaterc}.')
print(f'O Maior valor digitado na Segunda Linha foi {maior}.')
