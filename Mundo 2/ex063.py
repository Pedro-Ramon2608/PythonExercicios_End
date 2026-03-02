num = int(input('Digite quatos elementos de Fibonacci você quer ver: '))
a = 0
b = 1
print('{} -> {}'.format(a, b), end='')
cont = 3
while cont <= num:
    c = a + b
    print(' -> {}'.format(c), end='')
    a = b
    b = c
    cont += 1
print(' -> FIM')