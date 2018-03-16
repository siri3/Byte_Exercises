import requests 
from bs4 import BeautifulSoup
import csv 
import time

def write_to_csv(rows):
	with open('wsj.csv', 'a') as csvfile:		
		writer = csv.writer(csvfile)
		for i in rows:
			writer.writerow(i)
			
base_url = "http://quotes.wsj.com/"
stocks = ["AAPL","NKE","NFLX","AMZN","MSFT"]
field_names = ['stock','current price','price change','open price','close price','timestamp']

data = [field_names]
for i in stocks:
    url = base_url + i
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text,"html.parser")
    stock_data = [i]
    cur_price = soup.find('span',id = "quote_val").text
    chg_price = soup.find('span',id = "quote_change").text #wouldn't work if spaces in id. then use xpath. note it may be different across pages
    stock_data.extend([cur_price,chg_price])
    
    tags = soup.findAll('span', attrs= {'class':("data_data","data_lbl")})
    for i in tags:
        if i.text.strip() == "Open":
            open_price = i.next_sibling.next_sibling.text
            stock_data.append(open_price)
        #elif i.text.strip() == "Prior Close":
            #close_price = i.next_sibling.next_sibling.text
            #stock_data.append(close_price)
    
    close_price = float(cur_price.replace(",","")) - float(chg_price.replace(",",""))
    stock_data.append(close_price)
            
    ts = time.gmtime()
    stock_data.append(time.strftime("%Y-%m-%d %H:%M:%S", ts))   # 2018-03-03 12:08:22
    
    data.append(stock_data)   
    
write_to_csv(data)
    
    



    
    
