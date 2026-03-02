from random import randint
from time import sleep
print('\033[96;1m-=-\033[m' * 20)
print('\033[97;1mVamos Jogar Pedra, Papel e Tesoura e ver quem ganha!\033[m')
print('\033[96;1m-=-\033[m' * 20)
print('\033[91;1m[ 1 ] Pedra \033[m\n\033[97;1m[ 2 ] Papel \033[m\n\033[94;1m[ 3 ] Tesoura \033[m')
ppt = int(input('\033[97mDigite sua opção: '))
print('\033[96;1m-=-\033[m' * 20)
print('\033[97;7;1mJO\033[m')
sleep(1)
print('\033[97;7;1mKEN\033[m')
sleep(1)
print('\033[97;7;1mPÔ!!!\033[m')
sleep(1)
comp = randint(1, 3)
print('\033[96;1m-=-\033[m' * 10)

if ppt == 1: #se o jogador jogar Pedra
    if comp == 1:
        print('''\033[95;1mComputador Jogou: \033[91;1mPEDRA\033[m
\033[92;1mJogador Jogou: \033[91;1mPEDRA\033[m''')
        print('\033[96;1m-=-\033[m' * 10)
        print('\033[97;1mDeu EMPATE!\033[m')
    elif comp == 2:
        print('''\033[95;1mComputador Jogou: \033[97;1mPAPEL
\033[92;1mJogador Jogou: \033[91;1mPEDRA''')
        print('\033[96;1m-=-\033[m' * 10)
        print('\033[95;1mComputador VENCEU! Tente Novamente!\033[m')
    elif comp == 3:
        print('''\033[95;1mComputador Jogou: \033[94;1mTESOURA
\033[92;1mJogador Jogou: \033[91;1mPEDRA''')
        print('\033[96;1m-=-\033[m' * 10)
        print('\033[92;1mVOCÊ VENCEU!\033[m')

elif ppt == 2: #se o jogador jogar Papel
    if comp == 1:
        print('''\033[95;1mComputador Jogou: \033[91;1mPEDRA
\033[92;1Jogador Jogou: \033[97;1mPAPEL''')
        print('\033[96;1m-=-\033[m' * 10)
        print('\033[92;1mVOCÊ VENCEU!\033[m')
    elif comp == 2:
        print('''\033[95;1mComputador Jogou: \033[97;1mPAPEL
\033[92;1mJogador Jogou: \033[97;1mPAPEL''')
        print('\033[96;1m-=-\033[m' * 10)
        print('\033[97;1mDeu EMPATE!\033[m')
    elif comp == 3:
        print('''\033[95;1mComputador Jogou: \033[94;1mTESOURA
\033[92;1mJogador Jogou: \033[97;1mPAPEL''')
        print('\033[96;1m-=-\033[m' * 10)
        print('\033[95;1mComputador VENCEU! Tente Novamente!\033[m')

elif ppt == 3: #se o jogador jogar Tesoura
    if comp == 1:
        print('''\033[95;1mComputador Jogou: \033[91;1mPEDRA
\033[92;1mJogador Jogou: \033[94;1mTESOURA''')
        print('\033[96;1m-=-\033[m' * 10)
        print('\033[95;1mComputador VENCEU! Tente Novamente!\033[m')
    elif comp == 2:
        print('''\033[95;1mComputador Jogou: \033[97;1mPAPEL
\033[92;1mJogador Jogou: \033[94;1mTESOURA''')
        print('\033[96;1m-=-\033[m' * 10)
        print('\033[92;1mVOCÊ VENCEU!\033[m')
    elif comp == 3:
        print('''\033[95;1mComputador Jogou: \033[94;1mTESOURA
\033[92;1mJogador Jogou: \033[94;1mTESOURA''')
        print('\033[96;1m-=-\033[m' * 10)
        print('\033[97;1mDeu EMPATE!\033[m')
else:
    print('\033[93;1mOpção Invalida. Tente novamente.\033[m')