# Start of the function
def percent(marks):  # function can also contain null value e.g. percent()
    return (sum(marks)/400)*100
# End of the function


marks1 = [45, 46, 76, 77]
percentage1 = percent(marks1)

marks2 = [65, 85, 84, 40]
percentage2 = percent(marks2)

print(percentage1, percentage2)
