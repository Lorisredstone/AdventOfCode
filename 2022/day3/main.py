file = [x.split("\n")[0] for x in open("input.txt", "r").readlines()]

def get_priority(char:str) -> int:
    if char.islower():
        return "abcdefghijklmnopqrstuvwxyz".index(char) + 1
    else:
        return "ABCDEFGHIJKLMNOPQRSTUVWXYZ".index(char) + 26 + 1

total = 0
for sack in file:
    compartiment1 = sack[:int(len(sack)/2)]
    compartiment2 = sack[int(len(sack)/2):]
    priority = 0
    list_same_items = set(compartiment1).intersection(compartiment2)
    for item in list_same_items:
        priority += get_priority(item)
    total += priority

print(f"Part 1 : {total}")

total = 0
for i in range(0, len(file)-1, 3):
    elf1 = file[i]
    elf2 = file[i+1]
    elf3 = file[i+2]
    common = set(elf1).intersection(elf2).intersection(elf3)
    total += get_priority(max(common))
print(f"Part 2 : {total}")