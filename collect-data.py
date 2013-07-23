#!/usr/bin/env python
"""
This script is to be used to simply collect yahoo stock quotes for a 
single stock.
"""
import urllib
import os
import time
from threading import Thread

os.chdir('/home/jacob/Documents/stock-analysis')

BASE_URL = 'http://download.finance.yahoo.com/d/quotes.csv?s='
SYM_URL = '%5EDJI+{symbol}&f=sd1t1l1va2abc1ghk3ops7&e=.csv'
HEADERS = "symbol,last trade date,last trade time,last trade price," + \
          "volume,average daily volume,ask,bid,change,days low," + \
          "days high,last trade size,open,previous close,short ratio\n"

def get_data(symbol="SPY"):
    while True:
        try:
            stocks = urllib.urlopen(BASE_URL + 
                                    SYM_URL.format(symbol=symbol)).read()
        except IOError:
            print "Error reading the socket"
            time.sleep(120)
            continue

        if not os.path.exists("data.csv"):
	    stockdata = open("data.csv", "a")
	    stockdata.write(HEADERS)
        else:
    	    stockdata = open("data.csv", "a")
	    stockdata.write(stocks)
	    stockdata.close()
	    time.sleep(120)

# Start the get_data process as a daemon thread.
t = Thread(target=get_data)
t.daemon = True
t.start()

# If the script starts at 9:30am, then 23401sec should take us to 4:00pm
# Once the script finishes sleeping, it will automatically quit.
time.sleep(23401)

