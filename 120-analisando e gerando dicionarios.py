# Faça um programa que tenha uma função notas() que pode receber várias notas de alunos 
# e vai retornar um dicionário com as seguintes informações:
# Quantidade de notas
# A maior nota
# A menor nota
# A média da turma
# A situação (opcional) abaixo de 5 = reprovado/entre 5 e 7 = recuperação/acima de 7 = aprovado
# Adicione também as docstrings dessa função para consulta pelo desenvolvedor.

def notas(*n, situacao=False):
    """
    n = receber um numero indefinido de notas
    situacao(opcional) = se True mostra a situação abaixo de 5 = reprovado/entre 5 e 7 = recuperação/acima de 7 = aprovado 
    return = retorna o dicionário preenchido
    """
    dici = dict()
    dici['Quantidade: '] = len(n)
    dici['Maior nota: '] = max(n)
    dici['Menor nota: '] = min(n)
    dici['Média: '] = sum(n)/len(n)
    if situacao:
        if dici['Média: '] < 5:
            dici['Situação: '] = 'Reprovado'
        elif dici['Média: '] > 7:
            dici['Situação: '] = 'Aprovado'
        else:
            dici['Situação: '] = 'Recuperação'
    return dici


# help(notas)
r = notas(2.4, 8.9, 5.2, situacao=True)
print (r)
