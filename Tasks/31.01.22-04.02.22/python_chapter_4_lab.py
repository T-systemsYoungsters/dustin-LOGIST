import random

# 1.
print("-------------------------------------------------------------------------------------------------------------")
print("Welcome to Camel!")
print("You have stolen a camel to make your way across the great Mobi desert.")
print("The natives want their camel back and are chasing you down! Survive your desert trek and out run the natives.")
print("-------------------------------------------------------------------------------------------------------------")

# 2.
done = False

# 8.
miles_traveled = 0
thirst = 0
camel_tiredness = 0

# 9.
distance_natives_traveled = -20

# 10.
num_drinks_canteen = 10

# 3.
while not done:
    # 4.
    print("A. Drink from your canteen.")
    print("B. Ahead moderate speed.")
    print("C. Ahead full speed.")
    print("D. Stop for the night.")
    print("E. Status check.")
    print("Q. Quit.")

    # 5.
    user_choice = input("Your choice?: ")

    # 6.
    if user_choice.upper() == "Q":
        done = True

    # 11.
    elif user_choice.upper() == "E":
        print("---------------------------------------------------------------")
        print("Miles traveled:", miles_traveled)
        print("Drinks in canteen:", num_drinks_canteen)
        print("The natives are", distance_natives_traveled, "miles behind you.")
        print("---------------------------------------------------------------")

    # 12.
    elif user_choice.upper() == "D":
        camel_tiredness = 0
        print("---------------")
        print("Camel is happy.")
        print("---------------")
        distance_natives_traveled = distance_natives_traveled + random.randrange(7, 15)

    # 13.
    elif user_choice.upper() == "C":
        miles_traveled = miles_traveled + random.randrange(10, 21)
        print("-------------------------------------------------")
        print("Player traveled:", miles_traveled, "miles so far.")
        print("-------------------------------------------------")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + random.randrange(1, 4)
        distance_natives_traveled = distance_natives_traveled + random.randrange(7, 15)

    # 14.
    elif user_choice.upper() == "B":
        miles_traveled = miles_traveled + random.randrange(5, 13)
        print("-------------------------------------------------")
        print("Player traveled:", miles_traveled, "miles so far.")
        print("-------------------------------------------------")
        thirst = thirst + 1
        camel_tiredness = camel_tiredness + 1
        distance_natives_traveled = distance_natives_traveled + random.randrange(7, 15)

    # 15.
    elif user_choice.upper() == "A":
        if num_drinks_canteen > 0:
            num_drinks_canteen = num_drinks_canteen - 1
            thirst = 0
        else:
            print("---------------")
            print("No more drinks!")
            print("---------------")
    
    # 17.
    if thirst > 6:
        print("-------------------")
        print("You died of thirst!")
        print("-------------------")
        done = True

    # 16.
    elif thirst > 4:
        print("----------------")
        print("You are thirsty!")
        print("----------------")
        

    # 18.
    if camel_tiredness > 5:
        print("----------------------------")
        print("Your camel is getting tired.")
        print("----------------------------")

    # 19.
    elif camel_tiredness > 8:
        print("-------------------")
        print("Your camel is dead.")
        print("-------------------")

    # 20.
    if distance_natives_traveled == 0:
        print("------------------------")
        print("The natives catched you!")
        print("------------------------")
        done = True

    # 21.
    elif distance_natives_traveled == -15:
        print("------------------------------")
        print("The natives are getting close!")
        print("------------------------------")

    # 22.
    if miles_traveled >= 200 and distance_natives_traveled != 0 and camel_tiredness <= 8 and thirst <= 6:
        print("--------")
        print("You won!")
        print("--------")
        done = True

    # 23.
    i = random.randrange(1, 21)
    if i == 1 and done == False:
        print("------------------")
        print("You foud an oasis!")
        print("------------------")
        num_drinks_canteen = 10
        thirst = 0
        camel_tiredness = 0
