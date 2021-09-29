# file1 = "log.txt"   # Files are not identical
file1 = "this.txt"  # Files are identical
file2 = "copy_of_this.txt"

with open(file1) as f:
    f1 = f.read()

with open(file2) as f:
    f2 = f.read()

if f1 == f2:
    print("Files are identical.")
else:
    print("Files are not identical.")
