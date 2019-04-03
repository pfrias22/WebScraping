#!/usr/bin/env python

from imports_func import *
while True:
    print("recolectamos datos...")
    crypto = Cryptoclass()
    df, current_time = crypto.scrap()
    crypto.updateDB(df, current_time)
    time.sleep(60) # Delay for 1 minute (60 seconds). 



