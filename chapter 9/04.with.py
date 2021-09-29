# Using 'with' we do not have to use close()
with open('another.txt', 'r') as f:
    a = f.read()
with open('another.txt', 'w') as f:
    a = f.write("updated")
