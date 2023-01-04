with open("input.txt") as f:
    l = 0
    r = 0
    for line in f:
        if line[0] == 'R':
            r += 1
        if line[0] == 'L':
            l += 1

print(r)
print(l)
        