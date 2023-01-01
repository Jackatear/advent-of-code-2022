
with open("input.txt") as f:
    lines = []
    for line in f:
        if '\n' in line:
            lines.append(line[:-1])
        else:
            lines.append(line)
    
def edge_trees(arr):
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if i == 0:
                arr[i][j] = '1';
            if i == len(arr) - 1:
                arr[i][j] = '1';
            if j == 0: 
                arr[i][j] = '1';
            if j == len(arr[i]) - 1:
                arr[i][j] = '1';
                
def left_trees(arr, i, j):
    return arr[i][:j]

def right_trees(arr, i, j):
    return arr[i][j+1:]
    
def above_trees(arr, i, j):
    l = []
    for n in range(i):
        l.append(arr[n][j])
    return l
        
def below_trees(arr, i, j):
    l = []
    for n in range(i, len(arr)):
        l.append(arr[n][j])
    return l[1:]
        
def trees_around(tree, up, down, left, right):
    if tree > max(up):
        return True
    if tree > max(down):
        return True
    if tree > max(left):
        return True
    if tree > max(right):
        return True
    return False
    
            
        
# Make 2d array of all trees from input file
trees = [[] for x in range(len(lines))]   
row = 0
for line in lines:
    for tree in line:
        trees[row].append(tree)
    row += 1

# Make another 2d array where 1 means we can see the tree and 0 means we can't
visible_trees = [[] for x in range(len(lines))]   
row = 0
for line in lines:
    for tree in line:
        visible_trees[row].append('0')
    row += 1

# Make all outside trees visible
edge_trees(visible_trees)

for i in range(len(trees)):
    for j in range(len(trees[i])):
        size = trees[i][j]
        
        # LEFT
        left = left_trees(trees, i, j)
        
        # RIGHT
        if j != len(trees[i]) - 1:
            right = right_trees(trees, i, j)
 
        # ABOVE
        if i > 0:
            up = above_trees(trees, i, j)
        
        # BELOW
        if i < len(trees[i]) - 1:
            down = below_trees(trees, i, j)
        
            
        if visible_trees[i][j] != '1':
            if trees_around(trees[i][j], up, down, left, right):
                visible_trees[i][j] = '1'
    
sum = 0
for line in visible_trees:
    for n in line:
        sum += int(n)
        
print(sum)