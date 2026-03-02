pes18 = homens = mul20 = 0
while True:
    print('-' * 30)
    print('{:^30}'.format('CADASTRE UMA PESSOA'))
    print('-' * 30)
    idade = int(input('Idade: '))
    if idade >= 18:
        pes18 += 1
    sexo = ' '
    while sexo not in 'MF':
        sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]
    if sexo == 'M':
        homens += 1
    if sexo == 'F' and idade < 20:
        mul20 += 1
    print('-' * 30)
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('-' * 30)
print (f'Total de pessoas com mais de 18 anos: {pes18}')
print(f'Ao todo temos {homens} homens cadastrados.')
print(f'E temos {mul20} mulheres com menos de 20 anos.')
