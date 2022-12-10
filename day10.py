regX = 1
cycle = 0
sum = 0
yPosition = 0
xPosition = 0
crt = [[' ' for x in range(40)] for y in range(6)]

def nextCycle():
    global cycle, sum, xPosition, yPosition

    cycle += 1

    if (cycle == 20):
        sum += 20 * regX
    elif (cycle == 60):
        sum += 60 * regX
    elif (cycle == 100):
        sum += 100 * regX
    elif (cycle == 140):
        sum += 140 * regX
    elif (cycle == 180):
        sum += 180 * regX
    elif (cycle == 220):
        sum += 220 * regX

    if (cycle == 41):
        xPosition = 0
        yPosition = 1
    elif (cycle == 81):
        xPosition = 0
        yPosition = 2
    elif (cycle == 121):
        xPosition = 0
        yPosition = 3
    elif (cycle == 161):
        xPosition = 0
        yPosition = 4
    elif (cycle == 201):
        xPosition = 0
        yPosition = 5

    draw()
    xPosition += 1

def computeCommand(command):
    global regX, cycle

    values = command.split()
    if (values[0] == 'noop'):
        nextCycle()
    else:
        nextCycle()
        nextCycle()
        regX += int(values[1])

def draw():
    global xPosition, yPosition

    if (xPosition == regX or xPosition == (regX - 1) or xPosition == (regX + 1)):
        crt[yPosition][xPosition] = '#'     
    else:
        crt[yPosition][xPosition] = '.'

with open('day10_input.txt') as f:
    for line in f:
        computeCommand(line.strip())

print(sum)

for i in range(6):
    for j in range(40):
        print(crt[i][j], end="")
    print("")