from datetime import date
totmenor = 0
totmaior = 0
for c in range(1, 8):
    anonasc = int(input('Digite o ano de nascimento da {}° pessoa: '.format(c)))
    idade = date.today().year - anonasc
    if idade < 18:
        totmenor = totmenor + 1
    else:
        totmaior = totmaior + 1
print('No total há {} pessoas maior de idade e {} pessoas menor de idade'.format(totmaior, totmenor))