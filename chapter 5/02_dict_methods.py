myDict1 = {
    "Key": "value",
    "Prasad": "A Dickhead",
    "Marks": [9, 9, 10, 8, 6, 9, 5],
    "anotherDict": {'Prasad': 'Hero'}
}

# print(myDict1.keys())   # Prints the keys of the dictionary
# print(myDict1.values()) # Prints the values of the dictionary
# print(myDict1.items())  # Prints the content inside the Dictionary
# print(list(myDict1.keys())) # changest the type to 'list'

# Updating the dictionary by adding the key:value pairs
updateDict1 = {
    'Piyush': "Friend",
    'Ankush': 'Friend',
    "Prasad": "A Genius"
}
myDict1.update(updateDict1)
print(myDict1)

# get method
print(myDict1["Prasad"])  # Prints the value associated with key "Prasad"
print(myDict1.get("Prasad"))  # Prints the value associated with key "Prasad"

# Difference between .get and [] syntax in dictionaries.
# print(myDict1["Prasad69"])    # Throws an error (KeyError) as Prasad69 is not present in the dictionary
print(myDict1.get("Prasad69"))  # Returns None instead of throwing an error.
