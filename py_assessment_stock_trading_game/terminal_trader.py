import controller 
import sys
import getpass

def f(data):
    return ('${:,.2f}'.format(data))
    
def user_activity():  
    while True:
        choice = input('\n'+'1 - View Portfolio 2 - Buy/Sell stocks 3 - Logout ')
        if choice == '1':
            data = controller.stocks_earnings(user_name)  #(acct_bal,stocks_val,earnings,stocks_list) 
            print ('\n'+'Cash Balance: ', f(data[0]))  
            print ('Stocks Current Value: ', f(data[1]))
            print ('Account Value: ', f(data[0]+data[1]))
            print ('Account Earnings: ', f(data[2]),' ',('{:.4%}'.format(data[2]/100000)))   
            if len(data) > 3:
                print ('Stocks: ')
                for stock in data[3]:
                    print (stock)
            else:
                print ('Portfolio is empty')
        elif choice == '2':
            controller.user_trade(user_name)
        elif choice == '3':
            break
        else:
            print ('Incorrect choice. You have a total 5 attempts.')
            i += 1
###main###
while True:
    print ('\n'+'Welcome to the Terminal Stock Trader Game: ')
    choice = input('1: User Login'+'\n'+'2: Add New User'+'\n'+'3: Admin Login'+'\n'+'4: Exit game'+'\n')       
    if choice == '1':
        j = 1
        while j <= 5:
            user_name = input('Enter Username: ')
            password = getpass.getpass('Enter Password: ')
            action = controller.view_user(user_name, password) #returns tuple balance, admin, e
            balance = action[0]
            if balance >= 0:
                print ('\n'+'Login successful! Retreiving account information ...')
                data = controller.stocks_earnings(user_name)
                print ('\n'+'Cash Balance: ', f(data[0]))  
                print ('Stocks Current Value: ', f(data[1]))
                print ('Account Value: ', f(data[0]+data[1]))
                print ('Account Earnings: ', f(data[2]),' ',('{:.4%}'.format(data[2]/100000))) 
                user_activity()
                break
            elif action[0] == -1:
                print ('User name not found. You have a total of 5 attempts.')
                j += 1
            elif action[0] == -2:
                print ('Password incorrect. You have a total of 5 attempts. ')
                j += 1
            else:
                print (action[0], ' You have a total of 5 attempts.')
                j += 1      
    elif choice == '2':
        j = 1
        while j <= 5:
            user_name = input('Enter Username: ')
            action = controller.user_name_chk(user_name)
            if action == 1:
                print ('User name already exists. You have a total of 5 attempts. ')
                j += 1
            else:
                password = getpass.getpass('Password: ')
                first = input('First Name: ')
                last = input('Last Name: ')
                email = input('Email: ') 
                action = controller.new_user(user_name, password, first, last, email)
                if action == True:
                    print ('New user added. Your account is credited with $100,000. Continue trading game! ')
                    user_activity()
                    break
                else:
                    print (action, ' You have a total of 5 attempts.')
                    j += 1                  
    elif choice == '3': 
        j = 1
        while j <= 5:
            user_name = input('Enter Username: ')
            password = getpass.getpass('Enter Password: ')
            action = controller.view_user(user_name, password)   
            if action[1] == 1:   #admin status
                users = controller.leader_board()  #earnings, acct bal, userid, name
                print('***Leaderboard (by earnings)***')
                print('user name | userid | earnings | earnings% | account value | cash balance | stocks value')
                for i in range(0,len(users)):
                    print (users[i][4],'|',users[i][3],'|',f(users[i][0]),'|', '%.4f' %(users[i][0]/1000),'|',f(users[i][1] + users[i][2]),'|',f(users[i][1]),'|',f(users[i][2]))
                break
            else:
                print ('Admin error. You have a total of 5 attempts.')
                j += 1         
    elif choice == '4':
        print ('Bye..! Hope you enjoyed playing.'+'\n')
        sys.exit()
    else:
        print ('Invalid selection. Try again!')





 
        
            
            

