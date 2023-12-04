import unittest
import pandas as pd
from caminhocritico import *

class TestCpm(unittest.TestCase):
    def testOutputType(self):
        fileName = "visualizadorcpm.csv"
        result = LerArquivoCSV(fileName)
        dados = calculaCPM(result)
        typeFile = type(dados)
        typeSample = type(pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}))
        self.assertEqual(typeFile, typeSample)

    def numTarefasError(self):
        with self.assertRaises(ValueError):
            fileName = "numTarefasError.csv"
            result = LerArquivoCSV(fileName)
            calculaCPM(result)

if __name__ == "__main__":
    unittest.main()