nome = str(input('Digite o nome de uma cidade: '))
div = nome.split()
print('A cidade digitada possui \033[1;7;4;97;40mSANTO\033[m na primeira palavra dela: ', 'SANTO' in div[0].upper())