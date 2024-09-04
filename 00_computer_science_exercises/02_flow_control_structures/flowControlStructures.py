# Flow Control Structres , Alayna Brewer , v0.0
# Making Computer Programs Make Decisions 

temperature = 199.35
color = "Blue"
height = 5
likesPineappleOnpizza = True 

# SINGLE DECCISION POINT - if Statment 
# if CONDITIONAL_EXPRESSION: <-- this will use a COMPARISON OPERATOR 99% of the time .
# runThiscode IF the CONDITIONAL_EXPRESSION is True

if temperature > 100:
    print("It is hot as the sun outside.\n")

if color ==  "Blue":
    print("ilovemyman")
if height =="5":
    print("i want money not friends") 

# what if we want something diffrent to happen ?
if color == "Red": # COMMON ERROR FOR STUDENTS IS USING = INSTEAD OF ==.
    print( "Your shirt is the correct unifrom color. /n")

else:
    print("Your shirt is not the correct unifrom color. /n")

    # AMUSEMENT PARK HEIGHT CHECKER EXAMPLE 
    # Must be > min. height and < max. height to ride.
   
    # When writing if-elif-else blocks check for the HIGHEST VALUE first when using > or >=
if height >= 6:
    print("You're tall enough to ride the Tea Cups!/n")
elif height >= 3: 
    print("You're to tall to ride the Tea Cups!/n")
else: # "oh, no, something's wrong!"
    print(" Error , height not detected . Do not ride ./n")


# When writing if-elif-else blocks check for the LOWEST VALUE first when using < or <=
if height >= 3:
    print("You're not tall enough to ride the Tea Cups!/n")
elif height >= 6: 
    print("You're tall enough to ride./n")
else: # "oh, no, something's wrong!"
    print(" Error , height not detected . Do not ride ./n")
temperature= 99
if temperature >= 100:
    print (" It's too hot, students cannot go to recess./n" )
    elif