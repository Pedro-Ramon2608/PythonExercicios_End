n1 = float(input('Digite um valor: '))
n2 = float(input('Digite outro valor: '))
s = n1 + n2
cores = {
    'limpa':'\033[m',
    'blue':'\033[34m',
    'red':'\033[31m',
    'white':'\033[1;97m'
}
print('A soma entre {}{}{} e {}{}{} vale {}{}{}'.format(cores['blue'], n1, cores['limpa'], cores['red'], n2, cores['limpa'], cores['white'], s, cores['limpa']))