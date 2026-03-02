sair = ''
soma = totnum = numaior = numenor = quant = 0
while sair != 'N':
    num = int(input('Digite um número: '))
    sair = str(input('Você quer continuar? [S/N] ')).strip().upper()[0]
    soma += num
    totnum += 1
    quant += 1
    if quant == 1:
        numaior = numenor = num
    else:
        if num > numaior:
            numaior = num
        if num < numenor:
            numenor = num
media = soma / totnum
print('A média de todos os valores digitados foi {:.2f}'.format(media))
print('O MAIOR número digitado foi {}'.format(numaior))
print('O MENOR número digitado foi {}'.format(numenor))
