counter = 0

with open("input.txt") as input:
    for line in input:
        first, second = line.split(',')
        first = first.split('-')
        second = second.split('-')
        
        firstRange = [x for x in range(int(first[0]), int(first[1]) + 1)]
        secondRange = [x for x in range(int(second[0]), int(second[1]) + 1)]
            
        for x in firstRange:
            if x in secondRange: 
                counter = counter + 1
                break
          
    print(counter)
        
        