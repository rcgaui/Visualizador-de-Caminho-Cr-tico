import numpy as np
from exibicao import *
from leituradados import *

def buscaTarefa (dados, tarefa):
    x = 0
    flag = 0
    for i in dados['Tarefa']:
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
    ES = [0] * numTarefas
    EF = [0] * numTarefas
    temp = []
    for i in range(numTarefas):
        if (dados['Predecessor'][i] == None):
            ES[i] = 0
            EF[i] = ES[i] + dados['Duracao'][i]
        else:
            for j in dados['Predecessor'][i]:
                index = buscaTarefa(dados, j)
                if(index != None):
                    temp.append(EF[index])
                else:
                    temp.append(0)          
            if(temp!=None):
                ES[i] = max(temp)
            EF[i] = ES[i] + dados['Duracao'][i]
        temp = []
    dados['ES'] = ES
    dados['EF'] = EF

    return dados

def caminhoDeVolta (dados):
    numTarefas = dados.shape[0]
    LS = [0] * numTarefas
    LF = [0] * numTarefas
    temp = []
    for i in range(numTarefas -1, -1, -1):
        if (dados['Sucessor'][i] == None):
            LF[i] = np.max(dados['EF'])
            LS[i] = LF[i] - dados['Duracao'][i]
        else:
            for j in dados['Sucessor'][i]:
                index = buscaTarefa(dados, j)
                if(index!=None):
                    temp.append(LS[index])
                else:
                    temp.append(0)
            if(temp!=[]):
                LF[i] = min(temp)     
                LS[i] = LF[i] - dados['Duracao'][i]
            temp = []
    dados['LS'] = LS
    dados['LF'] = LF

    return dados

def calculaFolga(dados):
    numTarefas = dados.shape[0]
    FOLGA = np.zeros(shape=numTarefas, dtype=np.int8)
    for i in range(numTarefas):
        FOLGA[i] = dados['LS'][i] - dados['ES'][i]
    dados['Folga'] = FOLGA
    return dados

def calculaCPM(dados):
    dados = caminhoDeIda(dados)
    dados = caminhoDeVolta(dados)
    dados = calculaFolga(dados)
    return dados

def cpm(arquivo):
    df = LerArquivoCSV(arquivo)
    dados = calculaCPM(df)
    indexFolgaZero = np.where(dados['Folga'] == 0)[0]
    tarefasCpm = np.array(dados['Tarefa'][indexFolgaZero], dtype=np.str_)
    exibirCaminhoCritico(tarefasCpm)