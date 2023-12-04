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

def iniciaPrompt():
    ouf.linetitle("                                                                                                                        ", style="double")
    ouf.bigtitle("calculo caminho critico")
    ouf.boxtitle("Bem vindo ao projeto de calculo de caminho critico, insira abaixo o nome do arquivo CSV junto com o tipo. Ex: Cronograma.csv", style="double")
    
def printSepara():
    print("\n")
    ouf.linetitle("                                                                                                                        ", style="double")
    print("\n")