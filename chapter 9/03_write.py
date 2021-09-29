# write mode:- it will overwrite the whole file
f = open('another.txt', 'w')
f.write("Please write this line to the file\n")
f.write("Please write this line to the file\n")
f.write("Please write this line to the file\n")
f.write("Please write this line to the file\n")
f.close

# Append mode:- It will append/add the lines at the end of the file.
# f = open('another.txt', 'a')
# f.write(" i am appending.")
# f.close
