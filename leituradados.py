import os
from exibicao import *

def LerArquivoTexto(NomeDoArquivo):
    dirPath = os.path.dirname(os.path.abspath(__file__))
    folderPath = 'GeneralData'
    filePath = os.path.join(dirPath, folderPath)
    filePath = os.path.join(filePath, NomeDoArquivo)
    contadorLinhas = 0

    try:
        with open(filePath, "r") as file:
            cronograma = []
            contadorLinhas += 1

            for task in file:
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
        ErroTXTnotFound(NomeDoArquivo=NomeDoArquivo)
        return None
        

    

    file.close()
    return cronograma

LerArquivoTexto("TestFile.txt")