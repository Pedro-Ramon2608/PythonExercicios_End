dados = dict()
dados['nome'] = str(input('Nome: '))
dados['media'] = float(input(f'Média de {dados["nome"]}: '))
if dados['media'] >= 7:
    dados['situacao'] = 'Aprovado'
elif  5 <= dados['media'] < 7:
    dados['situacao'] = 'Recuperação'
else:
    dados['situacao'] = 'Reprovado'
print('-'*30)
print(f'Nome: {dados["nome"]}')
print(f'Média: {dados["media"]}')
print(f'Situação: {dados["situacao"]}')
print('-'*30)
