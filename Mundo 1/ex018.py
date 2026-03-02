import math
ang = float(input('Digite o valor do ângulo: '))
sen = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tan = math.tan(math.radians(ang))
print('O valor do seno é {:.2f}\nO valor do cosseno é {:.2f}\nO valor da tangente é {:.2f}'.format(sen, cos, tan))