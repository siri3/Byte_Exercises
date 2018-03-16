import model
import markit
import time

def user_name_chk(user_name):
    check = model.get_user(user_name) #returns row
    if check is None:
        return -1  #user not found
    else:
        return 1  #user_name exists

def view_user(user_name, password):
    try:
        user = model.get_user(user_name)  #returns row
        if user is not None: 
            if user[0] == password:
                return (user[1], user[2]) #balance, admin
            else:
                return (-2,0)  #incorrect password
        else:
            return (-1,0)    #user not found
    except Exception as e:
        return (e,)

def new_user(user_name, password, first, last, email):
    try:
        add = model.add_user(user_name, password, first, last, email)
        return add
    except Exception as e:
        print ('add new user error ',e)
        return e
        
def user_trade(user_name):
    i = 1
    while True:
        choice = input('\n'+'Enter 1 - To enter a stock name. 2 - To enter a stock symbol. ')
        if choice == '1':
            name = input('\n'+'Enter full or partial name of stock for lookup. ')
            symbol = markit.symbol_lookup(name)
            if len(symbol) == 0:
                print ('\n'+'No match found for that name. You have a total of five attempts')
                i += 1
            elif len(symbol) > 1:
                print ('\n'+'Too many matches found. You have a total of five attempts')
                print (symbol)
                i += 1
            elif len(symbol) == 1:
                print ('\n'+'Lookup successful!','\n',symbol)
                symbol = symbol[0]['Symbol']
                stock_data = markit.get_quote(symbol)
                print ('\n'+'Stock data:','\n',stock_data)
                break
            else:
                print ('Unknown error. You have a total of five attempts')
                print (symbol)                   
        elif choice == '2':
            symbol = input('\n'+'Enter stock symbol. ')
            symbol = symbol.upper()
            stock_data = markit.get_quote(symbol)
            if 'Message' in stock_data:
                print (stock_data['Message'],'\n','You have a total of 5 attempts.')
                i += 1
            elif stock_data['Status'] == 'SUCCESS':
                print (stock_data)
                break
            else:
                print (stock_data)
        else:
            print ('Incorrect choice. You have a total of 5 attempts.')
            i += 1
        if i > 5:
            return    
    i = 1
    while True: 
        choice = input('\n'+'Enter 1 - To Buy. 2 - To Sell. ')
        try:
            qty = int(input('Enter Quantity '))
        except Exception as e:
            print ("qty error ",e)
            i += 1         
        if choice == '1':
            action = model.buy(user_name,stock_data['Name'],symbol,qty,stock_data['LastPrice'])
            if action:
                print ('Insuffienct balance of ' + str(action) + ' to complete transaction.')
            else:
                print ('Transaction completed ')
                break
        elif choice == '2':
            action = model.sell(user_name,symbol,qty,stock_data['LastPrice'])
            if action:
                if action == -1:
                    print ('You do not own this stock')
                else:
                    print ('Insuffienct quantity of ' + str(action) + ' to complete transaction.')
            else:
                print ('Transaction completed ')
                break
        else:
            print ('Incorrect choice. You have a total of five attempts')
            i += 1
        if i > 5:
            return 

# earnings = 100000(cash bal + cur stock value)/100000 
def stocks_earnings(user_name):
    try:
        stocks = model.view_stocks(user_name)   #list of (name, symbol, qty, userid) tuples
        user = model.get_user(user_name)        #password, balance, admin
        acct_bal = user[1]
        if not stocks:
            return (acct_bal,0,(acct_bal - 100000))
        stocks_val = 0
        stocks_list = []
        for t in stocks:
            name = t[0]
            symbol = t[1]
            qty = t[2]
            stock_data = markit.get_quote(symbol)
            #print ('getting stock data...','\n')
            time.sleep(3)                       #to not exceed requests/sec
            cur_value = qty * stock_data['LastPrice']
            stocks_list.append((name,symbol,qty,cur_value))
            stocks_val = stocks_val + cur_value
        earnings = acct_bal + stocks_val - 100000
        return (acct_bal,stocks_val,earnings,stocks_list) 
    except Exception as e:
        print ('stocks_earnings error ', e)
    
def leader_board():
    users = model.get_users()  #userid, balance, first, last
    users_list = []
    for user in users:
        userid = user[0]
        if userid == 'admin123':
            continue
        acct_bal = user[1]
        name = user[2] + ' ' + user[3]
        data = stocks_earnings(userid)  #(acct_bal,stocks_val,earnings,stocks_list) 
        stocks_val = data[1]
        earnings = data[2]
        users_list.append((earnings,acct_bal,stocks_val,userid,name))  
    users_list.sort(reverse=True)
    return users_list
            
    
