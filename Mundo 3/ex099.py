from time import sleep
def maior(* num):
    maior = 0
    print('-=' * 30)
    print('Analisando os valores passados...')
    for c in range(0, len(num)):
        print(f'{num[c]} ', end='')
        sleep(0.25)
        if c == 0:
            maior = num[c]
        elif num[c] > maior:
            maior = num[c]
    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {maior}.')


maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
