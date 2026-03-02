dis = int(input('Qual será a distância percorrida? '))
if dis <= 200:
    Km = dis * 0.50
else:
    Km = dis * 0.45
print('\033[34mO valor total a ser pago pela viagem de {}Km, é de \033[m\033[32mR${:.2f}\033[m'.format(dis, Km))
