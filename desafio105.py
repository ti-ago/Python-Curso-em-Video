from curses import keyname
from multiprocessing.sharedctypes import Value


def notas(*notas,situação='esconder'):
    """
    >>>Função para analisar notas de vários alunos de uma mesma turma.
    *notas => notas dos alunos separadas por vírgula, ponto como casa decimal.
    situação => 'esconder' é o valor padrão, para mostrar colocar *** situação='mostrar' ***.
    
    """
    global turma
    turma = {}
    totalNotas = 0
    maiorNota = 0
    menorNota = 0
    mediaTurma = 0
    for nota in notas:
        totalNotas += 1
        if totalNotas == 1:
            maiorNota = menorNota = soma = nota
        else:
            if nota > maiorNota:
                maiorNota = nota
            elif nota < menorNota:
                menorNota = nota
            soma += nota
    mediaTurma = soma / totalNotas
    turma["total de notas"] = totalNotas
    turma["maior nota"] = maiorNota
    turma["menor nota"] = menorNota
    turma["média da turma"] = mediaTurma
    if situação == 'mostrar':
        if mediaTurma >= 9:
            turma['situação'] = 'excelente'
        elif mediaTurma >= 7:
            turma['situação'] = 'boa'
        elif mediaTurma >= 5:
            turma['situação'] = 'razoável'
        else:
            turma['situação'] = 'ruim'
    
    return turma

print(notas(9,8,10,4,9,6,7,8,situação='mostrar'))

