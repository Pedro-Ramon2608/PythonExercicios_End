somaidade = 0 #soma todas as idades
hmaisv = 0 #homem mais velho
nomev = '' #nome do homem mais velho
totm = 0 #número total de mulheres menores de 20 anos
for c in range(1, 5):
    nome = str(input('Digite o nome da {}° pessoa: '.format(c))).strip()
    idade = int(input('Digite a idade da {}° pessoa: '.format(c)))
    sexo = str(input('Digite o sexo da {}° pessoa: [M/F] '.format(c))).strip()
    if sexo in 'Mm' and c == 1:
        hmaisv = idade
        nomev = nome
    elif idade > hmaisv:
        hmaisv = idade
        nomev = nome
    if sexo in 'Ff' and idade < 20:
        totm = totm + 1 #total de mulheres menores de 20 anos.
    print('-' * 30)
    somaidade += idade
media = somaidade / 4
print('A média de idade do grupo é {}'.format(media))
print('O nome do homem mais velho é {} com {} anos de idade.'.format(nomev, hmaisv))
print('O número de mulheres que possuem menos de 20 anos de idade é {}'.format(totm))
