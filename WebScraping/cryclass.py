#!/usr/bin/env python

import os
import pandas as pd
from bs4 import BeautifulSoup
import urllib.request
from datetime import datetime
import requests
import urllib.robotparser
from parametros import *

class Cryptoclass:
    
    def __init__(self):
        self.page = parameters_dict["pagina"]
        self.path_output = parameters_dict["path_output"]
        self.columnas = parameters_dict["columnas"]
        self.monedas = parameters_dict["monedas"]
        
    def getRobots(self):
        queue = [self.page]
        robotsUrl = self.page + "robots.txt"
        parse = urllib.robotparser.RobotFileParser()
        parse.set_url(robotsUrl)
        parse.read()
        if parse.can_fetch('*',queue[0]):
            return True
        else:
            return False
        
    def createCSV(self, filename):
        df = pd.DataFrame(columns=self.columnas)
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
        df.columns = self.columnas
        cols = ['MarketCap', 'Price','Volume24h', 'CirculatingSupply']
        df[cols] = df[cols].round(1) # estandarizamos a un decimal
        
        return df, current_time
    
    def plot_values(self):
        import matplotlib.pyplot as plt
        name = input("introduce nombre moneda:")
        year = input("introduce anyo:")
        month = input("introduce mes:")
        day = input("introduce dia:")
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



