def notas(* num, sit=False):
    """
    -> Função para notas e situações de aluno
    :param num: recebe uma ou mais notas, sem limite
    :param sit: valor opicional, indica se deve ou não ser adicionada a situação
    :return: retorna um dicionário com várias informações sobre o aluno
    """
    desempenho = dict()
    desempenho['total'] = len(num)
    desempenho['maior'] = max(num)
    desempenho['menor'] = min(num)
    desempenho['media'] =  sum(num) / len(num)
    if sit:
        if desempenho['media'] >= 7:
            desempenho['situação'] = 'BOA'
        elif desempenho['media'] >= 5:
            desempenho['situação'] = 'RAZOÁVEL'
        else:
            desempenho['situação'] = 'RUIM'
    else:
        pass
    print('-'*60)
    return desempenho


resp = notas(5.5, 3.8, 6.2, 8.3, 4.2)
print(resp)
