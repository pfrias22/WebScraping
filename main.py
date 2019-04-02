import urllib.request
from bs4 import BeautifulSoup
import datetime
from cryclass import Cryptoclass

crypto = Cryptoclass()
response = urllib.request.urlopen("https://coinmarketcap.com")
html = response.read()
bs = BeautifulSoup(html, 'html.parser')
tab = bs.find('table')

# COLUMNS
head = tab.findAll('th')
header = []
for h in range(0,7):
    if h != 0:
        header.append(head[h].text)

crypto.setColumns(header)

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

fila = []
for r in range(0,len(resto)):
        for j in range(2,9):
                if j == 2 and type(resto[r][j+1]) is str and not (any(char.isdigit() for char in resto[r][j+1])):
                        fila.append(resto[r][j] + " " + resto[r][j+1])
                elif (j == 3) and (any(char.isdigit() for char in resto[r][j])):
                        fila.append(resto[r][j]) 
                elif j == 6 and not (any(char.isdigit() for char in resto[r][3])):
                        fila.append(resto[r][j])
                elif j == 6 and (any(char.isdigit() for char in resto[r][3])):
                        fila.append(resto[r][j] + " " + resto[r][j+1])                
                elif (j == 7) and not (any(char.isdigit() for char in resto[r][3])):
                        fila.append(resto[r][j] + " " + resto[r][j+1])
                elif (j == 8) and not (any(char.isdigit() for char in resto[r][3])):
                        fila.append(resto[r][j+1])
                elif (j == 8) and (any(char.isdigit() for char in resto[r][3])):
                        fila.append(resto[r][j])
                elif (j != 3) and (j != 7) and (j != 8):
                        fila.append(resto[r][j]) 
        body.append(fila)  
        fila = []

crypto.setRows(body)
crypto.setTime(datetime.datetime.now().strftime("%Y-%m-%d %H:%M"))
crypto.setCSV()