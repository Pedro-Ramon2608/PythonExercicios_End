vcasa = float(input('Qual é o valor da casa? R$'))
sal = float(input('Qual é o valor do seu salário? R$'))
anos = int(input('Em quantos anos vc deseja pagar? '))
prestacao = vcasa / (anos * 12)
if prestacao > (30 * sal / 100):
    print('\033[91mSeu emprestimo foi \033[1;4mNegado.\033[m')
else:
    print('\033[97mSeu empréstimo foi \033[1;4mAprovado!\033[m')