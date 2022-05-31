
from app.Libs.db.database import Database
from app.Libs.db.sql_uteis import DbSqlA
import urllib
from app.Config import *

try:
  sql_server = DbSqlA(f"mssql+pyodbc://{DATABASE_USER}:{urllib.parse.quote_plus(DATABASE_PASSWORD)}@{DATABASE_SERVER}/{DATABASE_NAME}?driver={DATABASE_DRIVER}")
except Exception as e:
  print(f'Erro ao conectar no banco de dados: {e}')
  exit()