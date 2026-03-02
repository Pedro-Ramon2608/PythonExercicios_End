def leiaDinheiro(msg):
    valido = False
    while not valido:
        entrada = str(input(msg)).replace(',', '.').strip()
        if entrada.isalpha() or entrada == '':
            print(f'\033[91;1mERRO: \"{msg}\" é um preço inválido!\033[m')
        else:
            valido = True
            return float(entrada)


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
