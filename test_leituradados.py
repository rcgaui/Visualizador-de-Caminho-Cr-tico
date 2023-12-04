import unittest
import pandas as pd
from leituradados import *

class TestDados(unittest.TestCase):
    def testFileType(self):
        fileName = "CSVTestFile.csv"
        result = LerArquivoCSV(fileName)
        typeFile = type(result)
        typeSample = type(pd.DataFrame({'col1': [1, 2], 'col2': [3, 4]}))
        self.assertEqual(typeFile, typeSample)

    def testFileNotFound(self):
        with self.assertRaises(FileNotFoundError):
            filename = "ArquivoNaoExiste.csv"
            LerArquivoCSV(filename)

    def testWrongFileType(self):
        with self.assertRaises(ValueError):
            filename = "ArquivoTipoErrado.txt"
            LerArquivoCSV(filename)

    def testDateFormat(self):
        with self.assertRaises(ValueError):
            filename = "CSVTestDate.csv"
            LerArquivoCSV(filename)

if __name__ == "__main__":
    unittest.main()