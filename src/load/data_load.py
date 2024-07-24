from typing import Dict

import pandas as pd
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from utils.envs import DEST_DB


class DataLoad:
    def __init__(self, dataframe:pd.DataFrame, dimensions:Dict[str, pd.DataFrame]) -> None:
        self.dataframe = dataframe
        self.dimensions = dimensions
        self.db_url = DEST_DB
        self.engine = create_engine(self.db_url)
        self.Session = sessionmaker(bind=self.engine)

    def load_data(self) -> None:
        with self.engine.connect() as connection:
            self.dataframe.to_sql(name='f_fato', con=connection, if_exists='replace', index=False)

            for table_name, df in self.dimensions.items():
                df.to_sql(name=table_name, con=connection, if_exists='replace', index=False)     

