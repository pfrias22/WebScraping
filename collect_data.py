#!/usr/bin/env python

from imports_func import *
import cryclass

crypto = cryclass.Cryptoclass()
if(crypto.getRobots()):
    while True:
        print("recolectamos datos...")
        #crypto = cryclass.Cryptoclass()
        df, current_time = crypto.scrap()
        crypto.updateDB(df, current_time)
        time.sleep(60) # Delay for 1 minute (60 seconds). 




