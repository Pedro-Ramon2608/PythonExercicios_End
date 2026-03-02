from datetime import date
ano = int(input('\033[97mDigite o ano de nascimento: '))
idade = date.today().year - ano
if idade < 18:
    print('\033[1;7;97mVocê ainda irá se alistar!\033[m')
    print('\033[1;7;97mFalta(m) {} ano(s) para você se alistar!\033[m'.format(18 - idade))
elif idade == 18:
    print('\033[1;7;97mJá é a hora de fazer o alistamento militar!\033[m')
else:
    print('\033[7;1;97mJá passou o tempo do alistamento militar!\033[m')
    print('\033[1;7;97mJá se passou/passaram {} ano(s) do alistamento militar!\033[m'.format(idade - 18))