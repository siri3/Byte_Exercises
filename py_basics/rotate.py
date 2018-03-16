#rot13

import string

alpha = string.ascii_lowercase

word = input("enter word ")
n = int(input("number to rotate by "))

#index values from -26 to 25 incl
if n < -26 or n > 26:
    n = n % 26
        
rotate = ""

try: 
    for c in word:
        if c.isupper() == True:
          c = c.lower()
          case = 1
        else:
            case = 0

        new_pos = alpha.index(c) + n 
          
        if new_pos > 25:
           new_pos = new_pos - 26
            
        if case == 1: 
            rotate = rotate + alpha[new_pos].upper()
        else:
            rotate = rotate + alpha[new_pos]   
    print(word," ",rotate)
except:
        print("enter only alphabets")
                  

        
        

