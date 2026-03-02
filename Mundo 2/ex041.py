from datetime import date
ano = int(input('Qual o ano de nascimento? '))
idade = date.today().year - ano
if idade <= 9:
    print('Você é um atleta \033[1;93mMirim\033[m.')
elif idade <= 14 and idade > 9:
    print('Você é um atleta \033[1;94mInfantil\033[m.')
elif idade > 14 and idade <= 19:
    print('Você é um atleta \033[1;95mJunior\033[m.')
elif idade > 19 and idade <= 20:
    print('Você é um atleta \033[1;33mSênior\033[m.')
elif idade > 20:
    print('Você é um atleta \033[1;91mMaster\033[m.')
