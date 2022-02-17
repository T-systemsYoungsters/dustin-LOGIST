# 1.
'''
# 1.a. String 
exampleString = "String"
# 1.b.Integer
exampleInteger = 1
# 1.c. Floating point
exampleFloatingPoint = 1.3
# 1.d. Boolean Example:
exampleBoolean = True
'''

# 2.
'''
my_list = [5, 2, 6, 8, 101]
print(my_list[1]) # index of value 2
print(my_list[4]) # index of value 101
print(my_list[5]) # index does not exist
'''

# 3.
'''
# Is looping throug array and prints the values
my_list=[5, 2, 6, 8, 101]
for my_item in my_list:
    print(my_item)
'''

# 4.
'''
my_list1 = [5, 2, 6, 8, 101]
my_list2 = (5, 2, 6, 8, 101)
my_list1[3] = 10 # Changing value in array with index 3
print(my_list1) # Prints the array with updated value of index 3
my_list2[2] = 10 # Is actually not working, because my_list2 is no array
print(my_list2) # Error, because my_list2 is no array
'''

# 5.
'''
my_list = [3 * 5] # Adding value 15 to array
print(my_list) # Printing array
my_list = [3] * 5 # Pushing the existing value by 5 times
print(my_list) # Printing array
'''

# 6.
'''
# Adding value 5 to the array
# Adding the itterator to the array
my_list = [5]
for i in range(5):
    my_list.append(i)
print(my_list)
'''

# 7.
'''
print(len("Hi")) # Printing length of string (Amount of characters)
print(len("Hi there.")) # Printing length of string (Amount of characters)
print(len("Hi") + len("there.")) # Printing length of string (Amount of characters)
print(len("2")) # Printing length of string (Amount of characters)
print(len(2)) # Has no length
'''

# 8.
'''
print("Simpson" + "College") # Printing string
print("Simpson" + "College"[1]) # Printing just first part, because second is invalid
print( ("Simpson" + "College")[1] ) # Interprets the string as array and gives back the value of index 1
'''

# 9.
'''
# Interprets the string as array and is looping through it and printing each value
word = "Simpson"
for letter in word:
    print(letter)
'''

# 10.
'''
# Printing three times word & and is adding the string "College" to it when itterating
word = "Simpson"
for i in range(3):
    word += "College"
print(word)
'''

# 11.
'''
# Word is "HiHiHi"
word = "Hi" * 3
print(word)
'''

# 12.
'''
my_text = "The quick brown fox jumped over the lazy dogs."
print("The 3rd spot is: " + my_text[3]) # Is getting the value with the index 3 (" " => empty string)
print("The -1 spot is: " + my_text[-1]) # Is getting the last index of my_text
'''

# 13.
'''
s = "0123456789"
print(s[1]) # Printing value with index 1
print(s[:3]) # Printing values with indexes up to 2
print(s[3:]) # Printing values beginning from index including 4
'''

# 14.
'''
list = []
num = int(input("Enter the size of the array: "))

print("Enter numbers: ")

for n in range(num):
  numbers = int(input())
  list.append(numbers)

print(list)
'''

# 15.
'''
list = [3,12,3,5,3,4,6,8,5,3,5,6,3,2,4]
listLength = len(list)
listSum = 0
listAverage = 0

for i in range(0, listLength):
    listSum += list[i]

listAverage = listSum / listLength
print(listAverage)
'''