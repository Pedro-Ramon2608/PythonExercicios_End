while True:
    print('=' * 45)
    num = int(input('Você deseja ver a tabuada de qual número? '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f' {num} x {c} = {num * c}')
print('PROGRAMA TABUADA ENCERRADO. Volte Sempre!')