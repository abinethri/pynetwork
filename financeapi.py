#Note - this code must run in Python 2.7.6 and you must download
# this program uses google finance api and yahoo finance api to get finance data.
 
from googlefinance import getQuotes
from yahoo_finance import Share
import urllib2
import json
import datetime

while True:
    
    try:
        symbol = raw_input('Enter a valid Company symbol or done to exit :')
        if (symbol == 'done'): break 
        share = Share(symbol)
        dict_data = getQuotes(symbol)[0]
        stock_price = dict_data['LastTradePrice']
        trade_time = dict_data['LastTradeDateTime']
        now = datetime.datetime.now()

        print
        print 'COMPANY NAME: ',share.get_name()
        print
        print 'CURRENT STOCK PRICE: ', stock_price
        print
        print 'LAST TRADE DATE AND TIME:' , trade_time
        print
        print 'CURRENT DATE AND TIME: ', now.strftime("%Y-%m-%d %H:%M") 
        print 
        print 'ISO Format Time:', now.isoformat()
        print 
        print "VALUE CHANGE(+ for Increase or - for Decrease): ", share.get_change()
        print 
        print "PERCENTAGE CHANGE(+ for Increase or - for Decrease): ", share.get_percent_change()
        
    
    except ValueError:
        print("Oops!  That was not a valid symbol. Try again...")    

    except urllib2.URLError:
        print("Oops! Hit IO Error-- Could be Network issue. Please try again!")
   
print 
print 'Exiting..See You !'        
