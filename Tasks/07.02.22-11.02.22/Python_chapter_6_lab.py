# 6.1 Part 1
'''
element = 10
elementCount = 1

for i in range(0, 9):
    for j in range(0, elementCount):
        print(element, " ", end = "")
        element += 1
    elementCount += 1
    print()
'''

# 6.2 Part 2
'''
size = int(input("Enter number of rows: "))

# First row
for i in range(0, (size * 2)):
    print("o", end = "")
print()

# Between rows
betweenRows = size - 2
for i in range(0, betweenRows):
    spaceCount = (size * 2) - 4
    space = ""
    for i in range(0, spaceCount):
        space += " "
    print("o",space,"o")

# Last row
for i in range(0, (size * 2)):
    print("o", end = "")
print()
'''

# 6.3 Part 3
# TO HEAVY!!!
'''
size = int(input("Enter one of the following numbers: 3 or 5: "))

if((size == 3) or (size == 5)):
    # imput: 3: lower = size - 2
    # imput: 3: upper = size + 2
    # imput: 5: lower = size - 4
    # imput: 5: upper = size + 4
    lower = size - 2
    higher = size + 2
    lower_two = 0
    higher_two = 0
    if(size == 5):
        lower_two = size - 4
        higher_two = size + 4

else:
    print("The number you entered is not valid!")
'''

# 6.4 Part 4
# -> Siehe pygame_base_template.py