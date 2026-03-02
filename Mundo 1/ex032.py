ano = int(input('Qual é o ano atual ou algum outro ano? '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano {} É um ano Bissexto.'.format(ano))
else:
    print('O ano {} \033[4;1;97mNÃO\033[m é um ano Bissexto!'.format(ano))
