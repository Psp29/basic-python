# Write a program to take 4 numbers from user and print the greatest number.

num1 = int(input("Enter number 1: "))
num2 = int(input("Enter number 2: "))
num3 = int(input("Enter number 3: "))
num4 = int(input("Enter number 4: "))

if(num1 > num4):
    g1 = num1
else:
    g1 = num4

if(num2 > num3):
    g2 = num2
else:
    g2 = num3

if(g1 > g2):
    print(str(g1), "is greatest")
else:
    print(str(g1), "is greatest")
