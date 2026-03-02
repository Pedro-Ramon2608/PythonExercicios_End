frase = str(input('Digite uma frase: ')).strip().upper()
pal = frase.replace(' ', '')
inv = ''
for letra in range(len(pal) - 1, -1, -1):
    inv += pal[letra]
print('O inverso de {} é {}.'.format(pal, inv))
if pal == inv:
    print('Esta palavra é um Palíndromo.')
else:
    print('Esta palavra NÃO é um Palíndromo.')
