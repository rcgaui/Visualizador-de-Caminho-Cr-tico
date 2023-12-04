from caminhocritico import *
from exibicao import *
from leituradados import *
import outputformat as ouf
import pandas as pd



iniciaPrompt()

arquivo =  input("Qual o nome do arquivo? \n")
while(arquivo):
    
    cpm(arquivo)

    printSepara()

    validacao = input("Gostaria de calcular outro caminho critico? (Y/N) ")
    if(validacao != "Y"):
        break
    
    arquivo =  input("Qual o nome do arquivo? \n ")

    


