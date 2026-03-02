num1 = int(input('Digite o primeiro valor: '))
num2 = int(input('Digite o segundo valor: '))
n = 0
while n != 5:
    print('\033[97;1m-=\033[m' * 30)
    print('''[ 1 ] SOMAR
[ 2 ] MULTIPLICAR
[ 3 ] MAIOR
[ 4 ] NOVOS NÚMEROS
[ 5 ] SAIR DO PROGRAMA''')
    n = int(input('Selecione a opção desejada: '))
    print('\033[97;1m-=\033[m' * 30)
    if n == 1:
        soma = num1 + num2
        print('O resultado da soma entre {} e {} foi {}'.format(num1, num2, soma))
    elif n == 2:
        mult = num1 * num2
        print('O resultado da multiplicação entre {} e {} foi {}'.format(num1, num2, mult))
    elif n == 3:
        if num1 > num2:
            print('O maior número foi {}, que foi o primeiro valor digitado.'.format(num1))
        else:
            print('O maior número foi {}, que foi o segundo valor digitado.'.format(num2))
    elif n == 4:
        num1 = int(input('Digite o primeiro valor: '))
        num2 = int(input('Digite o segundo valor: '))
print('Fim do Programa.')
