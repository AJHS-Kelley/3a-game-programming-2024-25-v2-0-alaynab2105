# Rock, Paper, Scissors by Alayna Brewer, v3.0

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
def playerName() -> str: # Function Signature -- name of a function, ( arguments if any)
    """Gets the name from the player and returns it. """
    # The line above is a DOCSTRING, it gives a brief example of what the function does.
    playerName = input("Please type your name then press enter.\n")
    print(f"Hello{playerName}!\n")
    isCorrect = input("Is that correct? Type yes or no and press enter.\n")
    if isCorrect == "yes":
        print(f"ok{playerName}, let's play Rock, Paper , Scissors!\n")
    else:   
        playerName=input("Please type your name then press enter.\n")
    return playerName

# CALLING THE FUNCTION
playerName = playerName() 
    
    # THE RULES using MULTIPLE-LINE STRINGS
def rules()-> None:
    """This function prints the rules for rock, paper, scissors."""
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
    # Does another part of this program need to access this information
# IF YES, YOU MUST HAVE A return STATEMENT 
# IF NO, A return STATEMENT IS NOT REQUIRED 

def playerChoice()-> str:
    """Allows the player to choose rock ,paper , scissors."""
    playerChoice = input ("Please enter rock , paper or scissors and press enter.\n").lower()
    if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
        playerChoice = input("Please enter rock, paper or scissors and press enter.\n").lower()
        if playerChoice != "rock" and playerChoice != "paper" and playerChoice != "scissors":
            print( " You are not follwing directions. Please try again.\n")
            exit()
        print(f"You have chosen {playerChoice}.\n")
    else:
        print(f"You have chosen {playerChoice}.\n")
    return playerChoice


def cpuChoice()->str:
    """Allows the CPU to choose rock, paper, scissors."""
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
    return cpuChoice

def pickWinner(playerChoice: str, cpuChoice: str) -> str:# playerChocie and cpuChoice are both ARGUEMENTS, they will be string vaules.
    """This function uses the player choice and CPU choice to determine a winner."""
    if playerChoice == "rock" and cpuChoice =="paper":
        # CPU WINS
        print(f"The CPU chose {cpuChoice} and you chose {playerChoice}.\n")
        print("The CPU wins a point.\n")
        cpuScore += 1
        return "CPU Wins"
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
        return "CPU Wins"
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
        return "CPU Wins"
    else:
        print("Unable to determine a winner. Please restart.\n")
        exit()

# MAIN GAME LOOP
while playerScore < 5 or cpuScore < 5:
    print(f"{playerName} you have {playerScore} points.\nThe CPU has {cpuScore} points.\n")
    

    # let cpu select choice at random.
    
    # print(f"CPU Choice: {cpuChoice}")
    
    # compare player choice to cpu choice 
    



print(f"Your Final Score: {playerScore}CPU Final Score: {cpuScore}\n")
if  playerScore > cpuScore:
    print(f"Congratulations {playerName}, a winner is you!\n")
elif cpuScore > playerScore:
    print(f"The CPU wins. You are a disappointment to all.\n")
else:
    print("Unable to determine a winner.\nPlease restart.\n")
    exit()


























