#!/usr/bin/env python

import os
import pandas as pd
import urllib.request
from bs4 import BeautifulSoup
from datetime import datetime
import requests

class Cryptoclass():
    cols = []
    rows = []
    time = ""
    
    def __init__(self):
        self.page = "https://coinmarketcap.com/"
        self.path_output = "/home/miquel/Escritorio/UOC/Q2_18_19/TCVD/PRACTICA1/OUTPUT"
        
    def createCSV(self, filename):
        df = pd.DataFrame(columns=['Name', 'MarketCap', 'Price','Volume24h', 'CirculatingSupply', 'Change24h','timestamp'])
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
                if len(linea) == 6 and linea[0] in ["Bitcoin", "Ethereum", "XRP", "Litecoin", "Bitcoin Cash"]:
                    linea.append(current_time)
                    datos.append(linea)
                linea = []

        df = pd.DataFrame(datos) 
        df.columns = ['Name', 'MarketCap', 'Price','Volume24h', 'CirculatingSupply', 'Change24h', 'timestamp']
        
        return df, current_time


