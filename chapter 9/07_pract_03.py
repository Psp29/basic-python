
for i in range(2, 21):
    with open(f"tables/table_of_{i}.txt", 'w') as w:
        for j in range(1, 11):
            w.write(f"{i} X {j} = {i*j}\n")
