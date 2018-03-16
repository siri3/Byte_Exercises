# Weekend-1-Assignment

You have 3 challenges this weekend. 

**Challenge #1** 

Using the file "words.txt" in this repo, write a function that reads the words in words.txt and stores them as keys in a
dictionary. It doesn’t matter what the values are. Use the 'in' operator to find if a word is in the dictionary. 

Here is some example code for opening files:

    #the .py file and words.txt must be in same folder

    doc = open('words.txt')

    #hold the individual words in a list for further use

    word_list = []


    for word in doc:
  
      word_list.append(word.strip())

**Challenge #2**

Define a function which can print a dictionary where the keys are numbers between 1 and 3 (both included) and the values are square of keys.

**Challenge #3**

You are required to write a program to sort the (name, age, height) tuples by ascending order where name is string, age and height are numbers.

The sort criteria is:

1: Sort based on name;
2: Then sort based on age;
3: Then sort by score.

The priority is that name > age > score.

If the following tuples are given as input to the program:

Tom,19,80
John,20,90
Jony,17,91
Jony,17,93
Json,21,85

Then, the output of the program should be:

[('John', '20', '90'), ('Jony', '17', '91'), ('Jony', '17', '93'), ('Json', '21', '85'), ('Tom', '19', '80')]


Enjoy!!
