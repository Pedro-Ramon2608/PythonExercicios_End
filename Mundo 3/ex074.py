from random import randint
print('Os números sorteados foram: ', end='')
'''for c in range(0, 5):
    numeros = randint(0, 10)
    print(f'{numeros}', end=' ')
    if c == 0:
        maior = numeros
        menor = numeros
    else:
        if numeros > maior:
            maior = numeros
        elif numeros < menor:
            menor = numeros
print(f'\nO maior número sorteado foi {maior}')
print(f'O menor número sorteado foi {menor}')'''

#Ou se resolve dessa forma:

numeros = (randint(0, 10), randint(0, 10), randint(0, 10), randint(0, 10))
for n in numeros:
    print(f'{n} ', end='')
print(f'\nO maior número sorteado foi {max(numeros)}')
print(f'O menor número sorteado foi {min(numeros)}')
