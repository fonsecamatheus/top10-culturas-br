import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


class DataLoad:
    def __init__(self, dataframe: pd.DataFrame) -> None:
        self.dataframe = dataframe
        #self.db_url = r'sqlite:///C:/Users/fonseca-matheus/Desktop/top10-culturas-br/data/top10culturasBR.sqlite'
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)

    def load_data(self) -> None:
        with self.engine.connect() as connection:
            self.dataframe.to_sql(name='tabela_fato', con=connection, if_exists='replace', index=False)
        print(f"Dados carregados com sucesso na tabela")

