#Write a function called most_frequent that takes a string and prints the letters in decreasing order of frequency. 
# use tuple

def most_frequent(word):
    c_set = set(word)
    
    list=[]
    for c in c_set:
        count = word.count(c)
        list.append((count,c))
    
    list.sort(reverse = True)
    
    for t in list:
        print (t[1])
        
    
    
most_frequent("ffffffffddddvvvvbuev")
        