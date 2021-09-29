sub1 = int(input("Enter marks of Maths: "))
sub2 = int(input("Enter marks of Physics: "))
sub3 = int(input("Enter marks of Chemistry: "))

if(sub1 <= 100 and sub2 <= 100 and sub3 <= 100):
    if(sub1 < 33 or sub2 < 33 or sub3 < 33):
        print(
            "You are failed, because you have less than 33 marks in one of the subject :(")
    elif(sub1+sub2+sub3)/3 < 40:
        print("You are failed, because of total percentage is less than 40 :(")
    else:
        print("Congratulations! You have passed the exams :)")

else:
    print("Warning: 'Marks cannot be greater than 100!!'")
