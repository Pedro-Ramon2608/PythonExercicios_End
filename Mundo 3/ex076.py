print('-'*30)
print(f'{'Lista de Produtos':^30}')
print('-'*30)
lista = ('Pão Frances', 0.50, 'Pão de Leite', 0.50, 'Leite', 6, 'Pão de Coco', 1, 'Sonho', 3, 'Coxinha', 2.50, 'Café', 4)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f'{lista[pos]:.<23}', end='')
    else:
        print(f'R$ {lista[pos]:.2f}')
print('-'*30)
