import requests
import json

def symbol_lookup(string):
    try:
	    lookup_url = "http://dev.markitondemand.com/Api/v2/Lookup/json?input="
	    url = lookup_url + string
	    r = requests.get(url)
	    data = r.content.decode()
	    py = json.loads(data) #list of dictionaries
	    return py
    except Exception as e:
	    print ('symbol lookup error',e)
	    return

def get_quote(string):
    try:
	    quote_url = "http://dev.markitondemand.com/MODApis/Api/v2/Quote/json?symbol="
	    url = quote_url + string
	    r = requests.get(url)
	    data = r.content.decode()
	    py = json.loads(data)  #dictionary
	    return py
    except Exception as e:
        print ('get quote error',e)
        return
		
