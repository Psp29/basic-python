# For hollow square
num = int(input("Enter no. of rows and columns: "))
print("Hollow square: ")
for i in range(num):    # For rows
    for j in range(num):    # For columns
        if(i == 0 or i == num-1 or j == 0 or j == num-1):
            print("@", end=" ")
        else:
            print(" ", end=" ")
    print()

# For Hollow rectangle
row = int(input("Please enter number of rows: "))
column = int(input("Please enter number of columns: "))
print("Hollow Rectangle with", row, "rows and", column, "columns: ")
for a in range(row):
    for b in range(column):
        if(a == 0 or a == row-1 or b == 0 or b == column-1):
            print("#", end=" ")
        else:
            print(" ", end=" ")
    print()
