from time import sleep
def contador(i, f, p):
    print('-='*20)
    if p == 0:
        p = 1
    if p < 0:
        p *= -1
    print(f'Contagem de {i} até {f} de {p} em {p}')
    if i > f:
        p *= -1
        for c in range(i, f-1, p):
            print(c, end=' ')
            sleep(0.25)
    else:
        for c in range(i, f+1, p):
            print(c, end=' ')
            sleep(0.25)
    print('FIM!')


contador(1, 10, 1)
contador(10, 0, 2)
print('Agora é a sua vez de personalizar a contagem!')
inicio = int(input('Início: '))
fim = int(input('Fim: '))
passo = int(input('Passo: '))
contador(inicio, fim, passo)
