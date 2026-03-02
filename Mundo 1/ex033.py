n1 = int(input('Digite o primeiro valor: '))
n2 = int(input('Digite o segundo valor: '))
n3 = int(input('Digite o terceiro valor: '))
maior = n1
menor = n1
if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3
print('O \033[4mMaior\033[m valor digitado foi \033[1;31m{}\033[m'.format(maior))
print('O \033[4mMenor\033[m valor digiotado foi \033[1;34m{}\033[m'.format(menor))
