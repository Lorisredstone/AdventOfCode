file = open("input.txt", "r")

liste = []
for elf in "".join(file.readlines()).split("\n\n"):
    total = sum(int(nb) for nb in elf.split("\n"))
    liste.append(total)

# Part 1
print(f"Part 1 : {max(liste)}")

# Part 2
new_liste = sorted(liste)
print(f"Part 2 : {sum(new_liste[::-1][:3])}") 