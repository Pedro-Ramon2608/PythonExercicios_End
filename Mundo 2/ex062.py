n1 = int(input('Digite o primeiro termo da PA: '))
r = int(input('Digite a razão da PA: '))
cont = 10
while cont != 0:
    print(n1, end=' > ')
    n1 += r
    cont -= 1
sorn = str(input('\nVocê deseja que apareça mais termos da PA? [S/N] ')).strip().upper()
if sorn == 'S':
    termos = int(input('Quantos termos você quer que apareçam mais? '))
    while termos != 0:
        print(n1, end=' > ')
        n1 += r
        termos -= 1
print('FIM')