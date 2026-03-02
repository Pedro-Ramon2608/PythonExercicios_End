a = float(input('Digite a primeira reta do Triângulo: '))
b = float(input('Digite a segunda reta: '))
c = float(input('Digite a terceira reta: '))
cor = {
    'limpa':'\033[m',
    'red':'\033[1;31m',
    'blue':'\033[1;34m',
    'yellow':'\033[1;33m'
}
if a + b > c and a + c > b and b + c > a:
    print('As retas {}{}{}, {}{}{} e {}{}{} formam um triângulo.'.format(cor['red'], a, cor['limpa'], cor['blue'], b, cor['limpa'], cor['yellow'], c, cor['limpa']))
else:
    print('As retas {}{}{}, {}{}{} e {}{}{} NÃO formam um triângulo.'.format(cor['red'], a, cor['limpa'], cor['blue'], b, cor['limpa'], cor['yellow'], c, cor['limpa']))
