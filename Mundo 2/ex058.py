from random import randint
comp = randint(0, 10)
num = -1
tottentativas = 0
while num != comp:
    print('-' * 60)
    num = int(input('Tente advinhar em qual número estou pensando entre 0 e 10: '))
    print('-' * 60)
    tottentativas += 1
    if num < comp:
        print('Você errou! Tente novamente um \033[4mpouco mais...\033[m')
    elif num > comp:
        print('Você errou! Tente novamente um \033[4mpouco menos...\033[m')
print('Parabéns Você Acertou!!!')
print('O número de tentativas que você teve até acertar foram {} tentativas.'.format(tottentativas))
