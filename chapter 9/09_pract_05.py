words = ["bich", "nibba", "timba"]
with open("sample.txt") as f:
    content = f.read().lower()  # converts all found string words in lowercase

for word in words:
    content = content.replace(word, "#be@ep#")

    with open("sample.txt", 'w') as f:
        f.write(content)
