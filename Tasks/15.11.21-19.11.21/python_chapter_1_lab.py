# 1.1 Part A
temp_fahrenheit = float(input("Enter temperature in Fahrenheit: "))
temp_celsius = 0

temp_celsius = (temp_fahrenheit - 32) * (5 / 9)

print("The temperature in Celsius: ", temp_celsius)

# 1.2 Part B
height = int(input("Enter the height of the trapezoid: "))
length_bottom = int(input("Enter the length of the bottom base: "))
length_top = int(input("Enter the length of the top base: "))
area = ((length_bottom + length_top) / 2) * height

print(area)

# 1.3 Part C
# Kreis Flächeninhalt
pi = 3.14
r = int(input("Enter the radius of the circle: "))
print("----------------------------------")

area = pi * (r ** 2)

print("The area of the circle is:", area)