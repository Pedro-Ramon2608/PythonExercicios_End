from random import randint
num = randint(0, 5)
esc = int(input('Digite um número entre 0 e 5 e veja se acertou: '))
if esc == num:
    print('\033[97mVOCÊ \033[4;1;97mACERTOU\033[m\033[97m, PARABENS!\033[m')
else:
    print('\033[31mVocê \033[4;31mERROU\033[m\033[31m, tente novamente!\033[m')