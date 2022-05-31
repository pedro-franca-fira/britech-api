from app.Steps.api import *
from app.Steps.upload import *
from app.Models.Cliente import ClienteInfo
from app.Models.db import sql_server
from dateUts import *
from app.Config import *
import pandas as pd
import os
os.system("cls")

#idpos,datahistorico

def main(): 

  if YESTERDAY:
    dtIn = lastWorkingDate(fmt='sql')
    dtFm = lastWorkingDate(fmt='sql')
  else:
    dtIn = '1900-01-01'
    dtFm = lastWorkingDate(fmt='sql')

  # RETORNA TODOS OS COTISTAS
  cotistas   = todosCotistas()
  idCotistas = [x['IdCotista'] for x in cotistas]

  # RETORNA TODOS OS FUNDOS NA DATA INFORMADA DE CADA COTISTA
  dtRng = dateRange(sqlToDate('2021-11-01'),today(),fmt='sql')

  datepos = []
  for dt in dtRng:
    val = fundoPosicao(idCotistas,dt)
    if not val: continue
    dte = val[0][0]["DataHistorico"]
    if dte.split("T")[0] == dt:
      datepos.append(val)

  datepos = sum(sum(datepos,[]),[])
  insertDataClientePosicao(datepos)
  #UPLOAD DATEPOS

  #==============================

  carteiras   = todasCarteiras(dtIn)
  idCarteiras = [x['IdCliente'] for x in carteiras]


  carteiras   = todasCarteiras(dtIn)
  # idCarteiras = [x['IdCliente'] for x in carteiras]
  # joinned     = ";".join([str(x['IdCliente']) for x in carteiras])
  opCotAn = operacaoCotistaAnalitico(carteiras,dtIn,dtFm)

  insertDataOperacaoAnalitico(opCotAn)







