# 1. What is missing from this code? (1 pt)
- ")" in Zeile 1

# 2. Write a Python program that will take in a number from the user and print if it is positive, negative, or zero. Use a proper if/elif/else chain, don't just use three if statements.
- Siehe python_chapter_3_worksheet.py

# 3. Write a Python program that will take in a number from a user and print out ``Success'' if it is greater than -10 and less than 10, inclusive. (1 pt)
- Siehe python_chapter_3_worksheet.py

# 4. This runs, but there is something wrong. What is it? (1 pt)
- Die Antwortmöglichkeiten werden erst angezeigt, nachdem man geantwortet hat.

# 5. There are two things wrong with this code that tests if x is set to a positive value. One prevents it from running, and the other is subtle. Make sure the if statement works no matter what x is set to. Identify both issues. (2 pts)
- Siehe python_chapter_3_worksheet.py
- x == 4 -> x = 4
- Null ist weder positiv noch negativ: if x >= 0: -> if x > 0:

# 6. What three things are wrong with the following code? (3 pts)
- Siehe python_chapter_3_worksheet.py
- input("Enter a number: ") -> int(input("Enter a number: "))
- if x = 3 -> if x == 3
- if x == 3 -> if x == 3:

# 7. There are four things wrong with this code. Identify all four issues. (4 pts)
- Siehe python_chapter_3_worksheet.py
- a ist nicht deklariert
- if a = "Beaker": -> if a == "Beaker":
- Einrückung else
- else -> else:

# 8. This program doesn't work correctly. What is wrong? (1 pt)
- Siehe python_chapter_3_worksheet.py
- Das if Statement war inkorrekt. Jede Eingabe wurde als Richtig gewertet.

# 9. Look at the code below. Write your best guess here on what it will print. Next, run the code and see if you are correct. Clearly label your guess and the actual answer. Also, if this or any other example results in an error, make sure to state that an error occurred. While you don't need to write an explanation, make sure you understand why the computer prints what it does. Don't get caught flat-footed when you need to know later. (2 pts)
- Guess: Buzz
- Answer: Buzz

# 10. Look at the code below. Write you best guess on what it will print. Next, run the code and see if you are correct. (2 pts)
- Siehe python_chapter_3_worksheet.py

# 11. Look at the code below. Write you best guess on what it will print. Next, run the code and see if you are correct. (2 pts)
- Siehe python_chapter_3_worksheet.py

# 12. What things are wrong with this section of code? The programmer wants to set the money variable according to the initial occupation the user selects. (1 pt)
- Siehe python_chapter_3_worksheet.py
- A, B, C sind nicht deklariert
- if user_input = A: -> if user_input == A:
- elif user_input = B: -> elif user_input == B:
- elif user_input = C: -> elif user_input == C:
- else if -> elif