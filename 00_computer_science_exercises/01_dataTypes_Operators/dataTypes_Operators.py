newInt = 3
newFloat = 4.0
newString=" Skibidi Toilet"
newBool= False
print(type(newInt))
print(type(newFloat))
print(type(newString))
print(type(newBool))
# Comparison Operators 

# Is-EQUAL-TO == Are the two vaules equal to each other?
# Returns True or False based on evaluation.
x = 6
print(x == 5)

# NOT-EQUAL-TO != Are the two vaules NOT equal?
# Returns True or False based on evaluation.
print(x != 12)

# GREATER THAN / GREATER -THAN-OR-EQUAL TO
print(5 > 3) # Greater Than 
print(12 >= 2) # Greater Than or Equal To

# LESS THAN / LESS-THAN-OR-EQUAL TO
print (5 <3 ) # LESS Than
print (12 <= 2) # less than or equL to

# LOGICAL OPERATORS 
# and - - ALL CONDTIONS MUST BE FALSE FOR ENTIRE STATMENT TO BE TRUE 
age = 16 
height = 68
# In order to ride the Teacups , you must be atleast 18 years old and atleast 60' tall
print(age >= 18 and height >=60)
print ( age >= 18 and height >= 60 and eyeColor == "Blue")
# ALWAYS CHECK FOR THE MOST LIKELY TO BE TRUE CONDITION!!!!!!
print ( defeatedBoss == True and level > 5 and hasBluekey == True)

# or - - AT LEAST ONE CONDITION MUST BE TRUE FOR ENTIRE STATEMENT TO BE TRUE 
print(age >= 18 and height >=60)
print ( age >= 18 and height >= 60 and eyeColor == "Blue")

# not -- RETURNS THE OPPOSITE VALUE OF THE STATEMENT .
a = 5
print (a == 5 )
print ( not ( not ( a == 5 )))
# COMBINING LOGICAL OPERATORS 
print (a == 5 and hasKey == True or isCloud == True)
# TRUE and .
# IDENTITY OPERATORS 
g = 1.0
h = 1.0
i = g 
print (g is h )
print ( i is h )
print ( i is not 1.0)
print ( i is not g )

# MEMBESHIP OPERATORS 
fruits = [ "apple", " banana", "tomato"]
print ( "banana" in fruits )
