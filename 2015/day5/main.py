file = open("input.txt", "r").readlines()

def isnice(s:str) -> int:
    voyels_number = sum(s.count(voyel) for voyel in "aeiou")
    double_letter = sum(s.count(letter*2) for letter in "abcdefghijklmnopqrstuvwxyz")
    bad_string = sum(s.count(bad) for bad in ["ab", "cd", "pq", "xy"])
    if voyels_number >= 3 and double_letter >= 1 and bad_string == 0:
        return 1
    return 0


total = sum(isnice(string.split("\n")[0]) for string in file)
print(f"part 1: {total}")

def isreallynice(s:str) -> int:
    repeated_letter = sum(s[i] == s[i+2] for i in range(len(s)-2))
    pair_no_overlap = sum(s[i:i+2] in s[i+2:] for i in range(len(s)-1))
    return 1 if repeated_letter and pair_no_overlap else 0
    

total = sum(isreallynice(string.split("\n")[0]) for string in file)
print(f"part 2: {total}")