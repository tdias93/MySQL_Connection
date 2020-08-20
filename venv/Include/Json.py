from Include import MySQL_AppKey_Connection
import urllib.request
import json
import time

def url (function):
    if function == 'brand':
        with urllib.request.urlopen('http://fipeapi.appspot.com/api/1/carros/marcas.json') as value:
            data = json.loads(value.read())
            return data

    elif function == 'model':
        with urllib.request.urlopen(f'http://fipeapi.appspot.com/api/1/carros/veiculos/{id_brand}.json') as value:
            data = json.loads(value.read())
            return data


value = url('brand')
i = 1

for brand_value in value:
    id_brand = brand_value['id']
    brand_name = brand_value['name']
    
    try:
        value_id_brand = MySQL_AppKey_Connection.select_tbdFabricante(id_brand)

        if value_id_brand == '':
            MySQL_AppKey_Connection.insert_tbdFabricante(int(id_brand), brand_name)
            print(f'Valore Salvos na Tabela tbdVeiculo - id_Fabricante {i} | id_TabelaFipe: {id_brand} | ds_Fabricante: {brand_name}')
        else:
            print(f'Valores Já Salvos na Tabela tbdVeiculo - {value_id_brand}')

    except Exception as e:
        print(f'Error: {e}')

    time.sleep(0.05)

    value = url('model')

    for car_value in value:
        id_car = car_value['id']
        car_name = car_value['name']

        try:
            value_id_car = MySQL_AppKey_Connection.select_tbdModelo(id_car)

            if value_id_car == '':
                MySQL_AppKey_Connection.insert_tbdModelo (int(id_car), int(i), car_name)
                print(f' Valore Salvos na Tabela tbdModeloVeiculo - id_TabelaFipe: {id_car} | id_Fabricante: {i} | ds_Modelo: {car_name}')
            else:
                print(f'Valores Já Salvos na Tabela tbdVeiculo - { value_id_car}')

        except Exception as e:
            print(f'Error: {e}')
    
        time.sleep(0.05)

    i = i + 1










