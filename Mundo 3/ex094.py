lista = list()
dados = dict()
media = soma = 0
while True:
    dados['nome'] = str(input('Nome: '))
    dados['sexo'] = ' '
    while dados['sexo'] not in 'FM':
        dados['sexo'] = str(input('Sexo: [M/F] ')).strip().upper()[0]
    dados['idade'] = int(input('Idade: '))
    soma += dados['idade']
    lista.append(dados.copy())
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

print('-='*30)
print(f'- O grupo tem {len(lista)} pessoas.')
media = soma / len(lista)
print(f'- A média de idade é de {media:.2f} anos.')

print('- As mulheres cadastradas foram: ', end='')
for i, v in enumerate(lista):
    if lista[i]['sexo'] == 'F':
        print(f'{lista[i]["nome"]} ', end='')

print('\n- Lista de pessoas que estão acima da média de idade: ')
for i, v in enumerate(lista):
    if v['idade'] > media:
        print()
        print(f'nome = {lista[i]["nome"]}; sexo = {lista[i]["sexo"]}; idade = {lista[i]["idade"]}')
print('<< ENCERRADO >>')
