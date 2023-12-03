import numpy as np

def buscaTarefa (dados, codigo):
    x = 0
    flag = 0
    for i in dados['Codigo']:
        if (i == codigo):
            flag = 1
            break
        x += 1
    if (flag == 1):
        return x
    else:
        print ('Erro na entrada do código')


def caminhoDeIda (dados):
    numTarefas = dados.shape[0]
    ES = np.zeros(numTarefas, dtype=np.int8)
    EF = np.zeros(numTarefas, dtype=np.int8)
    temp = []

    for i in range(numTarefas):
        if (dados['Predecessor'][i] == None):
            ES[i] = 0
            try:
                EF[i] = ES[i] + dados['Duracao'][i]
            except:
                print("Erro entrada da duração")
        else:
            for j in dados['Predecessor'][i]:
                index = buscaTarefa(dados, j)
                temp.append(EF[index])
                if(index == i):
                    print("Erro na entrada dos predecessores")
                else:
                    temp.append(EF[index])
            ES[i] = max(temp)
            try:
                EF[i] = ES[i] + dados['Duracao'][i]
            except:
                print("Erro entrada da duração")
        temp = []
    dados['ES'] = ES
    dados['EF'] = EF

    return dados

def caminhoDeVolta (dados):
    numTarefas = dados.shape[0]
    temp = []
    LS = np.zeros(numTarefas, dtype=np.int8)
    LF = np.zeros(numTarefas, dtype=np.int8)
    SUCESSOR = np.empty(numTarefas, dtype = object)
    for i in range(numTarefas-1, -1,-1):
        if(dados['Predecessor'][i] != None):
            for j in dados['Predecessor'][i]:
                index = buscaTarefa(dados,j)
                if(SUCESSOR[index] != None):
                    SUCESSOR[index] += dados['Codigo'][i]
                else:
                    SUCESSOR[index] = dados['Codigo'][i]

    dados["Sucessor"] = SUCESSOR

    for i in range(numTarefas -1, -1, -1):
        if (dados['Sucessor'][i] == None):
            LF[i] = np.max(dados['EF'])
            LS[i] = LF[i] - dados['Duracao'][i]
        else:
            for j in dados['Sucessor'][i]:
                index = buscaTarefa(dados, j)
                temp.append(LS[index])
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
    dados['FOLGA'] = FOLGA

    dados = dados.reindex(columns = ['Tarefa', 'Codigo','Predecessor','Sucessor','Duracao','ES','EF','LS','LF','FOLGA'])

    return dados

def calculaCPM(dados):
    dados = caminhoDeIda(dados)
    dados = caminhoDeVolta(dados)
    dados = calculaFolga(dados)
    return dados

def cpm(dados):
    dados = calculaCPM(dados)
    indexFolgaZero = np.where(dados['FOLGA'] == 0)[0]
    tarefasCpm = np.array(dados['Tarefa'][indexFolgaZero], dtype=np.str_)
    return tarefasCpm