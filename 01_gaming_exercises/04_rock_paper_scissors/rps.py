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
 if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors":
    playerChoice = input("Please enter rock, paper or scissors and press enter.\n").lower()
    if playerChoice != "rock" or playerChoice != "paper" or playerChoice != "scissors"
# print the current scorre for CPU and player
# let player select rock, paper, scissors ,
# let cpu select choice at random.
# compare player choice to cpu choice 
# print the results to the screen 
# award point to winner and output results.

