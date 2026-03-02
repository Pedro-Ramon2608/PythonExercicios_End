def leiaInt(num):
    num = input(num)
    while True:
        if num.isnumeric():
            return int(num)
        else:
            print('\033[1;91mERRO! Digite um número inteiro válido.\033[m')
            num = input('Digite um número: ')


n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')
