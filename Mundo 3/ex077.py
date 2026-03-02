palavras = ('aprender', 'programar', 'linguagem', 'python',
            'chamada', 'dinossauro', 'leao', 'baleia', 'anao',
            'humano', 'estudar', 'cebola', 'agua', 'fogo')
for p in palavras:
    print(f'\nNa palavra {p.upper()} temos ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')
