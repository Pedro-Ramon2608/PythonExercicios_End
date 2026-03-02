import math
co = float(input('Digite o cateto oposto: '))
ca = float(input('Digite o cateto adjacente: '))
hip = math.hypot(co, ca)
print('A hipotenusa do triângulo retângulo vale {:.2f}'.format(hip))
