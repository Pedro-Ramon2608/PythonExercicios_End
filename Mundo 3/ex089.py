lista = []
dados = []
while True:
    media = 0
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Nota 1: ')))
    dados.append(float(input('Nota 2: ')))
    media += (dados[1] + dados[2]) / 2
    dados.append(media)
    lista.append(dados[:])
    dados.clear()
    resp = ' '
    while resp not in 'SN':
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if resp in 'N':
        break

print('-=' * 20)
print(f'N° {'NOME':<15} {'MÉDIA':<6}')
print('-' * 30)
for c in range(0, len(lista)):
    print(f'{c}  {lista[c][0]:<15} {lista[c][3]:^6.1f}')
print('-' * 30)
while True:
    mostrar = int(input('Quer ver as notas de qual aluno? (999 interrompe)'))
    if mostrar <= len(lista):
        print(f'Notas de {lista[mostrar][0]} são [{lista[mostrar][1]}, {lista[mostrar][2]}]')
        print('-' * 40)
    if mostrar == 999:
        break
