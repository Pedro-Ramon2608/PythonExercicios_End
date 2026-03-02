num = (int(input('Digite um número: ')),
       int(input('Digite outro: ')),
       int(input('Digite outro: ')),
       int(input('Digite outro: ')))

print(f'Você digitou os valores {num}')
print(f'O número 9 apareceu {num.count(9)} vezes')
if 3 in num:
    print(f'O número 3 apareceu na {num.index(3)+1}ª posição')
else:
    print('O número 3 não foi digitado em nenhuma posição')

print('Os valores pares digitados foram: ',end='')
for c in num:
    if c % 2 == 0:
        print(c, end=' ')
    else:
        print('0')
