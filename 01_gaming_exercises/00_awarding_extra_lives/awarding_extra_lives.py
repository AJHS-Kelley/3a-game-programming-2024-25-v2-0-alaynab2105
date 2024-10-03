lives = 3
playerScore = int(input("put your score in\n"))

if playerScore <= 10000:
    lives -= 1
    print(f"my boyfriend scored {playerScore}points and lost a life\n")
elif playerScore < 100001:
    lives += 1
    print(f"my boyfriend scored {playerScore}points and got a extra life\n")
elif playerScore > 100000:
    lives += 2
    print(f"my boyfriend scored {playerScore}points and earned two extra lives\n")   

print(f"you have {lives} lives remaining.\n")