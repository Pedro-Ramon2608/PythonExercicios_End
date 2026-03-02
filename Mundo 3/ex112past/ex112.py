from utilidades_CeV import moeda
from utilidades_CeV import dado

p = dado.leiaDinheiro('Digite um preço: R$')
moeda.resumo(p, 80, 35)
