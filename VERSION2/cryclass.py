#!/usr/bin/env python

import os
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import requests

class Cryptoclass:
    cols = []
    rows = []
    time = ""
    
    def __init__(self):
        self.page = "https://coinmarketcap.com/"
        self.path_output = "/home/miquel/Escritorio/UOC/Q2_18_19/TCVD/PRACTICA1/VERSION2/OUTPUT"
        self.monedas = ["Bitcoin", "Ethereum", "XRP", "Litecoin", "Bitcoin Cash"]
        self.columnas_a_extraer = ['Name', 'MarketCap', 'Price','Volume24h', 'CirculatingSupply', 'Change24h','timestamp']
        
    def createCSV(self, filename):
        df = pd.DataFrame(columns=self.columnas_a_extraer)
        df.to_csv(filename)

    def updateDB(self, df, current_time): 
        year = current_time[:4]
        month = current_time[4:6]
        day = current_time[6:8]
        my_file = os.path.join(self.path_output, year, month, day, "data.csv")
        if not os.path.exists(os.path.join(self.path_output, year)):
            os.mkdir(os.path.join(self.path_output, year))
        if not os.path.exists(os.path.join(self.path_output, year, month)):
            os.mkdir(os.path.join(self.path_output, year, month))
        if not os.path.exists(os.path.join(self.path_output, year, month, day)):
            os.mkdir(os.path.join(self.path_output, year, month, day))
        if not os.path.exists(my_file):
            self.createCSV(my_file)
        
        df.to_csv(my_file, mode='a', header=False)
             

    def scrap(self):
        page = requests.get(self.page)
        soup = BeautifulSoup(page.content)
        current_time = datetime.now().strftime('%Y%m%d%H%M%S')
        
        datos = []
        linea = []

        for link in soup.find_all('td'):
            valor = link.get('data-sort')
            if valor is not None:
                linea.append(valor)
            else:
                if len(linea) == 6 and linea[0] in self.monedas:
                    linea.append(current_time)
                    datos.append(linea)
                linea = []

        df = pd.DataFrame(datos) 
        df.columns = self.columnas_a_extraer
        cols = ['MarketCap', 'Price','Volume24h', 'CirculatingSupply']
        df[cols] = df[cols].round(1) # estandarizamos a un decimal
        
        return df, current_time
    
    def plot_values(self):
        import matplotlib.pyplot as plt
        name = input("introduce nombre moneda:")
        year = input("introduce año:")
        month = input("introduce mes:")
        day = input("introduce día:")
        print("ploteamos datos...")
        path_data = os.path.join(self.path_output, year, month, day, "data.csv")
        if os.path.exists(path_data):
            df = pd.read_csv(path_data)
            # seleccionamos las filas correspondientes a la moneda deseada
            valid_rows = df.loc[df['Name'] == name]
            # ordenamos los valores por fecha
            valid_rows_sort = valid_rows.sort_values(by=['timestamp'])
            valid_rows_sort['timestamp'] = valid_rows_sort['timestamp'] - int(str(year)+str(month)+str(day)+str("000000"))
            plt.plot(valid_rows_sort['timestamp'], valid_rows_sort['Price'])
            plt.ylabel("price")
            plt.xlabel("timestamp (hhmmss)")
            plt.title("price evolution of " + name + " at " + day + "/" + month + "/" + year)
            plt.show() 
        else:
            print("no tenemos datos para esta moneda o esta fecha")



