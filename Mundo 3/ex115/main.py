from lib.arquivo import *
from lib.interface import *
from time import sleep

arq = 'cadastros.txt'

if not arquivoexiste(arq):
    criar_arquivo(arq)

while True:
    resp = menu(['Ver Lista de Cadastro', 'Cadastrar Pessoa', 'Sair do Sistema'])
    if resp == 1:
        sleep(1)
        #Opção para listar os dados de um arquivo
        ler_arquivo(arq)
    elif resp == 2:
        sleep(1)
        #Opção para cadastro de uma nova pessoa
        cabeçalho('CADASTRO DE NOVA PESSOA')
        nome = str(input('Nome: ')).strip()
        idade = leiaInt('Idade: ')
        cadastrar(arq, nome, idade)
    elif resp == 3:
        cabeçalho(f'{cor(2)}     Saindo do Sistema... Até Logo!')
        sleep(1)
        break
    else:
        print(f'{cor(1)}ERRO! Digite uma opção válida!')
    sleep(1)
