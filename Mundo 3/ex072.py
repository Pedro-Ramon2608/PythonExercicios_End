num = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco',
       'seis', 'sete', 'oito', 'nove', 'dez', 'onze',
       'doze', 'treze', 'catorze', 'quinze', 'dezesseis',
       'dezessete', 'dezoito', 'dezenove', 'vinte')
numero = int(input('Digite um número entre 0 e 20: '))
while numero < 0 or numero > 20:
    numero = int(input('Tente novamente um número entre 0 e 20: '))
print(f'Você digitou o número {num[numero]}')
continuar = ' '
while True:
    continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'S':
        numero = int(input('Digite um número entre 0 e 20: '))
        while numero < 0 or numero > 20:
            numero = int(input('Tente novamente um número entre 0 e 20: '))
        print(f'Você digitou o número {num[numero]}')
    elif continuar == 'N':
        break
