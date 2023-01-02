def strip(list, size):
    el = 0
    counter = 0
    print(size)
    for x in list:
        if int(x) >= size:
            el = counter
            return list[:el+1]
        counter += 1
    if el > 0:
        return list[:el+1]
    return list
        
trees = ['5', '1', '2']
size = 5

print(strip(trees, size))