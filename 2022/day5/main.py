file = [x.split("\n")[0] for x in open("input.txt", "r").readlines()]

"""
[V]     [B]                     [C]
[C]     [N] [G]         [W]     [P]
[W]     [C] [Q] [S]     [C]     [M]
[L]     [W] [B] [Z]     [F] [S] [V]
[R]     [G] [H] [F] [P] [V] [M] [T]
[M] [L] [R] [D] [L] [N] [P] [D] [W]
[F] [Q] [S] [C] [G] [G] [Z] [P] [N]
[Q] [D] [P] [L] [V] [D] [D] [C] [Z]
 1   2   3   4   5   6   7   8   9 
"""

list_stacks_part_1 = [[], [], [], [], [], [], [], [], []]
list_stacks_part_2 = [[], [], [], [], [], [], [], [], []]
stack = 0
for line in file[:8]:
    for x in line.split(" "):
        if x != "[0]":
            list_stacks_part_1[stack].append(x.split("[")[1].split("]")[0])
            list_stacks_part_2[stack].append(x.split("[")[1].split("]")[0])
        stack += 1
        stack %= 9
for i in range(len(list_stacks_part_1)):
    list_stacks_part_1[i] = list_stacks_part_1[i][::-1]
    list_stacks_part_2[i] = list_stacks_part_2[i][::-1]
for line in file[10:]:
    number = line.split(" ")[1]
    from_nb = line.split(" ")[3]
    to_nb = line.split(" ")[5]
    for _ in range(int(number)):
        list_stacks_part_1[int(to_nb) - 1].append(list_stacks_part_1[int(from_nb) - 1].pop())
        list_stacks_part_2[int(to_nb) - 1].append(list_stacks_part_2[int(from_nb) - 1].pop())
    # now we change the order of list_stack_part_2
    temp_stack = []
    for x in range(int(number)):
        temp_stack.append(list_stacks_part_2[int(to_nb)-1][len(list_stacks_part_2[int(to_nb)-1])-x-1])
    for _ in range(int(number)):
        list_stacks_part_2[int(to_nb)-1].pop()
    for x in temp_stack:
        list_stacks_part_2[int(to_nb)-1].append(x)
part1 = ""
for stack in list_stacks_part_1:
    part1 += stack.pop()
print(f"Part 1: {part1}")
part2 = ""
for stack in list_stacks_part_2:
    part2 += stack.pop()
print(f"Part 1: {part2}")
