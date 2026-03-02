n1 = int(input('\033[94mDigite o primeiro valor inteiro: \033[m'))
n2 = int(input('\033[91mDigite o segundo valor inteiro: \033[m'))
if n1 > n2:
    print('O primeiro valor \033[94m{}\033[m é maior que o segundo \033[91m{}\033[m.'.format(n1, n2))
elif n1 < n2:
    print('O segundo valor \033[91m{}\033[m é maior que o primeiro \033[94m{}\033[m.'.format(n2, n1))
else:
    print('\033[97mAmbos os valores são iguais!\033[m')