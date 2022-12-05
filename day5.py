stacks1 = []
stacks2 = []
stacksSize = 9
for i in range(0, stacksSize):
	stacks1.append(list())
for i in range(0, stacksSize):
	stacks2.append(list())

def moveCrateOneAtATime(stacks, count, fromStack, toStack):
    for i in range(0, count):
        stacks[toStack].insert(0, stacks[fromStack].pop(0))

def moveCratesTogether(stacks, count, fromStack, toStack):
    cratesToInsert = []
    # pop crates
    for i in range(0, count):
        cratesToInsert.append(stacks[fromStack].pop(0))
    # insert crates
    cratesToInsert.reverse()
    for i in range(0, len(cratesToInsert)):
        stacks[toStack].insert(0, cratesToInsert.pop(0))

moves = False
with open('day5_input.txt') as f:
    for line in f:
        if (moves == False):
            currentStack = 0
            currentWhiteSpace = 0
            for element in range(0, len(line)):
                if (line[element] == '['):
                    # stacks1
                    stacks1[currentStack].append(line[element + 1])
                    # stacks2
                    stacks2[currentStack].append(line[element + 1])
                    currentStack += 1
                    currentWhiteSpace = 0
                if (line[element] == ' '):
                    currentWhiteSpace += 1
                if (currentWhiteSpace == 4):
                    currentStack += 1
                    currentWhiteSpace = 0
            if (len(line.strip()) == 0):
                moves = True
        else:
            currentLine = line.split()
            # stacks1
            moveCrateOneAtATime(stacks1, int(currentLine[1]), int(currentLine[3]) - 1, int(currentLine[5]) - 1)
            # stacks2
            if (int(currentLine[1]) == 1):
                moveCrateOneAtATime(stacks2, int(currentLine[1]), int(currentLine[3]) - 1, int(currentLine[5]) - 1)
            else:
                moveCratesTogether(stacks2, int(currentLine[1]), int(currentLine[3]) - 1, int(currentLine[5]) - 1)

solution = ""
for i in range(0, stacksSize):
    solution += stacks1[i][0]
print(solution)

solution2 = ""
for i in range(0, stacksSize):
    solution2 += stacks2[i][0]
print(solution2)