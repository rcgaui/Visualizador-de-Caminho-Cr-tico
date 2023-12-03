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
            validaCSV(csvFile)
            #chama func palma
    except FileNotFoundError:
        ErroCSVnotFound(NomeDoArquivo=nomeDoArquivo)
        return None
    
    file.close()

def validaCSV(Arquivo):
    contadorLinhas = 0
    i = 0
    matriz = Arquivo.shape

    if(matriz[1] != 5):
        raise Exception(erroNumeroLinhas(contadorLinhas))   
    while(i<matriz[0]):
        dataInicio = Arquivo.loc[i].at["Data de Inicio"]
        dataFim = Arquivo.loc[i].at["Data de Término"]

        if dataInicio != datetime.strptime(dataInicio, "%d/%m/%Y").strftime('%d/%m/%Y') or dataFim != datetime.strptime(dataFim, "%d/%m/%Y").strftime('%d/%m/%Y'):
                raise ValueError
                
        i += 1
    
            
              


#LerArquivoCSV("CSVTestFile.csv")
