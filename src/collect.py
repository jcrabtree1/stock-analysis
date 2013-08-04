#!/usr/bin/env python
"""
This script is to be used to simply collect yahoo stock quotes for a 
single stock.
"""
import urllib
import os
import time
from threading import Thread

os.chdir('/home/pi/Documents/stock-analysis')

BASE_URL = 'http://download.finance.yahoo.com/d/quotes.csv?s='
SYM_URL = '%5EDJI+{symbol}&f=sd1t1l1va2abc1ghk3ops7&e=.csv'
HEADERS = "symbol,date,time,price," + \
          "volume,average daily volume,ask,bid,change,days low," + \
          "days high,last trade size,open,previous close,short ratio\n"

def get_data(symbol="SPY"):
    now = time.localtime()
    while now.tm_hour < 16:
        now = time.localtime()
        try:
            stocks = urllib.urlopen(BASE_URL + 
                                    SYM_URL.format(symbol=symbol)).read()
        except IOError:
            print "Error reading the socket"
            time.sleep(120)
            continue

        if not os.path.exists("data/%s.csv" % symbol):
	    stockdata = open("data/%s.csv" % symbol, "a")
	    stockdata.write(HEADERS)
        else:
    	    stockdata = open("data/%s.csv" % symbol, "a")
	    stockdata.write(stocks)
	    stockdata.close()
	    time.sleep(300)

if __name__ == '__main__':
    get_data()

