from cryclass import Cryptoclass
import time

crypto = Cryptoclass()
if(crypto.getRobots()):
    while True:
        print("Init web scraping")
        crypto.scraping()
        crypto.setCSV()
        time.sleep(60) # Delay for 1 minute (60 seconds). 