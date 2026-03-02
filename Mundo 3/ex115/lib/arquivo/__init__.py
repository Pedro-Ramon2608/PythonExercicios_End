from ..interface import *

def arquivoexiste(nome):
    try:
        arquivo = open(nome, 'r')
        arquivo.close()
    except FileNotFoundError:
        return False
    else:
        return True


def criar_arquivo(nome):
    try:
        arquivo = open(nome, 'w+')
        arquivo.close()
    except:
        print('\033[91;1mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[92;1mArquivo {nome} criado com sucesso!\033[m')


def ler_arquivo(nome):
    try:
        arquivo = open(nome, 'r')
    except:
        print('Não foi possível ler ou acessar o arquivo!')
    else:
        cabeçalho('PESSOAS CADASTRADAS')
        for linha in arquivo:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{cor(7)}{dado[0]:<30}{dado[1]:>2} anos')
    finally:
        arquivo.close()


def cadastrar(arq, nome='<desconhecido>', idade=0):
    try:
        arquivo = open(arq, 'a')
    except:
        print('Houve um erro na abertura do arquivo!')
    else:
        try:
            arquivo.write(f'{nome}; {idade}\n')
        except:
            print('Ocorreu um erro na hora de adicionar os dados.')
        else:
            print(f'{nome} foi adicionado(a) com sucesso!')
            arquivo.close()
