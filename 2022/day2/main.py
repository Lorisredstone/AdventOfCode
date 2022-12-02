file = open("input.txt", "r").readlines()

scorepart1 = 0
for line in file:
    if line == "A X\n": scorepart1 += 1 + 3
    if line == "A Y\n": scorepart1 += 2 + 6
    if line == "A Z\n": scorepart1 += 3 + 0
    if line == "B X\n": scorepart1 += 1 + 0
    if line == "B Y\n": scorepart1 += 2 + 3
    if line == "B Z\n": scorepart1 += 3 + 6
    if line == "C X\n": scorepart1 += 1 + 6
    if line == "C Y\n": scorepart1 += 2 + 0
    if line == "C Z\n": scorepart1 += 3 + 3
print(scorepart1)

scorepart2 = 0
for line in file:
    if line == "A X\n": scorepart2 += 0 + 3
    if line == "A Y\n": scorepart2 += 3 + 1
    if line == "A Z\n": scorepart2 += 6 + 2
    if line == "B X\n": scorepart2 += 0 + 1
    if line == "B Y\n": scorepart2 += 3 + 2
    if line == "B Z\n": scorepart2 += 6 + 3
    if line == "C X\n": scorepart2 += 0 + 2
    if line == "C Y\n": scorepart2 += 3 + 3
    if line == "C Z\n": scorepart2 += 6 + 1
print(scorepart2)