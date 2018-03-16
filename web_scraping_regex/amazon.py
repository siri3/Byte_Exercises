from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import csv
import time



def write_to_csv(rows):
	with open('amazon.csv', 'a') as csvfile:	
	    col_names = ["name","price","rating"]
	    writer = csv.writer(csvfile)
	    writer.writerow(col_names)
	    for i in rows:
	        writer.writerow(i)
	        
#driver.find_elements_by_xpath('//ul[@id="s-results-list-atf"]/li')
#items = results.find_elements_by_xpath('//*')

def get_page_items():

    ul_tag = driver.find_element_by_id('s-results-list-atf')
    items = ul_tag.find_elements_by_tag_name('li')  

    rows = []
    for item in items:
        
        #some discounts also have li tag, won't grab any data, can disregard or filter out here
        id = item.get_attribute('id')
        if id.find("result_") >=0:
            pass
        else:
           continue
            
        html = item.get_attribute('outerHTML')
        soup = BeautifulSoup(html,'html.parser')
     
        #remove sponsored text
        try:
            name = soup.find('h2').text    
        except:
            name = "missing"
            
        #other prices also use this class, make sure its the price
        try:
            price = soup.find('span', attrs = {'class':'a-size-base a-color-price s-price a-text-bold'}).text
        except:
            price = "missing"
    
        try:
            #asin = item.get_attribute('data-asin')
            #rating_tag = soup.find('span', attrs = {'name' : asin})
            #for child in rating_tag.descendants:
            #<span class="a-icon-alt">4 out of 5 stars</span> 
            #4 out of 5 stars
            #how to access
        
            #ratings = soup.findAll('span', attrs = {'class':'a-icon-alt'})
            #[<span class="a-icon-alt">prime</span>, <span class="a-icon-alt">1 out of 5 stars</span>]
            #how to iterate?
            #for i in rating:
                #print (rating.string)
        
            ratings = soup.findAll('span', attrs = {'class':'a-icon-alt'})
            if ratings[0].text.strip() == "prime":
                rating = ratings[1].text
            else:
                rating = ratings[0].text
            end = rating.find("out of")
            rating = rating[:end].strip()
        except:
            rating = "missing"

        rows.append([name,price,rating])
    return rows

#loop over n pages total 
def loop_pages(n):
    n = n-1                   #page 1 already loaded
    for i in range(2,2+n):
        next = driver.find_element_by_link_text('Next Page')
        page_url = next.get_attribute('href')
        driver.get(page_url)
        
        page_items = get_page_items()
        write_to_csv(page_items)

start = time.time()

result_id = 0     
url = "https://www.amazon.in"
driver = webdriver.Chrome()
driver.get(url)

search_str = input("enter item to search: ")
n = int(input("enter number of pages to return: "))
search_box = driver.find_element_by_id('twotabsearchtextbox')
search_box.send_keys(search_str)
search_box.submit()

#how to handle when no matches
page_items = get_page_items()
write_to_csv(page_items)

loop_pages(n)   #do we need to pass driver

end = time.time()
print (end - start)

"""   

from selenium.webdriver.support.ui import WebDriverWait

driver = webdriver.Firefox()
driver.wait = WebDriverWait(driver, 5) 

selenium.common.exceptions.WebDriverException: Message: unknown error: 
Element <a href="/s/ref=sr_pg_...?rh=i%3Aaps%2Ck%3Ajuice&amp;page=2&amp;keywords=juice&amp;ie=UTF8&amp;qid=1520373622">2</a> 
is not clickable at point (691, 535). 
Other element would receive the click: <h4 id="sx-hms-title" class="a-color-secondary">...</h4>
   

    items=[]
    base = '//*[@id="result_%d"]'
    global result_id
    while True:
        try:         
            xpath = base % result_id
            item = driver.find_element_by_xpath(xpath)  
            items.append(item)
            result_id += 1
        except:
            break
            
            
        page_buttons = driver.find_elements_by_class_name('pagnLink')
        for elem in page_buttons:
            if elem.text.strip() == 'i':
            button = elem.find_element_by_tag_name('a')
        page_url = button.get_attribute('href')
        driver.get(page_url)
        break
"""
    
    