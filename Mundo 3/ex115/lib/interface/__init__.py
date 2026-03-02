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


def cor(cores=0):
    tab = (
        '\033[m', #limpa cor - 0
        '\033[1;91m', #red - 1
        '\033[1;92m', #green - 2
        '\033[1;93m', #yellow - 3
        '\033[1;94m', #blue - 4
        '\033[1;95m', #purple - 5
        '\033[1;96m', #cyan - 6
        '\033[1;97m', #white - 7
    )
    return tab[cores]

def lin(tam=40):
    return  f'{cor(7)}-' * tam

def cabeçalho(txt):
    print(lin())
    print(txt.center(40))
    print(lin(), cor())


def menu(lista):
    cabeçalho('MENU PRINCIPAL')
    c = 1
    for item in lista:
        print(f'{cor(3)}{c} {cor(7)}- {cor(4)}{item}')
        c += 1
    print(lin())
    opc = leiaInt(f'{cor(3)}Sua opção: ')
    return opc
