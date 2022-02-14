# 1.
'''
x = 0
while x < 10:
    print(x)
    x = x + 2

# 0
# 2
# 4
# 6
# 8
'''

# 2.
'''
x = 1
while x < 64:
    print(x)
    x = x * 2

# 1
# 2
# 4
# 8
# 16
# 32
'''

# 3.
'''
x = 0
while x < 10 and x >= 0:
    print(x)
    x = x + 2

# x is already 0 and will always be bigger then 0
'''

# 4.
'''
x = 5
while x >= 0:
    print(x)
    if x == "1":
        print("Blast off!")
    x = x - 1

# Counting from 5 to 0 and not printing "Blast off!" because 1 != "1"
'''

# 5.
'''
x = float(input("Enter a number greater than zero: "))
 
if x <= 0:
    print("Too small. Enter a number greater than zero: ")
'''

# 6.
'''
x = 10
 
while x >= 0:
    print(x)
    x = x - 1
 
print("Blast-off")
'''

# 7.
'''
for i in range(10):
    print(i)
    i += 1

# i dose not to be declared, because it will be in range of 10 declared
'''

# 8.
'''
# Sample 1
x = 0
for i in range(10):
    x += 1
for j in range(10):
    x += 1
print(x)
 
# Sample 2
x = 0
for i in range(10):
    x += 1
    for j in range(10):
        x += 1
print(x)

# In sample 2 the second for-loop is inside the first one
'''