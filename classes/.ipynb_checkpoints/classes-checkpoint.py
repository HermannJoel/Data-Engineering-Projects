import pandas as pd
import sqlalchemy as sqlalchemy
from sqlalchemy import create_engine


class SQL:
    
    def __init__(self, query, conxn):
        self.query=query
        self.conxn=conxn
        
    def CreateConnection(self):
        engine=sqlalchemy.create_engine(self.conxn)
        connection=engine.connect()
        return connection
    
    def ReadSql(self):
        dataframe=pd.read_sql_query(
            sql=self.query, con=self.conxn
        )
        return dataframe