file = open("input.txt", "r").read()
add = sum(a == "(" for a in file)
remove = sum(a == ")" for a in file)
print(f"Part 1 : {add - remove}")

floor = 0
for i, a in enumerate(file):
    if a == "(":
        floor += 1
    else:
        floor -= 1
    if floor == -1:
        print(f"Part 2 : {i + 1}")
        break