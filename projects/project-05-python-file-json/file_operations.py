f = open("notes.txt", "r")
print(f.read())

with open("notes.txt", "r") as file:
    for names in file:
        data = names.strip().split(",")
        print(f"Technology: {data[0]} | Category: {data[1]}")
        