import mysql.connector
import time
import xlrd
from datetime import datetime

def con():
    try:
        # print('\n################################################## Connecting to Database')

        HOST = 'localhost'                 # IP Host
        # PORT = '3306'                      # Port Number
        USER = 'Admin'                     # Database User
        PASSWORD = 'Admin#2020'            # Database Password
        DB = 'appkey2'                     # Database Name

        string_conection = mysql.connector.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)

        return string_conection

    except Exception as e:
        print(f'Error: {e}')


def insert_tbdFabricante (id_tabelaFipe, name):

    try:
        sql = f"INSERT INTO tbdFabricante (id_TabelaFipe, ds_Fabricante) " \
              f"VALUES ({id_tabelaFipe}, '{name}')"

        connectio = con()                   # Abre Conexão com BD
        cursor = connectio.cursor()         # Obtem uma transação
        cursor.execute(sql)                 # Passa comando de dados em SQL para o BD
        connectio.commit()
        connectio.close()

    except Exception as e:
        print(f'Error: {e}')


def insert_tbdModelo (id_TabelaFipe, id_Fabricante, ds_Modelo):

    try:
        sql = f"INSERT INTO tbdModeloVeiculo (id_TabelaFipe, id_Fabricante, ds_Modelo) " \
              f"VALUES ({id_TabelaFipe}, {id_Fabricante}, '{ds_Modelo}')"

        connectio = con()                   # Abre Conexão com BD
        cursor = connectio.cursor()         # Obtem uma transação
        cursor.execute(sql)                 # Passa comando de dados em SQL para o BD
        connectio.commit()
        connectio.close()

    except Exception as e:
        print(f'Error: {e}')


def insert_tbdTransponder (ds_CodTransponder, ds_NomeCom,):

    try:
        sql = f"INSERT INTO tbdTransponder (ds_CodTransponder, ds_NomeCom) " \
              f"VALUES ('{ds_CodTransponder}', '{ds_NomeCom}')"

        connectio = con()                   # Abre Conexão com BD
        cursor = connectio.cursor()         # Obtem uma transação
        cursor.execute(sql)                 # Passa comando de dados em SQL para o BD
        connectio.commit()
        connectio.close()

    except Exception as e:
        print(f'Error: {e}')


def select_tbdFabricante(id_tabelaFipe):
    sql = f'SELECT * FROM tbdFabricante WHERE id_tabelaFipe = {id_tabelaFipe}'       # Comando SQL

    connectio = con()                    # Abre Conexão com BD
    cursor = connectio.cursor()          # Obtem uma transação
    cursor.execute(sql)                  # Passa comando de dados em SQL para o BD
    result = cursor.fetchall()           # Pega resultado da função

    cursor.close()                       # Fecha Transação
    connectio.close()                    # Fecha Conexão

    for item in result:
        return item


def select_tbdModelo(id_tabelaFipe):
    sql = f'SELECT * FROM tbdModeloVeiculo WHERE id_tabelaFipe = {id_tabelaFipe}'       # Comando SQL

    connectio = con()                    # Abre Conexão com BD
    cursor = connectio.cursor()          # Obtem uma transação
    cursor.execute(sql)                  # Passa comando de dados em SQL para o BD
    result = cursor.fetchall()           # Pega resultado da função

    cursor.close()                       # Fecha Transação
    connectio.close()                    # Fecha Conexão

    for item in result:
        return item
