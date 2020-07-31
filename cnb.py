import random #imports the random modules which generates random numbers

def loop(): 
    #print(num)
    ask= str(input("enter a four digit number: "))
    cow=0
    bull_Cow=0  #total number of digit guessed perfectly. right place + wrong place
    for i in range(0,4):
        if num[i]==ask[i]: # simultaneous checking of right digit at right place
            cow+=1         # increases cow by +1
    for i in num:
        if i in ask:
            bull_Cow +=1    # increments if the digit guessed is present in secret no
    bull=bull_Cow-cow #counts the no of right guesses at wrong place = total right guesses - right guesses #at right place
    print("you have {} cows and {} bulls".format(cow,bull))
    return cow #return 0


if __name__=='__main__':    # When the Python interpeter reads a source file, it first defines a few #special variables. In this case, we care about the __name__ variable
    num= str(random.randrange(1000,9999)) #The randrange() method returns a randomly selected #element from the specified range
    cow= 0
    count=0 #this variable is used to count the number of attempts made by the user
    
    while cow !=4:  # loop continues until cow==4
        count+=1
        cow = loop()  # object creation and calling of function 
        if cow == 4:  
         print("Congrats! You guessed " + str(count) + " times.") #prints success message upon successful guess
