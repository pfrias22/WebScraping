from pathlib import Path
import csv
class Cryptoclass():
    cols = []
    rows = []
    time = ""
    # def __init__(self, columns):
    #     for c in columns:
    #         self.cols.append(c)
        
        # for r in rows:
        #     print(r)
    def setColumns(self, columns):
        self.cols = columns
        return columns

    def setRows(self, rows):
        self.rows = rows
        return rows

    def setTime(self, time):
        self.time = time
        return time

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