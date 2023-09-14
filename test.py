import sys

def text2Array(string):
    lines = string.split()
    tree = []
    for line in lines:
        row = [int(num) for num in line]
        tree.append(row)
    return tree
    
def ICU(tree, row, col):
    value = tree[row][col]
    right = tree[row][col+1:]
    left = tree[row][:col]
    up = [r[col] for r in tree[:row]]
    down = [r[col] for r in tree[row+1:]]
    isRightMax = all(value > r for r in right)
    isLeftMax = all(value > l for l in left)
    isUpMax = all(value > u for u in up)
    isDownMax = all(value > d for d in down)
    if row == 0 or col == 0 or row+1 == len(tree) or col+1 == len(tree[0]):
        return True
    elif isRightMax or isLeftMax or isUpMax or isDownMax:
        return True
    return False

i = 0
inputFile = sys.argv[1]
with open(inputFile, 'r') as file:
    text = file.read()
    tree = text2Array(text)
    for row in range(len(tree)):
        for col in range(len(tree[0])):
            result = ICU(tree, row, col)
            if result:
                i += 1
print(i)  

