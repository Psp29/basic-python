r = open("sample.txt")

# Reads and prints first line
data = r.readline()
print(data)

# Reads and prints second line
data = r.readline()
print(data)

# Reads and prints third line and so on...
data = r.readline()
print(data)
r.close()
