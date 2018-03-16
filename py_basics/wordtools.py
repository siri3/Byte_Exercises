#1. Remove white spaces in a string
def remove_spaces(str):
    for c in str:
        if c == " ":
            continue
        else:
            new_str = new_str + c
    return (new_str)
      
#2. Return a dictionary of characters against its count present in the string
def ch_count(str):

    dict = {}

    for c in set(str):
       dict[c] = str.count(c)
    
    return (dict)


#3. Read the contents of the file, and returns the word count dictionary
def word_count(file_name):

    file = open(file_name)
    text = file.read()
   
    text = text.split()
      
    dict = {}

    for word in text:
        word = word.lower()
        if word[-1].isalpha() == False:
            word = word[:-1]
        
        if word in dict:
            dict[word] = dict[word] + 1
        else:
            dict[word] = 1
    
    file.close()
    
    return (dict)

#4. Check whether a string is palindrom or not
#5. Sort the word in an alphabetical order

#6. Search and replace a string with new string
def find_replace(str,search_str,replace_str):
    pos = str.find(search_str)
    l = len(search_str)
    return (str[:pos]+replace_str+str[pos+l-1])

#7. Convert all the characters in the string to lower case and return the lower case string
def lower(str):
    new_str=""
    for c in str:
        if c in range (97,123):
            new_c = chr(ord(c)-32)
            new_str = new_str + new_c
        else:   
            new_str = new_str + c
    return(new_str)
        
#8. Convert all the characters in the string to upper case and return the upper case string
def upper(str):
    new_str=""
    for c in str:
        if c in range (65,91):
            new_c = chr(ord(c)+32)
            new_str = new_str + new_c
        else:   
            new_str = new_str + c
    return(new_str)
    