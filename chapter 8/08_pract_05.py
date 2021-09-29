def remove_and_split(string, word):
    # Here we replaced the word with the blank or empty value
    newStr = string.replace(word, "")
    # strip is an in built function which removes extra spaces from start and end of the string.
    return newStr.strip()


this = "       jo mama      "
n = remove_and_split(this, "mama")
print(n)
