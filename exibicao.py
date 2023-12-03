import outputformat as ouf

def ErroTXTnotFound(NomeDoArquivo):
    errorMsg = "Desculpe, o arquivo " + NomeDoArquivo + " nao foi encontrado na pasta GeneralData."
    print(errorMsg)

def ErroCSVnotFound(NomeDoArquivo):
    errorMsg = "Desculpe, o arquivo " + NomeDoArquivo + " nao foi encontrado na pasta GeneralData."
    print(errorMsg)

def erroNumeroLinhas(linhas):
    errorMsg = "A quantidade de campos preenchidos na linha " + str(linhas) +  " esta incorreta"
    print(errorMsg)

def exibirCaminhoCritico():
    data = ["Tarefa 1", "Tarefa 7", "Tarefa 8", "Tarefa 11"]
    ouf.showlist(data, style="box", title="Caminho Critico")
