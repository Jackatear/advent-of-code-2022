def main():
        print(calorie_counter('input.txt'))

def calorie_counter(file):
    
    elf_dict = {}
    el = 1
    
    # Iterate through the input file that has been provided.
    # Assign each block as a key in the dict. This key is the elf and the value is the total cals they're carrying 
    with open(file) as input:
        
        # if not a digit, its a new elf so create a new key/elf in the dict
        for line in input:
            if not line[0].isdigit():
                el += 1
            else:
                if el not in elf_dict:
                    elf_dict[el] = 0
                elf_dict[el] += int(line)
                
                   
    # Find the largest value
    max_elf = max(elf_dict, key=elf_dict.get)   
    return f"Elf {max_elf} has {elf_dict[max_elf]} calories"


if __name__ == '__main__':
    main()