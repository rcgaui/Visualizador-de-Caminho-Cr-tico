from caminhocritico import *
from exibicao import *
from leituradados import *
import pandas as pd

dados = pd.read_csv("./GeneralData/jogo_da_senha_teste.csv").replace({np.nan: None})
dados = calculaCPM(dados)
print("\n",dados)
print("\n****************************************************************************************************************************\n")
caminhoCritico = cpm(dados)
exibirCaminhoCritico(caminhoCritico)
