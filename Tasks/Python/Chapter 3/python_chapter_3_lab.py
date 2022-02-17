# 1.
counter = 0

print()
print("Welcome to my quiz")
print("------------------")
print()
print("- You have to answer five questions.")
print("- There are two different answer methods:")
print("  - A, B or C")
print("  - Direct answer")
print()

# First question
print("1. Question")
print("Which year do we have?")
print("----------------------")
print()
print("A: 2019")
print("B: 2021")
print("C: 1921")
print()

answer = input("Enter your answer: ")

if answer.upper() == 'B':
    print("Correct: The answer is B -> 2021")
    counter += 1
else:
    print("Incorrect: The correct answer is B -> 2021")

print()

# Second question
print("2. Question")
print("In which month did we start our studdy?")
print("---------------------------------------")
print()
print("A: October")
print("B: November")
print("C: December")
print()

answer = input("Enter your answer: ")

if answer.upper() == 'A':
    print("Correct: The answer is A -> October")
    counter += 1
else:
    print("Incorrect: The correct answer is A -> October")

print()

# Third question
print("3. Question")
print("How much do we get paid each month in the first year?")
print("-----------------------------------------------------")
print()

answer = input("Enter your answer: ")

if answer.replace(" ", "") == '1209€' or answer == '1209':
    print("Correct: The answer is 1209€")
    counter += 1
else:
    print("Incorrect: The correct answer is 1209€")

print()

# Fourth question
print("4. Question")
print("How does this programing language is spelled correctly?")
print("-------------------------------------------------------")
print()

answer = input("Enter your answer: ")

if answer == 'Python':
    print("Correct: The answer is Python")
    counter += 1
else:
    print("Incorrect: The correct answer is Python")

print()

# Fifth question
print("5. Question")
print("What does the file-ending .md mean?")
print("-----------------------------------")
print()
print("A: Mobilcom Debitel")
print("B: Nothing")
print("C: MarkDown")
print()

answer = input("Enter your answer: ")

if answer.upper() == 'C':
    print("Correct: The answer is C -> MarkDown")
    counter += 1
else:
    print("Incorrect: The correct answer is C -> MarkDown")

print()

# Finishing
print("You got", counter, "points out of 5.")

percent = int((counter * 100) / 5)

print("You have answered", percent, "% of the questions correctly.")
print()