def main():
    print(solution('input.txt'))
    

def solution(Input):
    
    # 1 read file,
    # each line, calculate the score figure
    # then calculate the figure your hand gives you 
    # keep adding them up until the end  
    
    hand = {"A": 1,
            "B": 2,
            "C": 3,
            "X": 1,
            "Y": 2,
            "Z": 3}
    
    # They play "A" (rock), I win with "Y" (paper)...
    win = {"A": "Y", "B": "Z", "C": "X"}
    
    hand_score = 0
    win_score = 0
    total_score = 0
    
    with open(Input) as input:
        for line in input:
            i, j = line.split(' ')
            j = j.strip()
            i = i.strip()
            hand_score += hand[j]
            if win[i] == j:
                win_score += 6
            elif hand[i] == hand[j]:
                win_score += 3
            else:
                win_score += 0

    total_score = hand_score + win_score
    
    return total_score
    
if __name__ == '__main__':
    main()