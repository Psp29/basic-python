# important note: To read and write a binary file you have to use 'rb' to read a binary file and 'rt' to read a text file. Default is text.

# reading a file
r = open("sample.txt", 'r')  # 'r' is for read mode
# if we donot specify r or w it consider it as 'r' (read mode)
r = open("sample.txt")
# data = r.read()   # it is compulsory to read only once.
data = r.read(3)    # It will print first 3 characters
print(data)
r.close()
