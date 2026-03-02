peso = float(input('Quantos Kg você possui? '))
altura = float(input('Qual é a sua altura em metros? '))
imc = peso / (altura ** 2)
if imc < 18.5:
    print('Você possui IMC igual a {:.2f}, e isso te classica como \033[93;1mAbaixo do Peso\033[m.'.format(imc))
elif imc >= 18.5 and imc <= 25:
    print('Seu IMC é de {:.2f}, e é classificado como \033[92;1mPeso Ideal\033[m.'.format(imc))
elif imc >= 25 and imc <= 30:
    print('Seu IMC é de {:.2f}, e é classificado como \033[94;1mSobrepeso\033[m.'.format(imc))
elif imc >= 30 and imc <= 40:
    print('Seu IMC é de {:.2f}, e é classificado como \033[95;1mObesidade\033[m.'.format(imc))
elif imc > 40:
    print('Seu IMC é de {:.2f}, e é classificado como \033[91;1;4mObesidade Mórbida\033[m.'.format(imc))
