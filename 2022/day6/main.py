file = open("input.txt", "r").read()

for x in range(0, len(file)-5):
    marker = file[x:x+3]
    if len(set(marker + file[x+3])) == 4:
        print(f"Part 1: {x+3}")
        break
    
for x in range(0, len(file)-15):
    marker = file[x:x+13]
    if len(set(marker + file[x+13])) == 14:
        print(f"Part 1: {x+14}")
        break