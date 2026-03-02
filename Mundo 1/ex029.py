velo = int(input('Qual a velocidade do seu carro? '))
if velo > 80:
    km = (velo - 80) * 7
    print('\033[33;1mVocê está {}Km/h acima da velocidade maxima permitida, entao sua multa é de\033[m \033[32;1mR${}.\033[m'.format(velo - 80, km))
else:
    print('Tudo Certo, dentro do limite de velocidade \033[97mpermitida!\033[m')
