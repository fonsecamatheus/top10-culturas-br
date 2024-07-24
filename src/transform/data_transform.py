from typing import Any, Dict, List

import pandas as pd


class DataTransform:
    def __init__(self, data_extract:List[Dict[str, Any]]) -> None:
        self.df = pd.DataFrame(data_extract)

    def data_transforms(self) -> pd.DataFrame:
        #Deletando colunas do df
        self.df.drop(['NC', 'NN', 'MC', 'D1C', 'D2C', 'D3C', 'D4C'], axis=1, inplace=True)
        #Renomeando as colunas do df
        self.df.rename(columns={'MN':'UNIDADE', 'V':'VALOR', 'D1N': 'LOCAL', 'D2N':'VARIAVEL', 'D3N':'ANO', 'D4N':'PRODUTO'}, inplace=True)     
        #Tratando os valores da coluna PRODUTO 
        self.df['PRODUTO'] = self.df['PRODUTO'].str.replace(' (em caroço)', '')\
                                               .str.replace(' (em casca)', '')\
                                               .str.replace(' (em grão)', '')\
                                               .str.replace(' (cacho)', '')\
                                               .str.replace(' (em grão)', '')\
                                               .str.replace(' Total', '')

        self.df['VALOR'] = self.df['VALOR'].replace({'...': None, '-': None}).astype('float32')
        self.df['ANO'] = self.df['ANO'].astype('int32')

        return self.df

    
    