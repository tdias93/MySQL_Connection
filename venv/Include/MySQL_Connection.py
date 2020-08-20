import mysql.connector
import time
import xlrd
from datetime import datetime

def con():
    try:
        # print('\n################################################## Connecting to Database')

        HOST = '187.182.165.126'           # IP Host
        PORT = '3306'                      # Port Number
        USER = 'Admin'                     # Database User
        PASSWORD = 'Admin#2020'            # Database Password
        DB = 'Homologa_si'                 # Database Name

        string_conection = mysql.connector.connect(host=HOST, port=PORT, user=USER, passwd=PASSWORD, db=DB)

        return string_conection

    except Exception as e:
        print(f'Error: {e}')


def insert(name, lat, lng):

    try:
        sql = f"INSERT INTO location (NAME, lat, lng, course, speed, type, payload, nr_serial) " \
              f"VALUES ('{name}', '{lat}', '{lng}', 0.0, 0.0, '{name}', '{name}','1')"
        #sql = f'INSERT INTO location (name) VALUES ("Teste")'

        connectio = con()                   # Abre Conexão com BD
        cursor = connectio.cursor()         # Obtem uma transação
        cursor.execute(sql)                 # Passa comando de dados em SQL para o BD
        connectio.commit()
        connectio.close()

        print('TESTE -' + str(x))

    except Exception as e:
        print(f'Error: {e}')


def select():
    sql = 'SELECT * FROM location'       # Comando SQL

    connectio = con()                    # Abre Conexão com BD
    cursor = connectio.cursor()          # Obtem uma transação
    cursor.execute(sql)                  # Passa comando de dados em SQL para o BD
    result = cursor.fetchall()           # Pega resultado da função

    cursor.close()                       # Fecha Transação
    connectio.close()                    # Fecha Conexão

    for item in result:
        print(item)


book = xlrd.open_workbook('C:\\Users\\thiag\\Desktop\\Teste_BD.xlsx')
sh = book.sheet_by_index(0)

x = 1
linha = 1

while linha <= 934:

    name = sh.cell_value(rowx= x, colx=1)
    lat = float(sh.cell_value(rowx= x, colx=2))
    lng = float(sh.cell_value(rowx= x, colx=3))

    insert(name, lat, lng)

    print(str(lat) + ', ' + str(lng))

    x = x + 1
    linha = linha + 1

    time.sleep(1)


'''

id = 1
i = 1
while i <= 994:
    connectio = con()                           # Abre Conexão com BD
    cursor = connectio.cursor()                 # Obtem uma transação
    cursor.execute(F'SELECT * FROM location WHERE ID > {id}')    # Passa comando de dados em SQL para o BD
    result = cursor.fetchall()                  # Pega resultado da função

    for item in result:
        print(item)
        id = item[0]

    i = i + 1
    connectio.close()                    # Fecha Conexão
    time.sleep(1)
    
'''
