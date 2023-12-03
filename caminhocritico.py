import numpy as np

def buscaTarefa (dados, tarefa):
    x = 0
    flag = 0
    for i in dados['TAREFA']:
        if (i == tarefa):
            flag = 1
            break
        x += 1
    if (flag == 1):
        return x
    else:
        print ('Erro na inserção de tarefa')


def caminhoDeIda (dados):
    numTarefas = dados.shape[0]
    ES = np.zeros(numTarefas, dtype=np.int8)
    EF = np.zeros(numTarefas, dtype=np.int8)
    temp = []
    for i in range(numTarefas):
        if (dados['PREDECESSOR'][i] == None):
            ES[i] = 0
            EF[i] = ES[i] + dados['DURACAO'][i]
        else:
            for j in dados['PREDECESSOR'][i]:
                index = buscaTarefa(dados, j)
                temp.append(EF[index])
            ES[i] = max(temp)
            EF[i] = ES[i] + dados['DURACAO'][i]
        temp = []
    dados['ES'] = ES
    dados['EF'] = EF

    return dados

def caminhoDeVolta (dados):
    numTarefas = dados.shape[0]
    LS = np.zeros(numTarefas, dtype=np.int8)
    LF = np.zeros(numTarefas, dtype=np.int8)
    temp = []
    for i in range(numTarefas -1, -1, -1):
        if (dados['SUCESSOR'][i] == None):
            LF[i] = np.max(dados['EF'])
            LS[i] = LF[i] - dados['DURACAO'][i]
        else:
            for j in dados['SUCESSOR'][i]:
                index = buscaTarefa(dados, j)
                temp.append(LS[index])
            LF[i] = min(temp)
            LS[i] = LF[i] - dados['DURACAO'][i]
            temp = []
    dados['LS'] = LS
    dados['LF'] = LF

    return dados

def calculaFolga(dados):
    numTarefas = dados.shape[0]
    FOLGA = np.zeros(shape=numTarefas, dtype=np.int8)
    for i in range(numTarefas):
        FOLGA[i] = dados['LS'][i] - dados['ES'][i]
    dados['FOLGA'] = FOLGA
    return dados

def calculaCPM(dados):
    dados = caminhoDeIda(dados)
    dados = caminhoDeVolta(dados)
    dados = calculaFolga(dados)
    return dados

def cpm(dados):
    dados = calculaCPM(dados)
    indexFolgaZero = np.where(dados['FOLGA'] == 0)[0]
    tarefasCpm = np.array(dados['TAREFA'][indexFolgaZero], dtype=np.str_)
    return tarefasCpm