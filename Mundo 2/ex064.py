print('Digite 999 para parar')
num = soma = totnum = 0
while num != 999:
    num = int(input('Digite um valor: '))
    if num != 999:
        totnum += 1
        soma = soma + num
print('Você digitou no total {} números e a soma entre eles foi {}'.format(totnum, soma))
