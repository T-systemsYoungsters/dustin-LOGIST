import random

# 1.
'''
for i in range(10):
    print("Dustin Plewa")

print("Done")
'''

# 2.
'''
for i in range(20):
    print("Red")
    print("Gold")
'''

# 3.
'''
for i in range(50):
    print((i + 1) * 2)
'''

# 4.
'''
i = 10
while i >= 0:
    print(i)
    i = i - 1

print("Blast off!")
'''

# 5.
'''
# - total wird nicht ausgegeben sondern x
# - x muss int sein
# total = total + x nicht + i

print("This program takes three numbers and returns the sum.")

total = 0

for i in range(3):
    x = int(input("Enter a number: "))
    total = total + x

print("The total is:", total)
'''

# 6.
'''
i = random.randrange(1, 11)
print(i)
'''

# 7.
'''
i = random.uniform(1, 10)
print(i)
'''

# 8.
'''
total = 0
pos = 0
neg = 0
zero = 0

for i in range(7):
    x = int(input("Enter a number: "))
    total = total + x

    # Checking for positive
    if x > 0:
        pos = pos + 1
    elif x < 0:
        neg = neg + 1
    else:
        zero = zero + 1


print("Total sum:", total)
print("Total pos:", pos)
print("Total neg:", neg)
print("Total zero:", zero)
'''

# 9.
'''
coin = ""
head = 0
tail = 0

for i in range(0, 50):
    i = random.randrange(0, 2)

    if i == 0:
        coin = "head"
        head = head + 1
    elif i == 1:
        coin = "tail"
        tail = tail + 1

    print(coin)

print("Total head:", head)
print("Total tail:", tail)
'''

# 10.
'''
playerChoice = int(input("Enter a number between 0 and 2 (rock, paper, scissors): "))
playerChoiceStr = ""
computerChoice = random.randrange(0, 3)
computerChoiceStr = ""
winner = ""

# Player
if playerChoice == 0:
    playerChoiceStr = "rock"
elif playerChoice == 1:
    playerChoiceStr = "paper"
elif playerChoice == 2:
    playerChoiceStr = "scissors"

# Computer
if computerChoice == 0:
    computerChoiceStr = "rock"
elif computerChoice == 1:
    computerChoiceStr = "paper"
elif computerChoice == 2:
    computerChoiceStr = "scissors"

# Checking win
# Draw
if (computerChoice == 0 and playerChoice == 0) or (computerChoice == 1 and playerChoice == 1) or (computerChoice == 2 and playerChoice == 2):
    winner = "Draw"
# Computer
if (computerChoice == 0 and playerChoice == 2) or (computerChoice == 1 and playerChoice == 0) or (computerChoice == 2 and playerChoice == 1):
    winner = "Computer"
# Player
if (playerChoice == 0 and computerChoice == 2) or (playerChoice == 1 and computerChoice == 0) or (playerChoice == 2 and computerChoice == 1):
    winner = "Player"


# Output
print("Player:", playerChoiceStr)
print("Computer:", computerChoiceStr)
print("Winner:", winner)
'''