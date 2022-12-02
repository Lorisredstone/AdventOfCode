file = open("input.txt", "r").read()

from dataclasses import dataclass

@dataclass
class House:
    x:int
    y:int
    
    def __hash__(self):
        return hash((self.x, self.y))

visited_houses = set()
current_coords = [0,0]

for char in file:
    if char == "^":
        current_coords[1] += 1
    elif char == "v":
        current_coords[1] -= 1
    elif char == ">":
        current_coords[0] += 1
    elif char == "<":
        current_coords[0] -= 1
    visited_houses.add(House(current_coords[0], current_coords[1]))
print(f"part 1 : {len(visited_houses)}")

visited_houses = set()
current_coords = [[0,0], [0,0]]
for i, char in enumerate(file):
    if char == "^":
        current_coords[i%2 != 0][1] += 1
    elif char == "v":
        current_coords[i%2 != 0][1] -= 1
    elif char == ">":
        current_coords[i%2 != 0][0] += 1
    elif char =="<":
        current_coords[i%2 != 0][0] -= 1
    visited_houses.add(House(current_coords[i%2 != 0][0], current_coords[i%2 != 0][1]))

print(len(visited_houses))