import re

# This checks if everything in the whole value list is a number
def can_calculate(dictionary, key):
    check = True

    for value in dictionary[key]:
        if not value.isnumeric():
            return False
    return check


# if can_calculate == true, we can run this function to add all the values up:
def calculate(dictionary, key):
    sum = 0
    
    if len(dictionary[key]) == 1:
        sum = dictionary[key][0];
        return str(sum)
    else:
        for item in dictionary[key]:
            sum += int(item)
    return str(sum)
            

with open("input.txt") as f:
    
    directories = {}
    
    current_directory_list = []

    for line in f:
        
        new_directory = re.search(r'cd [\/a-zA-Z0-9]+', line)
        trace_back = re.search(r'cd \.\.', line)
        
        if trace_back:
            current_directory_list = current_directory_list[:-1]

        if new_directory:
            _, name = new_directory.group(0).split(' ')
           
            current_directory_list.append(name)
            
            if len(current_directory_list) > 1:
                current_directory_tuple = tuple(current_directory_list)
            else:
                current_directory_tuple = name
            
            if current_directory_tuple not in directories:
                directories[current_directory_tuple] = []
        
        if (line[0].isdigit()):
            mem, key = line.split(' ')
            directories[current_directory_tuple].append(mem)
            
        if (line[0] == 'd'):
            x, y =line.split(' ')
            directories[current_directory_tuple].append(y[:-1])

    
    x = 0
    while True:
        passed = directories.copy()
        curr_item = ''
        check_inside = []
    
        for key in directories:
            
            # Check through the dictrionary for lists which are all numeric 
            # if they are, we can add them up 
            # and return a string of their value
            if isinstance(directories[key], list):
                if can_calculate(directories, key):
                    directories[key] = calculate(directories, key)
                else:
                    
                    # We need to replace the 'directories' from the value list with their contents
                    # so the contents are all numbers
                    for item in directories[key]:
                        if not item.isnumeric():
                            curr_item = item
                            
                            check_inside = list(key)
                            check_inside.append(item)
                            if can_calculate(directories, tuple(check_inside)):
                                directories[key].remove(curr_item)
                                if isinstance(directories[tuple(check_inside)], list):
                                    directories[key].append(calculate(directories,  tuple(check_inside)))
                                else:
                                    directories[key].append(directories[tuple(check_inside)])

        # Check whether the dictionary has changed after two iterations
        # If it hasn't we can break the loop
        dif = 0
        for line in directories:
            if directories[line] != passed[line]:
                dif = 1
        if dif == 0:
            break
        
    # PART TWO #
    c = 0
    for line in directories:
        if c > 0:
            break
        total_space_used = int(directories[line])
        c += 1
    
    total_space = 70000000
    total_space_needed = 30000000
    current_space_left = total_space - total_space_used
    dif = total_space_needed - current_space_left
    
    potential = []
    
    for line in directories:
        if int(directories[line]) >= dif:
            potential.append(int(directories[line]))
    
    print(min(potential))
    
   
        

        
    
    

            