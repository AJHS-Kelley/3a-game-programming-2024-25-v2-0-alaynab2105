# Rock, Paper, Scissors by Alayna Brewer, v0.0

# MODULE IMPORTS
import random, time

# DATA STUCTURES -- PLAYER
playerScore = 0
playerChoice = None
numDraws = 0
# DATA STUCTURES -- CPU
cpuScore = 0
cpuChoice = None


 # MAIN GAME LOOP 
loopCount= 0
loopsReq = int(input("How many loops do you want\nEnter an integer, no commas, and press ENTER "))
# req is the universal abbreviation in computer programming for REQUEST. reqs= REQUEST
rpsTimeStart = time.time() # returns the number of seconds since Jan. 01, 1970 @ 12:00AM
while loopCount < loopsReq :
    
       # let cpu select choice at random.
    cpuChoice = random.randint(0,2) # randomly select 0,1, or 2.
    if cpuChoice == 0:
        cpuChoice= "rock"
    elif cpuChoice == 1:
        cpuChoice ="paper"
    elif cpuChoice == 2:
        cpuChoice = "scissors"
    else:
        print("unable to determine CPU choice.\nPlease restart.\n")
        exit()
        # print(f"CPU Choice:{cpuChoice}")

    # let PLAYER select choice at random.
    playerChoice = random.randint(0,2) # randomly select 0,1, or 2.
    if playerChoice == 0:
        playerChoice= "rock"
    elif playerChoice == 1:
        playerChoice ="paper"
    elif playerChoice == 2:
        playerChoice = "scissors"
    else:
        print("unable to determine CPU choice.\nPlease restart.\n")
        exit()
    print(f"playerChoice {playerChoice}\n cpuChoice {cpuChoice}")    
    # compare player choice to cpu choice 
    if playerChoice == "rock" and cpuChoice =="paper": # THIS IS CORRECT
    # CPU WINS     
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n") 
        cpuScore+=1  
    elif playerChoice == "rock" and cpuChoice == "rock":
         # THIS IS A DRAW
        
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point\n")
        numDraws +=1
    elif playerChoice =="scissors" and cpuChoice == "rock":  
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        # CPU WINS
        cpuChoice+=1
    elif playerChoice == "scissors" and cpuChoice == "paper": 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n") 
        print("You win a point.\n") 
        # PLAYER WINS
        playerScore += 1   
    elif playerChoice == "scissors" and cpuChoice == "scissors": 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        # THIS IS A DRAW
        numDraws +=1
    elif playerChoice == "paper" and cpuChoice == "rock": 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        # PLAYER WINS
        playerScore += 1 
    elif playerChoice == "paper" and cpuChoice == "paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n") 
        # DRAW
        numDraws +=1
    elif playerChoice == "paper" and cpuChoice == "scissors":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        # CPU WINS
        cpuChoice+=1
        
    elif playerChoice == "paper" and cpuChoice == "scissors":      
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        # CPU WINS
        cpuScore += 1
    else:
        print("Unable to determine a winner. Please restart.\n")
        exit()
    loopCount += 1 


print(f"Your Final Score: {playerScore}CPU Final Score: {cpuScore}\n")
if  playerScore > cpuScore:
    print(f"Congratulations. a winner is you!\n")
elif cpuScore > playerScore:
    print(f"The CPU wins. You are a disappointment to all.\n")
else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()

rpsTimeStop = time.time()
rpsTime = rpsTimeStop - rpsTimeStart
print(f"Number of loops:{loopCount}\n")
print(f"Execution Time {rpsTime:.2F} seconds.\n") # :.2F formats to 2 deciaml places.





















