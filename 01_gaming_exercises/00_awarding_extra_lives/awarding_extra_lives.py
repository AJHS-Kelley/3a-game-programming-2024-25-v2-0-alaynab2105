lives = 3
playerScore = int(input("put your score in\n"))

if playerScore <= 10000:
    print(f"my boyfriend scored {playerScore}points and lost a life\n")
elif playerScore < 100001:
     print(f"my boyfriend scored {playerScore}points and got a extra life\n")
else:
    print(f"my boyfriend scored {playerScore}points and earned two extra lives\n")   
