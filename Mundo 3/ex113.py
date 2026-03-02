def leiaInt(num):
    while True:
        try:
            entrada = int(input(num))
        except (ValueError, TypeError):
            print('\033[1;91mERRO! Digite um número Inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;91m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return entrada


def leiaFloat(num):
    while True:
        try:
            entrada = float(input(num))
        except (ValueError, TypeError):
            print('\033[1;91mERRO! Digite um número Real válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\033[1;91m\nUsuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return entrada


inteiro = leiaInt('Digite um número Inteiro: ')
real = leiaFloat('Digite um número Real: ')
print(f'O valor inteiro digitado foi {inteiro} e o real foi {real}')
