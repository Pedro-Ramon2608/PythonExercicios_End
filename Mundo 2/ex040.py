n1 = float(input('\033[97mDigite sua primeira nota: '))
n2 = float(input('\033[97mDigite sua segunda nota: '))
media = (n1 + n2) / 2
if media < 5:
    print('\033[91;1;4mREPROVADO!\033[m \n\033[97mPois sua média foi {}, ficando abaixo de 5.\033[m'.format(media))
elif media >= 5 and media <= 6.9:
    print('\033[93;1;4mRECUPERAÇÃO!\033[m \n\033[97mSua média foi {}, estando entre 5 e 6.9.\033[m'.format(media))
elif media >= 7:
    print('\033[92;1;4mAPROVADO!\033[m \n\033[97;1mParabéns, sua média foi {}, ficando acima de 7.\033[m'.format(media))