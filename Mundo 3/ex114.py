import urllib.error
import urllib.request

try:
    site = urllib.request.urlopen('https://pudim.com')
except urllib.error.URLError:
    print('\033[1;91mO site Pudim não está acessível no momento.\033[m')
except Exception as erro:
    print('Erro:', erro)
else:
    print('\033[1;92mConsegui acessar o site Pudim com sucesso!\033[m')
