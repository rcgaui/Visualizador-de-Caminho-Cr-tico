import os
from exibicao import *
import pandas as pd
from datetime import datetime

def LerArquivoCSV(nomeDoArquivo):
    dirPath = os.path.dirname(os.path.abspath(__file__))
    folderPath = 'GeneralData'
    filePath = os.path.join(dirPath, folderPath)
    filePath = os.path.join(filePath, nomeDoArquivo)

    pd.options.display.max_rows = 9999

    try:
        with open(filePath, "r") as file:
            csvFile = pd.read_csv(file, header=0,usecols=["Tarefa", "Predecessor", "Sucessor", "Data de Inicio", "Data de Término"])
            csvFile = formata_df(csvFile)         
            file.close()
            return csvFile
    except FileNotFoundError:
        ErroCSVnotFound(NomeDoArquivo=nomeDoArquivo)
        return None
    

def validaCSV(Arquivo):
    contadorLinhas = 0
    i = 0 
    j = 0
    matriz = Arquivo.shape

    if(matriz[1] != 5):
        raise Exception(erroNumeroLinhas(contadorLinhas))   
    while(i<matriz[0]):
        arqloc = Arquivo.loc[i]
        dataInicio = Arquivo.loc[i].at["Data de Inicio"]
        dataFim = Arquivo.loc[i].at["Data de Término"]

        if dataInicio != datetime.strptime(dataInicio, "%d/%m/%Y").strftime('%d/%m/%Y') or dataFim != datetime.strptime(dataFim, "%d/%m/%Y").strftime('%d/%m/%Y'):
                raise ValueError
                
        i += 1
    
def formata_df(dfTarefas): #recebe o arquivo lido com o pd.read_csv(nome)
    date_format = "%d/%m/%Y"

    inicios = dfTarefas["Data de Inicio"]
    fins = dfTarefas["Data de Término"]
    srDura = pd.Series()


    for i in range(0, len(dfTarefas["Tarefa"])):
        dIn =  datetime.strptime(inicios[i], date_format).date()
        dFim = datetime.strptime(fins[i], date_format).date()


        srDura[i] = (dFim - dIn).days

    dfTarefas.drop("Data de Inicio", axis = 1, inplace = True)
    dfTarefas.drop("Data de Término", axis = 1, inplace = True)

    dfTarefas["Duracao"] = srDura
    return dfTarefas       
              


LerArquivoCSV("CSVTestFile.csv")
