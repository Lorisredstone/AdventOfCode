file = open("input.txt", "r").read()

# import md5
from hashlib import md5

print(md5(file.encode()).hexdigest())

for i in range(1000000000):
    if md5(f"{file}{i}".encode()).hexdigest()[:5] == "00000":
        print(f"part 1: {i}")
        break

for i in range(1000000000):
    if md5(f"{file}{i}".encode()).hexdigest()[:6] == "000000":
        print(f"part 2: {i}")
        break