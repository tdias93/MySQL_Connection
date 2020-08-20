from Include import MySQL_AppKey_Connection
import time
import xlrd

book = xlrd.open_workbook('C:\\Users\\thiag\\Desktop\\Tab_Cad.xlsx')
sh = book.sheet_by_index(0)

x = 1
linha = 2

while sh.cell_value(rowx= x, colx=1) != "":

    ds_CodTransponder = sh.cell_value(rowx= x, colx=0)
    ds_NomeCom = sh.cell_value(rowx= x, colx=1)

    MySQL_AppKey_Connection.insert_tbdTransponder(ds_CodTransponder, ds_NomeCom)

    print(ds_CodTransponder + ', ' + ds_NomeCom)

    x = x + 1
    linha = linha + 1

    #print('Teste: ' + sh.cell_value(rowx=x, colx=1))

    time.sleep(0.02)