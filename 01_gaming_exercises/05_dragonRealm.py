# Dragon Realm, <STUDENT_NAME>, v0.0
# Based on https://inventwithpython.com/chapter6.html by Al Sweigart
# Good progress so far, please make sure to finish by FRIDAY, NOVEMBER 22. 

import random
import time
import datetime

# SAVING DATA TO A FILE
# STEP 1 -- Create the file name to us.
logFileName = "dragonRealmLog" + str(time.time()) + ".txt"
# Just use dragonRealmLog.txt as the file name on line 10. 
# Example: dragonRealmLog1132AM.txt

# STEP 2 -- Create / Open the file to save the data.
saveData = open(logFileName,"a")
# FILE MODES
# "x" CREATES FILE, IF FILE EXISTS, EXIT WITH ERROR MESSAGE.
# "w" CREATES FILE, IF FILE EXISTS, ERASE AND OVERWRITE FILE CONTENTS.
# "a" CREATES FILE, IF FILE EXISTS, APPEND DATA TO THE FILE.

saveData.write("GAME STARTED" + " " + str(datetime.datetime.now()) + "\n")

# ITEM DATA 
itemSelected = 0
numItems= 0 
hasCharger = False
hasSnacks = False
hasHeadphones = False
waitTime = 0
# TRANSPORTATION FATE
busFate = random.randint(0,1)
trainFate = random.randint(0,1)
planeFate = random.randint(0,1)

# GAME FUNCTIONS
def displayIntro():
    print( " Wakey wakey brave solider it's time to get up and find the safest way to get to orlando")
    print('You are in a land full of dragons and trolls. In front of you,')
    print('you see three ways to get to orlando. In one way you see a bus, the dragon is friendly')
    print('and will share his treasure with you. The other dragon')
    print('is greedy and hungry, and will eat you on sight.')
    print('and in the third one there is a troll that is friendly')
    print()
time.sleep(waitTime) 

def chooseTransportation():
    transportation = ''
    while transportation != '1' and transportation != '2'and transportation != '3':
        print('Which transportation will you take? (1,2 or 3) 1 for the bus 2 for the train and 3 for the plane')
        transportation = input()
    return transportation

def checkTransportation(chosenTransportation):
    print('You approach the Bus ...')
    time.sleep(2)
    print('It is dark and spooky...')
    time.sleep(2)
    print('A large dragon jumps out in front of you! He opens his jaws and...')
    print()
    time.sleep(2)

    friendlyTransportation = random.randint(1, 2, 3)

    if chosenTransportation == str(friendlyTransportation):
        print('Gives you his treasure!')

    else:
        print('Gobbles you down in one bite!')

# Game loop 
        
print("This is a text based adventure game. Occassionally, the game will pause to give you time to read the instructions and descriptions.\n" )
waitTime = int(input("How many seconds would you like the game to pause each time?\nA minimum of two seconds and a maximum of five seconds is suggested.\nEnter an integer value and press enter."))

playAgain = 'yes'

while playAgain == 'yes'or playAgain == 'y':

    displayIntro()

    
    # ITEM SELECTION
    print("As you begin to set out for adventure, you need to gather some equipment. You can only bring two items with you.  Choose carefully.\n")
    print("Your options are:a charger, snacks or headphones.\n")
    time.sleep(waitTime)
    numItems = 0 
    while numItems < 2:
        itemSelected = int(input("Which item do you want? Enter 1 for the charger , 2 for the snacks, or 3 for the headphones.\n"))
        if itemSelected == 1:
            hasCharger = True
        elif itemSelected == 2:
            hasSnacks = True
        elif itemSelected == 3:
            hasHeadphones = True
        else:
            print("Unable to determine an item. Please enter 1 for the charger, 2 for the snacks, and 3 for the headphones.\n")
        numItems += 1
        print("You have chosen your equipment and set out for adventure. You are equipped with:\n")
    if hasCharger:
        print("an charger.\n")
    if hasSnacks:
        print("snacks.\n")
    if hasHeadphones:
        print("Headphones.\n")
    time.sleep(waitTime)
    transportation = chooseTransportation()
    if transportation == '1':
        print( " You chose the bus!")
        if busFate == 0:
            print("The bus ride was long but you made it and a troll shared his treasure with you!!")
        elif busFate == 1:
            print("The bus left but suddenly the bus driver passed out and the bus flipped over after a crash and a troll steals everything you have and eats you.")
    elif transportation == '2':
        print(" You chose the train!")
        if trainFate == 0:
            print("You made it , you did have to stop a couple times because of problems with the train but you made it and a friendly dragon gave you some gold!")
        elif trainFate == 1:
            print("All of a sudden the dragon finds you and opens his jaws and eats you in one bite.")
    elif transportation == '3':
        print(" You chose the plane!")
        if planeFate == 0:
            print("You  made it safely and a nice dragon and troll gave you a bunch of treasure!!")
        elif planeFate == 1:
            print("You were almost to orlando but while you were on the plane a dragon blew his fire breathe and blew the whole plane up..")
    

  

playAgain = 'yes'

while playAgain == 'yes' or playAgain == 'y':
    displayIntro()
    transportationNumber = chooseTransportation()
    (transportationNumber)
    print('Do you want to play again? (yes or no)')
    playAgain = input()




# CLOSE THE FILE
saveData.write("END OF GAME LOG\n\n")
saveData.close()
