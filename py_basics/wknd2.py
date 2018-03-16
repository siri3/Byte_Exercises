#https://knightlab.northwestern.edu/2014/06/05/five-mini-programming-projects-for-the-python-beginner/


def roll():
    import random
    roll = input("enter y to continue, enter to stop ")
    while roll == "y":
        print (random.randint(1,6))
        roll = input("enter y to continue, enter to stop ")
        
def guess():
    import random
    num = random.randint(1,100)
   
    while True:
        try:
            guess = int(input("Guess a number between 1 and 100 "))       
        except ValueError:
            print("Not an integer!")
            continue
        else:
            break 
    if guess == num:
        print ("guessed correctly")
    elif guess > num:
        print ("guess is too high")   
    else:
        print ("guess is too low")
    print ("number was ",num)
              
def madlib():
    print ("lets make a story, please enter at prompts ")
    sub = input("enter a subject ")
    sub_adj = input("enter something to describe subject ")
    sub_verb = input("what is subject doing? ")
    day = input("what kind of day is it? ")
    print ("here's the story: ")
    print (sub + " is " + sub_adj + " and " + sub_verb + " on a "+ day + " day." )
    
def hangman():
    import random
    import string
    word_list = ["apple","bangle","catterpillar","dance","elephant","federation","gullible","hallucination","indigo","jasmine","lactose","maximise","nymph"]
    word = random.choice(word_list)
    l = len(word)
    guess = "_" * l
    ctr = 0
    level = input("enter difficulty level. 1 - easy 2 - medium 3 - hard ")
    if level == "1":
        n = 13
    elif level == "2":
        n = 10
    elif level == "3":
        n = 7
    else:
        print ("invalid choice. setting level to medium.")
        n = 10
    tries = []
    print ("guess the ",l," letter word. you have ",n,"tries. at any point enter the full word to guess word.")
    for i in range (1,n+1):
        while True:
            ch = input("enter a letter: ")
            if len(ch) == len(word):
                if ch.strip() == word:
                    print ("you have guess correctly!")
                    return word
                else:
                    print ("you have guessed incorrectly!")
                    return word
            if ch not in string.ascii_letters:
                print ("not a letter!")
                continue
            elif ch == "":  
                print ("please enter something ")
                continue
            elif ch in tries:
                print ("letter already tried, try again ")
                continue
            else:
                break
        tries.append(ch)
        pos = word.find(ch)
        while pos >= 0:
            ctr = ctr + 1
            guess = guess[:pos]+ch+guess[pos+1:]
            if pos < l:
                pos = word.find(ch,pos+1) 
        print (i," ",guess)      
        if ctr == l:
            print ("you have guess correctly!")
            return word
    print ("no more tries left!")
    return word
        
            
        
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    