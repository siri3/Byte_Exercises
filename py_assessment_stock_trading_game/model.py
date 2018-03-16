import sqlite3
        
def add_user(user_name, password, first, last, email):
    try:
        conn = sqlite3.connect('tradex.db')
        c = conn.cursor()
        c.execute('INSERT INTO Users (userid, password, first, last, email, balance) VALUES (?,?,?,?,?,100000)', (user_name, password, first, last, email,))
        conn.commit()
        conn.close()
        return True
    except Exception as e: 
        return e

def get_user(user_name):
    try:
        conn = sqlite3.connect('tradex.db')
        c = conn.cursor()
        c.execute('SELECT password, balance, admin FROM Users WHERE userid = ?', (user_name,))
        row = c.fetchone()
        return row
    except Exception as e:
        print ("view_user ", e)
        return
        
def get_users():
    try:
        conn = sqlite3.connect('tradex.db')
        c = conn.cursor()
        c.execute('SELECT userid, balance, first, last FROM Users')
        users = c.fetchall()
        return (users)
    except Exception as e:
        print ('get users', e)
        return
        
def view_stocks(user_name):
    try:
        conn = sqlite3.connect('tradex.db')
        c = conn.cursor()
        c.execute('SELECT * FROM Stocks WHERE userid = ?', (user_name,)) #name, symbol, qty, userid
        rows = c.fetchall()  #returns list of tuples
        #header = c.description
        conn.commit()
        conn.close()
        return rows
    except Exception as e: 
        print ("view_stocks error: ",e)
        return
            
def buy(user_name, stock_name, symbol, qty, price):
    try:
        conn = sqlite3.connect('tradex.db')
        c = conn.cursor() 
        
        c.execute('SELECT balance FROM Users WHERE userid = ?', (user_name,))
        row = c.fetchone()
        balance = row[0]
        purchase_amt = price * qty
        if balance < purchase_amt:
            return balance
            
        c.execute('SELECT qty FROM Stocks WHERE userid =? AND symbol =?',(user_name, symbol,))
        row = c.fetchone()
        if row is not None:
            c.execute('UPDATE Stocks SET qty = ? WHERE userid = ? AND symbol =?', ((row[0] + qty), user_name, symbol,))
        else:
            c.execute('INSERT INTO Stocks (name, symbol, qty, userid) VALUES (?,?,?,?)', (stock_name, symbol, qty, user_name, ))
        
        balance = balance - purchase_amt
        c.execute('UPDATE Users SET balance = ? WHERE userid = ?', (balance, user_name,))
        
        conn.commit()
        conn.close()
    except Exception as e:
        print ('buy error', e)
        return
    
def sell(user_name, symbol, qty, price):
    try:
        conn = sqlite3.connect('tradex.db')
        c = conn.cursor() 
       
        c.execute('SELECT qty FROM Stocks WHERE userid = ? AND symbol =?', (user_name, symbol,))
        row = c.fetchone()
        if row is not None:
            prev_qty = row[0]
        else:
            return -1
        if prev_qty < qty:
                return prev_qty
        else:
            new_qty = prev_qty - qty
        c.execute('UPDATE Stocks SET qty = ? WHERE userid = ? AND symbol =?', (new_qty, user_name, symbol,))
        
        c.execute('SELECT balance FROM Users WHERE userid = ?', (user_name,))
        row = c.fetchone()
        balance = row[0] + (price * qty)
        c.execute('UPDATE Users SET balance = ? WHERE userid = ?', (balance, user_name,))
              
        conn.commit()
        conn.close()
    except Exception as e:
        print ('sell error', e)
        return
    

    
    