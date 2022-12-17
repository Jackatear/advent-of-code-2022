# # 1 - read the input file 

# # 2 - each three lines is a new 'group'

# # 3 - create an array that will hold each of the common items

# --> array = ['r', 'T', 's']...
# -- where element one represents the first group etc...

# then find the priority number by comparing it to our alphabet array. 


priority_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

with open("input.txt") as input:
    line_count = 3;
    line_reader = []
    chunked = []
    items = []
    for line in input:
        line_reader.append(line[:-1])
        
    group = 0
    i = 0
    while True:
        _ = line_reader[group:group+4]
        chunked.append(_)
        group += 3
        i += 1
        if len(chunked) == (len(line_reader)/3):
            break
    
    # Now look through chunked array for each common item 
    for group in chunked:
        p1 = group[0]
        p2 = group[1]
        p3 = group[2]
        
        p1 = set(p1)
        p2 = set(p2)
        p3 = set(p3)
        
        done = 0
        # find longest 
        longest = max(len(p1), len(p2), len(p3))
        
        if len(p1) == longest and done == 0:
            for item in p1:
                if item in p2 and item in p3:
                    items.append(item)
                    done += 1
                    
        if len(p2) == longest and done == 0:
            for item in p2:
                if item in p1 and item in p3:
                    items.append(item)
                    done += 1
                    
        if len(p3) == longest and done == 0:
            for item in p3:
                if item in p1 and item in p2:
                    items.append(item)
                    done += 1
                    
    for i in range(len(items)):
        _ = priority_string.index(items[i]);
        items[i] = _ + 1
        
        
    print(len(chunked))
    print(len(line_reader))
    print(len(items))
    sum = 0
    
    for n in items:
        sum += n
        
    print(sum)
        
            
        
        
        
    