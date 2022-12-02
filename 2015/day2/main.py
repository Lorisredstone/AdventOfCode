file = open("input.txt", "r").readlines()

grand_total = 0
for box in file:
    l, w, h = box.split("x")
    l, w, h = int(l), int(w), int(h)
    total = 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)
    grand_total += total
print(f"Part 1 : {grand_total}")

grand_total = 0
for box in file:
    l, w, h = box.split("x")
    l, w, h = int(l), int(w), int(h)
    total = 2*(l+w+h-max(l, w, h)) + l*w*h
    grand_total += total
print(f"Part 2 : {grand_total}")