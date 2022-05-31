
from app.Auth.authentication import basicAuthentication
from app.Config import YESTERDAY, API_HML
from dateUts import *


def todosCotistas():
    link =  f'{API_HML}/Fundo/BuscaCotistasPorCPFCNPJouID?cpfCnpj=&idCotista=&nome='
    response = basicAuthentication(link)
    return response


def fundoPosicao(ListCotista,data=""):
      lista = []
      for idCotista in ListCotista:
          link = f'{API_HML}/Fundo/BuscaPosicaoCotistaPorData?dataPosicao={data}&idPosicao=&idCotista={idCotista}&idCarteira=&tipoCotistaMovimentacao='
          response = basicAuthentication(link)
          if not response == []:
                lista.append(response)
                print(f'{len(lista)}: {idCotista}: cliente posicao')

      return lista




def todasCarteiras(dt):
    link =  f'{API_HML}/Common/BuscaCliente?idCliente=&idClienteExterno=&DataAlteracao='
    link =  f'{link}{dt}'
    response = basicAuthentication(link)
    return response

def idCotista(listId):
    lista = []
    for id_cliente in listId:
        link = f'http://saa-ast-0034/WS/api/Fundo/BuscaCotistasPorFundo?idCarteira={id_cliente}'
        response = basicAuthentication(link)
        if not response == []:
            lista.append(response)
        else:
            pass#print("ERROR:",response,id_cliente)
    return lista




def operacaoCotistaAnalitico(listCarteira,dateI,dateF):
    idCarteira = ";".join([str(x['IdCliente']) for x in listCarteira])
    lista      = []
    
    link = f'{API_HML}' + '/Fundo/OperacaoCotistaAnalitico?idsCarteiras={}'
    
    dt       = f'&dataInicio={dateI}&dataFim={dateF}'
    link     = f'{link}{dt}'
    url      = link.format(idCarteira)
    return basicAuthentication(url)