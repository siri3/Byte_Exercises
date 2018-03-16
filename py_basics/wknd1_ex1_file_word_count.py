file = open("words.txt")

word_dict = {}

for word in file:
    word_dict[word.strip()]="one day I will hold a meaning"
    
file.close()

#check if word is in dictionary

word = input("enter word ")
if word in word_dict:
    print (word," ",word_dict[word])
else:
    print ("word not found in dictionary")
    
    