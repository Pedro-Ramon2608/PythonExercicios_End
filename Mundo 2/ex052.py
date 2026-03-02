num = int(input('Digite um número: '))
tot = 0
for c in range(1, num + 1):
    if num % c == 0:
        print('\033[91m', end=' ')
        tot += 1
    else:
        print('\033[96m', end=' ')
    print('{}'.format(c), end=' ')
if tot == 2:
    print('\n\033[mO número {} é um número PRIMO.'.format(num))
else:
    print('\n\033[mO número {} NÃO É PRIMO.'.format(num))
