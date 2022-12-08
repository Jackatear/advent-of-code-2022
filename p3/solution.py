def main():
    print(solution('input.txt'))

def solution(input_file):
    priority_string = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    priority_list = list(priority_string)
    
    with open(input_file) as input:
        priority_sum = 0
        
        for line in input:
            length = len(line)
            mid = length/2
            first_compartment = line[0:mid]
            second_compartment = line[mid::]
            
            #remove whitespace at end of line
            second_compartment = second_compartment.strip()
            
            # if we make a compartment into a set, we have some functions that can help
            # the intersection method returns to us the common items between the two data sets
            common_item = list(set(first_compartment).intersection(second_compartment))
            
            
            # add the indexes up (+1 since its 0 indexed)
            _ = (priority_list.index(common_item[0])) + 1
            priority_sum += _
            
    return priority_sum
            
            
            
            
        
if __name__ == '__main__':
    main()