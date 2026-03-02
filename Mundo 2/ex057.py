sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
while sexo != 'M' and sexo != 'F':
    print('-' * 32)
    print('Sexo Inválido! Tente Novamente.')
    print('-' * 32)
    sexo = str(input('Digite seu sexo: [M/F] ')).strip().upper()[0]
print('Sexo registrado com sucesso!')
