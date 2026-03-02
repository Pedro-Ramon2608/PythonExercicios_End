num = int(input('Digite um numero inteiro: '))
if num % 2 == 0:
    print('\033[97mO numero {} é \033[4;1;36mPAR\033[m'.format(num))
else:
    print('\033[97mO numero {} é \033[1;4;35mIMPAR\033[m'.format(num))
