# Rock, Paper, Scissors by Alayna Brewer, v0.0

# MODULE IMPORTS
import random

# DATA STUCTURES -- PLAYER
playerScore = 0
playerName = "Test Player"
playerChoice = None

# DATA STUCTURES -- CPU
cpuScore = 0
cpuChoice = None

# PLAYER NAME INPUT
playerName = input("Please type your name then press enter.\n")
print(f"Hello{playerName}!\n")
isCorrect = input("Is that correct? Type yes or no and press enter.\n")

# .lower() can turn ALL input into lowercase.
#.upper() can turn ALL input into UPPERCASE.

if isCorrect == "yes":
    print(f"ok{playerName}, let's play Rock, Paper , Scissors!\n")
else:   
    playerName=input("Please type your name then press enter.\n")

    # THE RULES using MULTIPLE-LINE STRINGS
    print(f"""
Welcome to Rock, Paper, Scissors Robot!
It's Time to play Rock , Paper, Scissors!
          
You will play against the CPU. The first player to score 5 points wins.
You will select from ROCK, PAPER, or SCISSORS.
The CPU will select ROCK, PAPER OR SCISSORS at random.
          
1) ROCK BEATS SCISSORS
2) SCISSORS BEATS PAPER
3)PAPER BEATS ROCK
"""    )
    
# MULTI-LINE STRINGS CAN BE USED AS BIG COMMENTS
"""
Anything in between the sets of double-quotes is just ignored.
If you need to write large comments, it's easier to use multi-line strings then
putting a # in front of 15 diffrent lines.
"""

# MAIN GAME LOOP
while playerScore < 5 or cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
    playerChoice = input ("Please enter rock , paper or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        print( " You are not follwing directions. Please try again.\n")
        exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")

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
    print(f"CPU Choice: {cpuChoice}")

    # compare player choice to cpu choice 
    if playerChoice == "rock" and cpuChoice =="paper":
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore+=1
    # CPU WINS
    elif playerChoice =="rock" and cpuChoice == "scissors":
    # PLAYER WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1
    elif playerChoice == "rock" and cpuChoice == "rock":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
    elif playerChoice =="scissors" and cpuChoice == "rock":
        # CPU WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n") 
        cpuScore+=1
    elif playerChoice == "scissors" and cpuChoice == "paper": 
        # PLAYER WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n") 
        print("You win a point.\n")
        playerScore += 1 
    elif playerChoice == "scissors" and cpuChoice == "scissors":
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n")
    elif playerChoice == "paper" and cpuChoice == "rock":
        # PLAYER WINS 
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("You win a point.\n")
        playerScore += 1 
    elif playerChoice == "paper" and cpuChoice == "paper": 
        # DRAW
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("It's a draw!\n") 
    elif playerChoice == "paper" and cpuChoice == "scissors":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore+=1 
    else:
        print("Unable to determine a winner. Please restart.\n")
        exit()


print(f"Your Final Score: {playerScore}CPU Final Score: {cpuScore}\n")
if  playerScore > cpuScore:
    print(f"Congratulations {playerName}, a winner is you!\n")
elif cpuScore > playerScore:
    print(f"The CPU wins. You are a disappointment to all.\n")
else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()


























