num = []
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    if c == 0 or n > num[-1]:
        num.append(n)
        print('Adicionado ao final da lista')
    else:
        if n < num[0]:
            num.insert(0, n)
            print(f'Adicionado na posição {num.index(n)} da lista')
        elif n > num[0] and n < num[1]:
            num.insert(1, n)
            print(f'Adicionado na pósição {num.index(n)} da lista')
        elif n > num[1] and n < num[2]:
            num.insert(2, n)
            print(f'Adicionado na posição {num.index(n)} da lista')
        elif n > num[2] and n < num[3]:
            num.insert(3, n)
            print(f'Adicionado na posição {num.index(n)} da lista')
print('=-' * 20)
print(f'Os valores digitados em ordem foram {num}')
