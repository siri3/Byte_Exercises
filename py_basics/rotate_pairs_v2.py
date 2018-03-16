def rotate(word,n):
    import string
    alpha = string.ascii_lowercase

    #index values from -26 to 25 incl
    if n < -26 or n > 26:
        n = n % 26
        
    rotate = ""
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
    
    return(rotate)

import string
word_list = []
print ("enter words, press ""enter"" when you are done")
while True:
    flag = 1
    word = input("enter word ")
    if word == "":
        break
    else:
        for c in word:
            if c not in string.ascii_letters:
                print ("enter only letters")
                flag = 0
                break
        if flag == 1: 
            word_list.append(word)
# ask if better way to do this

rotate_pairs = {}
for word in word_list:
    for n in range (0,26):
        rotate_pairs[word] = rotate(word,n)
#how to store dict with duplicate keys but different items

print (rotate_pairs)





