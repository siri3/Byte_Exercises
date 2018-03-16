#does position of function matter
# learn how to have dic with non unique keys

def isrotate(word1, word2):
    import string
    l1 = len(word1)
    l2 = len(word2)
    
    if l1 != l2:
        return False
    
    diff = ord(word2[0]) - ord(word1[0])
    if diff < 0:
        diff = 26 + diff # rotate by -1 is same as rotate by 25
    for i in range (1,l1):
        diff_i = ord(word2[i]) - ord(word1[i])
        if diff_i < 0:
            diff_i = 26 + diff_i
        if diff_i != diff:
            return False
    return True

dict={}
print ("enter words, press ""enter"" when you are done")
while True:
    word = input("enter word ")
    if word == "":
        break
    else:
        dict[word]=""
        
for k in dict:
    rotate_pair=[] 
    for w in dict:
        if k in dict[w]: 
            rotate_pair.append(w)
            continue 
        print (flag)
        if isrotate(k,w) == True and k !=w :
            rotate_pair.append(w)
    dict[k]=rotate_pair
    
print (dict)
    

            
        
        
        
        