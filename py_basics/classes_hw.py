#For each company, store the name, ticker
#symbol, purchase date, purchase price, and number of shares. Methods include: add
#new symbol (new purchase), remove symbol (all shares sold), and YTD or Annual
#Return performance for any or all symbols given a current price (and date).

import datetime

class stock:
    
    def __init__(s,name,ticker,date,price,n):
        s.name = name
        s.ticker = ticker
        s.pur_date = date
        s.pur_price = price
        s.num_shares = n
            
    def ytd(s,price):
        growth = price - s.pur_price
        temp = s.pur_date.split("/")
        time = (datetime.date.today() - datetime.date(int(temp[2]),int(temp[0]),int(temp[1])))/365
        time = time/datetime.timedelta(days=1)
        return (growth/time)
        
    def __delete__(s,obj):
        del s.value
        
     
def add(name,ticker,date,price,n):
    ticker = stock(name,ticker,date,price,n)
    print (ticker," created")
    print (ticker.name)

stocks = ["NFLX","TSLA","INTL","AAPL"]
    
    
    
s1 = stock("netflix","NFLX","2/2/18",200,100)
s2 = stock("tesla","TSLA","1/1/17",75,50)

print (s1.name)
print (s2.ytd(50))

(name,ticker,date,price,n)=input("enter name,ticker,purchase date,price,#shares")
add(name,ticker,date,price,n)



