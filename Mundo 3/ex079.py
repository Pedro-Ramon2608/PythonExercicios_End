num = []
while True:
    n = int(input('Digite um valor: '))
    if n not in num:
        num.append(n)
        print('Valor adicionado.')
    else:
        print('Valor duplicado! Não vou adicionar.')
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('=-' * 20)
print(f'Você digitou os valores {sorted(num)}')
