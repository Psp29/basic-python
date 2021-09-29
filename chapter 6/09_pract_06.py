marks = int(input("Enter your percentage: "))

if marks <= 100:
    if marks >= 90:
        grade = 'Ex'
    elif marks >= 80:
        grade = 'A'
    elif marks >= 70:
        grade = 'B'
    elif marks >= 60:
        grade = 'C'
    elif marks >= 50:
        grade = 'D'
    else:
        grade = 'F'
    print("Your grade is:", grade)
else:
    print("Percentage cannot exceed 100!!!")
