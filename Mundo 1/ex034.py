sal = float(input('Digite o valor do seu salário: R$'))
if sal > 1250:
    n1 = sal + (sal * 10 / 100)
else:
    n1 = sal + (sal * 15 / 100)
print('\033[97mSeu salário atualizado é de \033[1;32mR${:.2f}\033[m'.format(n1))