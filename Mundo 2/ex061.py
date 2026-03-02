n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 10
while cont != 0:
    print(n1, end=' > ')
    n1 += r
    cont -= 1
print('FIM')
