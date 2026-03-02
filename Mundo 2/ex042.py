a = float(input('Digite o primeiro lado do Triãngulo: '))
b = float(input('Digite o segundo lado: '))
c = float(input('Digite o terceiro lado: '))
if a + b > c and a + c > b and b + c > a:
    if a == b and b == c:
        print('Os lados {}, {} e {}, formam um Triângulo Equilatero.'.format(a, b, c))
    elif a == b or a == c or b == c:
        print('Os lados {}, {} e {}, formam um Triângulo Isósceles.'.format(a, b, c))
    elif a != b and a != c and b != c:
        print('Os lados {}, {} e {}, formam um Triângulo Escaleno.'.format(a, b, c))
else:
    print('Não é possivel formar um Triângulos com os lados digitados.')