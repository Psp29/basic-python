username = input("Please enter a username: ")
userlen = len(username)
if userlen < 10:
    print("Entered Username contains less than 10 characters!!")
elif userlen == 10:
    print("Entered Username contains exactly 10 characters.")
else:
    print("Entered Username contains more than 10 characters.")
