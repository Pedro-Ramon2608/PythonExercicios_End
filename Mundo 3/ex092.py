from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: '))
nasc = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - nasc
dados['ctps'] = int(input('Carteira de Trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratação'] = int(input('Ano de contratação: '))
    anotrabalho = date.today().year - dados['contratação'] #quantos anos de trabalho
    apos = 35 - anotrabalho #tempo restante até a aposentadoria
    dados['salário'] = float(input('Salário: R$'))
    dados['aposentadoria'] = apos + dados['idade']  # idade de aposentadoria

print('-='*20)
for k, v in dados.items():
    print(f' - {k} tem o valor {v}')
