from app.Models.db.database import database
import pyodbc
import pandas as pd
from app.Models.db import sql_server

def insertDataOperacaoAnalitico(data):
    operacaoData = pd.DataFrame.from_dict(data)
    operacaoData.to_sql('OperacaoCotistaAnalitico',con=sql_server.engine,if_exists='append',index=False, chunksize=10, method='multi')

def insertDataClientePosicao(data):
    posicaoData = pd.DataFrame.from_dict(data)
    posicaoData.to_sql('fundo_posicao',con=sql_server.engine,if_exists='append',index=False, chunksize=10, method='multi')

