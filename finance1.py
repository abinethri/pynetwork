# Note - this code must run in Python 2.7.6 and you must download
# This code fetches financial data by sending query to google and yahoo finance websites and there is no time relay and is accurate. 

import urllib
import json
import datetime

now = datetime.datetime.now()


serviceurl = 'http://finance.google.com/finance/info?'

def stock_info(symbol):

    url = serviceurl + urllib.urlencode({'q':symbol})
    #print 'Retrieving', url
    uh = urllib.urlopen(url)
    data = uh.read()
    #print 'Retrieved',len(data),'characters' 
    json_data = json.loads(data[5:len(data)-2])
    return json_data

serviceurl2 = 'http://autoc.finance.yahoo.com/autoc?'

def get_company_name(sym):
    url2 = serviceurl2 + urllib.urlencode({'query':sym, 'region':'US', 'lang':'en'})
    #print 'Retrieving', url2
    uh = urllib.urlopen(url2)
    data = uh.read()
    #print 'Retrieved',len(data),'characters'
    json_data = json.loads(data)
    company_name = json_data['ResultSet']['Result'][0]['name']  
    return company_name 

while True:    
    try:
        name = raw_input('Enter a stock symbol or done to exit: ')
        if (name == 'done'): break
        data = stock_info(name)
        price = data['l']
        value = data['c']
        percnt_chnge = data['cp']
        last_trade = data['lt_dts']
        print "STOCK PRICE: ", price
        print 
        print "LAST TRADE TIME:", last_trade
        print 
        print "VALUE CHANGES (+ for Increase or - for Decrease): ", value
        print
        print "PERCENTAGE CHANGES (+ for Increase or - for Decrease): ", percnt_chnge,'%'
        print 
        print "CURRENT DATE AND TIME: ", now.strftime("%Y-%m-%d %H:%M"), 'ISO Format: ', now.isoformat()
        company = get_company_name(name)
        print     
        print "COMPANY NAME: ", company
         
        
    except ValueError:
        print("Oops!  That was not a valid symbol. Try again...")    

    except IOError:
        print("Oops! Hit IO Error-- Could be Network issue. Please try again!")

print 'Exiting..See You !'          
        
        
        


