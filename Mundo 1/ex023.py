num = int(input('Digite um numero de 0 a 9999: '))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print('Analisando o numero \033[97m{}\033[m'.format(num))
print('Unidade: \033[34m{}\033[m'.format(u))
print('Dezena: \033[31m{}\033[m'.format(d))
print('Centena: \033[32m{}\033[m'.format(c))
print('Milhar: \033[35m{}\033[m'.format(m))