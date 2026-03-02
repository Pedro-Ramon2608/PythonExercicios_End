n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite o valor da razão da PA: '))
for c in range(1, 11):
    print(n1, end=' > ')
    n1 = n1 + r
print('FIM')