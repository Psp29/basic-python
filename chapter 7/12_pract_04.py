num = int(input("Enter any number: "))
prime = False

for i in range(2, num):
    if(num % i == 0):
        prime = False
        break

if prime:
    print("This number is Prime")
else:
    print("This number is not Prime")
