totcompra = p1000 = pmaisb = cont = 0
produtomb = '' #nome do produto mais barato
print('-' * 30)
print('{:^30}'.format(' Loja do Ninja '))
print('-' * 30)
while True:
    nome = str(input('Digite o nome do produto: ')).strip()
    preco = float(input('Preço: R$'))
    if preco > 1000:
        p1000 += 1
    totcompra += preco
    if cont == 0 or preco < pmaisb:
        produtomb = nome
        pmaisb = preco
    cont += 1
    continuar = ' '
    while continuar not in 'SN':
        continuar = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if continuar == 'N':
        break
print('{:-^30}'.format(' FIM DAS COMPRAS '))
print(f'O total da compra foi R${totcompra:.2f}')
print(f'Temos {p1000} produtos custando acima de R$1000.00')
print(f'O produto mais barato foi {produtomb} que custa R${pmaisb:.2f}')
