xSize = 0
ySize = 1

with open('day8_input.txt') as f:
    xSize = len(f.readline().strip())
    for line in f:
        ySize += 1

grid = [[0 for x in range(xSize)] for y in range(ySize)]

tmp = 0
with open('day8_input.txt') as f:
    for line in f:
        trees = line.strip()
        for i in range(0, len(trees)):
            grid[tmp][i] = int(trees[i])
        tmp += 1

def treeVisible(grid, xSize, ySize, treeXPosition, treeYPosition):
    treeValue = grid[treeXPosition][treeYPosition]

    tmp = 0
    for i in range(treeXPosition + 1, xSize):
        if (grid[i][treeYPosition] >= treeValue):
            tmp += 1
            break
    
    for i in range(treeXPosition - 1, -1, -1):
        if (grid[i][treeYPosition] >= treeValue):
            tmp += 1
            break
        
    for i in range(treeYPosition + 1, ySize):
        if (grid[treeXPosition][i] >= treeValue):
            tmp += 1
            break
 
    for i in range(treeYPosition - 1, -1, -1):
        if (grid[treeXPosition][i] >= treeValue):
            tmp += 1
            break

    return tmp < 4

def scenicScore(grid, xSize, ySize, treeXPosition, treeYPosition):
    treeValue = grid[treeXPosition][treeYPosition]

    tmp1 = 0
    tmp2 = 0
    tmp3 = 0
    tmp4 = 0
    for i in range(treeXPosition + 1, xSize):
        if (grid[i][treeYPosition] >= treeValue):
            tmp1 += 1
            break
        tmp1 += 1
    
    for i in range(treeXPosition - 1, -1, -1):
        if (grid[i][treeYPosition] >= treeValue):
            tmp2 += 1
            break
        tmp2 += 1
        
    for i in range(treeYPosition + 1, ySize):
        if (grid[treeXPosition][i] >= treeValue):
            tmp3 += 1
            break
        tmp3 += 1
 
    for i in range(treeYPosition - 1, -1, -1):
        if (grid[treeXPosition][i] >= treeValue):
            tmp4 += 1
            break
        tmp4 += 1

    return tmp1 * tmp2 * tmp3 * tmp4


outerVisibleTrees = 2 * xSize + 2 * ySize - 4
innerVisibleTrees = 0

for i in range(1, xSize - 1):
    for j in range(1, ySize - 1):
        if (treeVisible(grid, xSize, ySize, i, j) == True):
            innerVisibleTrees += 1

totalVisibleTrees = outerVisibleTrees + innerVisibleTrees

highestScenicScore = 0
currentScenicScore = 0

for i in range(1, xSize - 1):
    for j in range(1, ySize - 1):
        currentScenicScore = scenicScore(grid, xSize, ySize, i, j)
        if (currentScenicScore > highestScenicScore):
            highestScenicScore = currentScenicScore

print(totalVisibleTrees)
print(highestScenicScore)