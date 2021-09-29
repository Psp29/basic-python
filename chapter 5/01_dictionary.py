# Dictionary is unordered
# Dictionary is Mutable
# Dictionary is indexed
# Dictionary cannot contain more than one keys if we try to use more than one key then the previous key will be overwrited.


myDict1 = {
    "Key": "value",  # A simple key value pair
    "Prasad": "A Dickhead",
    # Wen can store any datatype as a value in a dictionary.
    "Marks": [9, 9, 10, 8, 6, 9, 5],
    # DictCeption (Basically we can store a dictionary inside or as a value inside a dictionary) also known as 'Nested Dictionary'
    "anotherDict": {'Prasad': 'Hero'}
}

# Prints the value of the speccified key in the dictionary
print(myDict1["Key"])
print(myDict1["Prasad"])
print(myDict1["Marks"])  # Before changing the dictionary

myDict1['Marks'] = [69, 420]    # Changing the values in a Dictionary

print(myDict1["Marks"])  # After changing the dictionary
print(myDict1["anotherDict"])   # Prints the dictionary
# Prints value of the dictionary inside the dictionary
print(myDict1["anotherDict"]["Prasad"])
