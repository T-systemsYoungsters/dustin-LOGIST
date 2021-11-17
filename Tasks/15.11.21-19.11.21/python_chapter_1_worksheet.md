# 1. Write a line of code that will print your name.
- print("Dustin Plewa")

# 2. How do you enter a comment in a program?
- "#"

# 3. What do the following lines of code output? ALSO: Why do they give a different answer?
- print(2 / 3) -> 0.6666666666666666
- print(2 // 3) -> 0
- "/" Dividiert Zahlen und gibt Nachkommastellen aus
- "//" Dividiert Zahlen und streicht Nachkommastellen

# 4. Write a line of code that creates a variable called pi and sets it to an appropriate value.
- pi = 3.14159265359

# 5. Why does this code not work?
- Python ist Case-sensitive: Die ausgegebene Variable entspricht nicht der Deklarierten

# 6. All of the variable names below can be used. But which ONE of these is the better variable name to use?
- area (Sollte mit kleinem Buchstaben beginnen, kein Leerzeichen, Nicht Uppercase -> Konstante)

# 7. Which of these variables names are not allowed in Python? (More than one might be wrong. Also, this question is not asking about improper names, just names that aren't allowed. Test them if you aren't sure.)
- 1Apple
- account number
- account.number
- account#
- PI (Konstante)
- great.big.variable
- 2x
- total%
- #left

# 8. Why does this code not work?
- a ist nicht deklariert und der Variable wurde nch der Ausgabe erst ein Wert zugewiesen

# 9. Explain the mistake in this code:
- pi wird auf float geparst

# 10. This program runs, but the code still could be better. Explain what is wrong with the code.
- x Variable weglassen und den Wert gleich pi zuweisen

# 11. Explain the mistake in the following code:
- Evtl. Klammersetzung

# 12. Explain the mistake in the following code:
- a = 3(x + y) -> Operator fehlt oder Tippfehler

# 13. Explain the mistake in the following code:
- Input & Float müssen vertauscht werden -> Strin in float konvertiert

# 14. Do all these print the same value? Which one is better to use and why?
- Ja, sie geben alle das selbe aus.
- Style guide besagt das vor und nach Operator ein Leerzeichen sein sollte.

# 15. What is a constant?
- Eine Variable, welche nach der Deklaration nicht mehr verändert werden kann.

# 16. How are variable names for constants different than other variable names?
- Konstanten werden ausschließlich uppercase deklariert

# 17. What is a single quote and what is a double quote? Give and label an example of both.
- "You've" -> Double quotes, da single quotes ein Bestandteil des Textes sind.
- 'Your' -> String literal: Kein single quote in Text enthalten

# 18. Write a Python program that will use escape codes to print a double-quote and a new line using the Window's standard. (Note: I'm asking for the Window's standard here. Look it up out of Chapter 1.)
- print(" \" \n")

# 19. Can a Python program print text to the screen using single quotes instead of double quotes?
- Ja

# 20. Why does this code not calculate the average?
- print(3 + 4 + 5 / 3) -> Flasche Klammersetzung -> print((3 + 4 + 5) / 3)

# 21. What is an ``operator'' in Python?
- Ein Operator ist ein mathematisches Zeichen wie beispielsweise:
    - "+"
    - "-"
    - "*"
    - "/"
    - "//"

# 22. What does the following program print out?
- 3

# 23. Correct the following code:
- user_name = input("Enter your name: )" -> user_name = input("Enter your name: ")

# 24. Correct the following code:
- value = int(input(print("Enter your age"))) -> value = int(input("Enter your age"))
print(value)
