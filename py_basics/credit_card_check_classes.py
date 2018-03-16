Using the [Luhn Algorithm](http://en.wikipedia.org/wiki/Luhn_algorithm), also known as "modulus 10", we will be determining the validity of a given credit card number.

For now, you are just editing the included python file. You will find the skeleton of the `CreditCard` class inside. 
We want our class to have its three main properties set on [instantiation](http://en.wikipedia.org/wiki/Instance_(computer_science)) - card_number, card_type, and valid. 
Look at the code, you'll see this already there.

If the card number given passes the Luhn algorithm, valid should be true and cardType should be set to 'VISA', 'AMEX', etc. 
If it does not pass, valid should be false and cardType should be set to "INVALID"

Class Card:

    def __init__(myCard,valid,type,num):
        myCard.valid = valid
        myCard.card_type = type
        myCard.card_number = num
    
    def determine_card_type(myCard):
        if str(myCard.card_number).startswith("4"):
            myCard.card_type = "Visa"
        elif int(str(myCard.card_number)[:2]) in range (51,56):
            myCard.card_type = "Mastercard"
        elif myCard.card_number.startswith("34") or myCard.card_number.startswith("37"):
            myCard.card_type = "AMEX"
        elif str(myCard.card_number).startswith("6011") 
            myCard.card_type = "Discover"
        else:
            myCard.card_type = "INVALID"
            
    def check_length(myCard):
        l = len(str(myCard.card_number))
        if (myCard.card_type == "Visa" or "Mastercard" or "Discover") and (l == 16):
            myCard.valid = True
        else:
            myCard.valid = False
        if (myCard.card_type == "AMEX" and (l == 15):
            myCard.valid = True
        else:
            myCard.valid = Fasle

    def validate(myCard):
        num = list(str(myCard.card_number))
        l = len(num)
        sum = 0
        for i in range (l,-1,-1):
            
            digit = num[i]*2
            if digit > 9:
                digit = digit - 9
            sum = sum + digit
        if sum%10 == 0:
            myCard.valid = True
        else:
            myCard.valid = False
        return myCard.valid
            
            




Keep your code super clean and [DRY](http://en.wikipedia.org/wiki/Don't_repeat_yourself). 
If you are repeating yourself, stop and think about how to better approach the problem. 
Keep your code encapsulated - imagine your CreditCard class is an interface other code will need to read. 
You want it as separate and unentangled as possible. Your class should not be dependent on any code outside of it - except, of course, code to instantiate it.



