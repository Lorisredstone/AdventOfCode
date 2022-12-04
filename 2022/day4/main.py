file = [x.split("\n")[0] for x in open("input.txt", "r").readlines()]

total_part_1 = 0
total_part_2 = 0
for line in file:
    range1 = line.split(",")[0]
    range2 = line.split(",")[1]
    values_1 = range(int(range1.split("-")[0]), int(range1.split("-")[1])+1)
    values_2 = range(int(range2.split("-")[0]), int(range2.split("-")[1])+1)
    if all(x in values_1 for x in values_2) or all(x in values_2 for x in values_1):
        total_part_1 += 1
    if any(x in values_1 for x in values_2) or any(x in values_2 for x in values_1):
        total_part_2 += 1
        
print(f"Part 1 : {total_part_1}")
print(f"Part 2 : {total_part_2}")
    
