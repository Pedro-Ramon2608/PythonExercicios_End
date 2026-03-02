n = int(input('Digite o número de qual tabuada quer ver: '))
i = int(input('Em qual número você deseja que ela inicie? '))
f = int(input('Qual número você deseja que ela termine? '))
for c in range(i, f+1):
    print('{} x {} = {}'.format(n, c, n * c))