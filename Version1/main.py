from cryclass import Cryptoclass

while True:
    crypto = Cryptoclass()
    crypto.scraping()
    crypto.setCSV()
    time.sleep(60) # Delay for 1 minute (60 seconds). 