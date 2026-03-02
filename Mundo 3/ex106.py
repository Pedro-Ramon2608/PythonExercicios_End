from time import sleep

c = ('\033[m', # 0 - sem cor
     '\033[0;97;41m', # 1 - vermelho
     '\033[0;97;42m', # 2 - verde
     '\033[0;97;43m', # 3 - amarelo
     '\033[0;97;44m', # 4 - azul
     '\033[0;97;45m', # 5 - roxo
     '\033[7;97m', # 6 - branco
     )


def PyHelp(msg):
    titulo(f'Acessando o manual do comando \'{msg}\'', 4)
    sleep(1.5)
    print(c[6], end='')
    help(msg)
    print(c[0], end='')


def titulo(msg, cor=0):
    tam = len(msg) + 2
    print(c[cor], end='')
    print('-' * tam)
    print(f'{msg}')
    print('-' * tam)
    print(c[0], end='')
    sleep(1)


r = ''
while True:
    titulo('  SISTEMA DE AJUDA PYTHON', 5)
    r = str(input('Função ou Biblioteca > '))
    if r.lower() == 'fim':
        break
    else:
        PyHelp(r)
titulo('  ATÉ LOGO!', 1)
