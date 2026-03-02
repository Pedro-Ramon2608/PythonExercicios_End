frase = str(input('Digite uma frase: ')).strip()
print('A frase {} apareceu '.format(frase), frase.upper().count('A'), ' a letra A.')
print('A primeira vez que a letra A aparece é na posição: ', frase.upper().find('A')+1)
print('A ultima vez que a letra A aparece é na posição: ', frase.upper().rfind('A')+1)