import outputformat as ouf

def ErroCSVnotFound(NomeDoArquivo):
    errorMsg = "Desculpe, o arquivo " + NomeDoArquivo + " nao foi encontrado na pasta GeneralData."
    print(errorMsg)

def erroNumeroLinhas(linhas):
    errorMsg = "A quantidade de campos preenchidos na linha " + str(linhas) +  " esta incorreta"
    print(errorMsg)

def erroFormatoArquivo(nomeDoArquivo):
    errorMsg = "O tipo de arquivo  de " + nomeDoArquivo + " inserido não é do tipo csv"
    print(errorMsg)

def exibirCaminhoCritico(data):
    ouf.showlist(data, style="box", title="Caminho Critico")
