from random import randint

print('=-' * 20)
print('VAMOS JOGAR PAR OU ÍMPAR')
print('=-' * 20)
vitorias = 0
while True:
    num = int(input('Diga um Valor: '))
    comp = randint(0, 10)
    PouI = str(input('Par ou Ímpar? [P/I] ')).strip().upper()[0]
    soma = num + comp
    if soma % 2 == 0:
        print('-' * 48)
        print(f'Você jogou {num} e o computador {comp}. Total de {soma} DEU PAR')
        print('-' * 48)
        if PouI == 'P':
            print('Você VENCEU! \nVamos jogar novamente...')
            print('=-' * 20)
            vitorias += 1
        elif PouI == 'I':
            print('Você PERDEU!')
            break
    if soma % 2 != 0:
        print('-' * 48)
        print(f'Você jogou {num} e o computador {comp}. Total de {soma} DEU ÍMPAR')
        print('-' * 48)
        if PouI == 'I':
            print('Você VENCEU! \nVamos jogar novamente...')
            print('=-' * 20)
            vitorias += 1
        elif PouI == 'P':
            print('Você PERDEU!')
            break
print('=-' * 20)
print(f'GAME OVER! Você venceu {vitorias} vezes.')
