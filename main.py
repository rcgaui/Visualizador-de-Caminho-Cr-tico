from caminhocritico import *
from exibicao import *
from leituradados import *
import outputformat as ouf
import pandas as pd



ouf.bigtitle("calculo caminho critico")
print("Bem vindo ao projeto de calculo de caminho critico, insira abaixo o nome do arquivo CSV junto com o tipo. Ex: Cronograma.csv\n ")

arquivo =  input("Qual o nome do arquivo? \n")
while(arquivo):
    cpm(arquivo)
    arquivo =  input("Qual o nome do arquivo? \n")

    validacao = input("Gostaria de calcular outro caminho critico? (Y/N)")
    if(validacao != "Y"):
        break


