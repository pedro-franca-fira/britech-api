
from app.Config import API_HML, YESTERDAY
from app.Auth.authentication import basicAuthentication
from dateUts import *


class ClienteInfo():

  def clientePosicao(ListCotista):
      lista = []
      for idCotista in ListCotista:
          link = f'{API_HML}/Fundo/BuscaPosicaoCotistaPorData?dataPosicao=&idPosicao=&idCotista={idCotista}&idCarteira=&tipoCotistaMovimentacao='
          response = basicAuthentication(link)
          if not response == []:
                lista.append(response)
                print(f'{len(lista)}: {idCotista}: cliente posicao')

      return lista

  def clienteMovimentacao(ListCarteira):
    print('ClienteMovimentacao')
    lista = []
    for idCliente in ListCarteira:
        link = f'{API_HML}/Fundo/BuscaCotistasPorFundo?idCarteira={idCliente}'
        response = basicAuthentication(link)
        if not response == []:
            lista.append(response)
            print(f'{len(lista)}: {idCliente}: cliente movimentacao')

    return lista

  def operacaoCotistaAnalitico(listCarteira):
    dateYstd = lastWorkingDate(fmt="%Y-%m-%d")
    lista = []
    
    link = f'{API_HML}' + '/Fundo/OperacaoCotistaAnalitico?idsCarteiras={}'
    
    ystd = f'&dataInicio={dateYstd}&dataFim={dateYstd}'
    tdy = f'&dataInicio=1900-01-01&dataFim={DateUteis.now(fmt="%d-%m-%Y")}'
    print(listCarteira)

    for idCarteira in listCarteira:
        prm = ystd if YESTERDAY else tdy
        url = f'{link.format(idCarteira)}{prm}'
        print(url)
        response = basicAuthentication(url)
        if not response == []:
            lista.append(response)
            print(f'{idCarteira} - {len(response)} [operacaoCotistaAnalitico]')
    return lista


    