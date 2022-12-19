import re

def instruct(arr, n, x, y):
    n = int(n)
    x = int(x)
    y = int(y)
    
    x = x-1 
    y = y-1
    
    moving = []
    
    # remove n elements from x
    for i in range(n):
        moving.append(arr[x].pop())
    
    
    # Put back in correct order
    for i in range(len(moving)):
        arr[y].append(moving[i]) 


boxes = []
horizontal_boxes = []
vertical_boxes = []

with open("input.txt", "r") as f:
    for i in range(0, 8):
        boxes.append(f.readline())
        
    for i in range(len(boxes)):
        boxes[i] = f"{boxes[i][0:-1]} "

    index = 0
    for box in boxes:
        horizontal_boxes.append([])
        for i in range(0, len(box) - 2, 4):
            string = box[i:i+4]
            horizontal_boxes[index].append(string.strip())
        index += 1

    vertical_boxes = [[] for x in range(0, 9)]
    
    for i in range(9):
        for j in range(8):
            vertical_boxes[i].append(horizontal_boxes[j][i])
        vertical_boxes[i] = vertical_boxes[i][::-1]

    for i in range(9):
        while '' in vertical_boxes[i]:
            vertical_boxes[i].remove('')
            
    # read instructions.
    # all instructions start with m...
    print('---')
    for line in vertical_boxes:
        print(line)
    
    for line in f:
        if line[0] == 'm':
            instructions = re.findall('[0-9]+', line)
            n, x, y = instructions
            instruct(vertical_boxes, n, x, y)

    
    result = []
    print(())
    for line in vertical_boxes:
        result.append(line[-1])
    
    print(result)
    
    