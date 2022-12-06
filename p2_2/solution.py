def main():
    print(solution("input.txt"))



def solution(Input):
    
    # VARIABLES
    result_points = 0
    hand_points = 0
    
    # DICTS/MAPS
    # This maps the 2nd char to the points
    result = {
        "X": 0,
        "Y": 3,
        "Z": 6
    }
    
    # This maps which hand we have to play 
    # with the points we will receive from that 
    # hand
    #
    # ie B X
    # They hands[i][j]
    # hands["B"]["X"] = 1
    # hand_points += hands[i][j]
    hands = {
        "A": {
            "X": 3,
            "Y": 1,
            "Z": 2
        },
        
        "B": {
            "X": 1,
            "Y": 2,
            "Z": 3
        },
        
        "C": {
            "X": 2,
            "Y": 3,
            "Z": 1
        }
        
    } 
    
    
    with open(Input) as input:
        for line in input:
            
            # Clean white space 
            # assign characters to i and j
            _ = line.strip()
            i,j = _.split(' ')
            j = j.strip()
            
            result_points += result[j]
            hand_points += hands[i][j]
            
                
    total = result_points + hand_points
    
    return(total)
    # Result = 15702


if __name__ == '__main__':
    main()