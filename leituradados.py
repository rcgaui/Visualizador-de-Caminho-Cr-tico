import os
from exibicao import *
import csv

def LerArquivoTexto(nomeDoArquivo):
    dirPath = os.path.dirname(os.path.abspath(__file__))
    folderPath = 'GeneralData'
    filePath = os.path.join(dirPath, folderPath)
    filePath = os.path.join(filePath, nomeDoArquivo)
    contadorLinhas = 0

    try:
        with open(filePath, "r") as file:
            cronograma = []

            for task in file:
                contadorLinhas += 1
                tasksArray = task.split()
                if len(tasksArray) != 5:
                    raise Exception("A quantidade de campos preenchidos na linha " + str(contadorLinhas) +  " esta incorreta")
                if '[' in  tasksArray[1]:
                    predecessors = tasksArray[1][1:-1]
                    predecessorsArray = predecessors.rsplit(";")
                    tasksArray[1] = predecessorsArray
                if '[' in tasksArray[2]:
                    successors = tasksArray[2][1:-1]
                    successorsArray = successors.rsplit(";")
                    tasksArray[2] = successorsArray
                
                cronograma.append(tasksArray)
    except FileNotFoundError:
        ErroTXTnotFound(NomeDoArquivo=nomeDoArquivo)
        return None

    file.close()
    return cronograma

def LerArquivoCSV(nomeDoArquivo):
    dirPath = os.path.dirname(os.path.abspath(__file__))
    folderPath = 'GeneralData'
    filePath = os.path.join(dirPath, folderPath)
    filePath = os.path.join(filePath, nomeDoArquivo)
    contadorLinhas = 0

    try:
        with open(filePath, "r") as file:
            csvFile = csv.reader(file)
            cronograma = []


            for lines in csvFile:
                contadorLinhas += 1 
                if(contadorLinhas > 1):
                    if len(lines) != 5:
                        raise Exception("A quantidade de campos preenchidos na linha " + str(contadorLinhas) +  " esta incorreta")
                    if ';' in  lines[1]:
                        predecessors = lines[1]
                        predecessorsArray = predecessors.rsplit(";")
                        lines[1] = predecessorsArray
                    if ';' in lines[2]:
                        successors = lines[2]
                        successorsArray = successors.rsplit(";")
                        lines[2] = successorsArray
                    
                    cronograma.append(lines)
    except FileNotFoundError:
        ErroCSVnotFound(NomeDoArquivo=nomeDoArquivo)
        return None
    
    file.close()
    return cronograma
