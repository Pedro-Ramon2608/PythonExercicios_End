totnum = 0
soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    totnum += 1
    soma += num
print(f'Foram digitados {totnum} números e a soma entre eles é {soma}')
