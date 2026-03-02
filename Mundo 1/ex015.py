d = int(input('Quantos dias você ficou com o carro? '))
km = float(input('Quantos Km rodados? '))
p = (d*60) + (km*0.15)
print('O valor a se pagar é R${}'.format(p))
