import requests 
from bs4 import BeautifulSoup
import csv 

def write_to_csv(rows):
	with open('boxofficemojo.csv', 'a') as csvfile:		
		writer = csv.writer(csvfile)
		for i in rows:
			writer.writerow(i)
			
def get_tbl_data(url):
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text,"html.parser")
    rows = soup.findAll('tr', bgcolor = ("#ffffff","#f4f4ff"))
    tbl = []
    for row in rows:
        row_l = []
        for cell in row:
            row_l.append(cell.text)
        tbl.append(row_l)
    return tbl
			
			
base_url = "http://www.boxofficemojo.com/yearly/chart/?page=%d&view=releasedate&view2=domestic&yr=2017&p=.htm"


for i in range(1,9):
    url = base_url % i
    tbl_data = get_tbl_data(url)
    write_to_csv(tbl_data)
    
    