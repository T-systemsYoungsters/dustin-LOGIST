# 1.
'''
temperature = float(input("Temperature: "))
if temperature > 90:
    print("It is hot outside.")
else:
    print("It is not hot out.")
'''

# 2.
'''
number = int(input("Enter a number: "))

if number < 0:
    print("The number is negative.")
elif number > 0:
    print("The number is positive.")
else:
    print("The number is 0.")
'''

# 3.
'''
number = int(input("Enter a number: "))

if number > -10 and number < 10:
    print("Success")
'''

# 4.
'''
user_input = input("A cherry is a: ")
print("A. Dessert topping")
print("B. Desert topping")
if user_input.upper() == "A":
    print("Correct!")
else:
    print("Incorrect.")
'''

# 5.
'''
x = 0
if x > 0:
    print("x is positive.")
elif x == 0:
    print("x is not positive and not negative.")
else:
    print("x is not positive.")
'''

# 6.
'''
x = int(input("Enter a number: "))
if x == 3:
    print("You entered 3")
'''

# 7.
'''
answer = input("What is the name of Dr. Bunsen Honeydew's assistant? ")
a = ""

if a == "Beaker":
    print("Correct!")
else:
    print("Incorrect! It is Beaker.")
'''

# 8.
'''
x = input("How are you today?")
if x == "Happy" or x == "Glad":
    print("That is good to hear!")
'''

# 9.
'''
x = 5
y = x == 6 # 5 == 6
z = x == 5 # 5 == 5
print("x=", x)
print("y=", y)
print("z=", z)
if y:
    print("Fizz")
if z:
    print("Buzz")
'''

# 10.
'''
x = 5
y = 10
z = 10
print(x < y) # True
print(y < z) # False
print(x == 5) # True
print(not x == 5) # False
print(x != 5) # False
print(not x != 5) # True
print(x == "5") # False ?
print(5 == x + 0.00000000001) # False
print(x == 5 and y == 10) # True
print(x == 5 and y == 5) # False
print(x == 5 or y == 5) # True
'''

# 11.
'''
print("3" == "3") # True
print(" 3" == "3") # False
print(3 < 4) # True
print(3 < 10) # True
print("3" < "4") # True
print("3" < "10") # True -> False
print( (2 == 2) == "True" ) # False
print( (2 == 2) == True ) # True
print(3 < "3") # False ? -> Error
'''

# 12.
'''
print("Welcome to Oregon Trail!")
 
print("A. Banker")
print("B. Carpenter")
print("C. Farmer")

A = 'Banker'
B = 'Carpenter'
C = 'Farmer'
money = 0
 
user_input = input("What is your occupation? ")

if user_input == A:
    money = 100
elif user_input == B:
    money = 70
elif user_input == C:
    money = 50
 
print("Great! you will start the game with", money, "dollars.")
'''