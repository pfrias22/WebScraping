from pathlib import Path
import csv
import urllib.request
from bs4 import BeautifulSoup
import datetime

class Cryptoclass():
    cols = []
    rows = []
    time = ""

    def __init__(self):
        self.page = "https://coinmarketcap.com/"

    def scraping(self):
        response = urllib.request.urlopen(self.page)
        html = response.read()
        bs = BeautifulSoup(html, 'html.parser')
        tab = bs.find('table')
        self.time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        # COLUMNS
        head = tab.findAll('th')
        header = []
        for h in range(0,7):
                if h != 0:
                        header.append(head[h].text)
                else:
                        header.append("");
        header.append("timestamp")
        self.setColumns(header)
        # ROWS
        body = []
        rest = []
        for row in tab.findAll('tr'):
            fila = ""    
            for c in row.findAll('td'):  
                fila += c.text
            rest.append(fila)

        resto = []
        for i in range(1,len(rest)):
            resto.append(rest[i].split())
        print(resto)
        fila = []
        for r in range(0,len(resto)):
                for j in range(0,10):
                        if j == 2 and type(resto[r][j+1]) is str and not (any(char.isdigit() for char in resto[r][j+1])):
                                fila.append(resto[r][j] + " " + resto[r][j+1])
                        elif (j == 3) and (any(char.isdigit() for char in resto[r][j])):
                                fila.append(resto[r][j]) 
                        elif j == 6 and (any(char.isdigit() for char in resto[r][3])) and not (any(char.isdigit() for char in resto[r][j+2])):
                                fila.append(resto[r][j] + " " + resto[r][j+1] + " " + resto[r][j+2])
                        elif j == 6 and not (any(char.isdigit() for char in resto[r][3])):
                                fila.append(resto[r][j])
                        elif j == 6 and (any(char.isdigit() for char in resto[r][3])):
                                fila.append(resto[r][j] + " " + resto[r][j+1]) 
                        elif (j == 7) and not (any(char.isdigit() for char in resto[r][3])) and not (any(char.isdigit() for char in resto[r][j+2])):
                                fila.append(resto[r][j] + " " + resto[r][j+1] + " " + resto[r][j+2])
                        elif (j == 7) and not (any(char.isdigit() for char in resto[r][3])) and (any(char.isdigit() for char in resto[r][j+2])):
                                fila.append(resto[r][j] + " " + resto[r][j+1])
                        elif (j == 8) and (any(char.isdigit() for char in resto[r][j])):
                                fila.append(resto[r][j])
                        elif (j == 8) and not (any(char.isdigit() for char in resto[r][j])) and not (any(char.isdigit() for char in resto[r][j+1])):
                                fila.append(resto[r][j+2])
                        elif (j == 8) and not (any(char.isdigit() for char in resto[r][3])) and (any(char.isdigit() for char in resto[r][j+1])):
                                fila.append(resto[r][j+1])
                        elif (j == 8) and (any(char.isdigit() for char in resto[r][3])) and not (any(char.isdigit() for char in resto[r][j])):
                                fila.append(resto[r][j+1])
                        elif (j == 9) and not (any(char.isdigit() for char in resto[r][3])) and (any(char.isdigit() for char in resto[r][j])) and (any(char.isdigit() for char in resto[r][j-1])):
                                fila.append(resto[r][j+1])
                        elif (j != 3) and (j != 7) and (j != 8) and (j != 1) and (j != 9) and (j != 10):
                                fila.append(resto[r][j])
                fila.append(self.time)
                body.append(fila)  
                fila = []

        self.setRows(body)

    def setColumns(self, columns):
        self.cols = columns
        return columns

    def setRows(self, rows):
        self.rows = rows
        return rows

    def setCSV(self):        
        my_file = Path("./cryptocurrencies.csv")
        if my_file.is_file():
            with open(my_file, 'a') as csvfile:
                for r in self.rows:
                    filewriter = csv.writer(csvfile, lineterminator='\n')
                    filewriter.writerow(r)
        else:
            with open(my_file, 'w') as csvfile:
                writer = csv.writer(csvfile, lineterminator='\n')
                writer.writerow(self.cols)                
                for r in self.rows:
                    writer.writerow(r)