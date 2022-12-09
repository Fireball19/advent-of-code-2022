class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.size = 0
        self.directories = []
        self.files = []

class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size

listsContent = False
head = Directory('/', None)
currentDirectory = head
directories = []
directories.append(head)

def identifyCommand(line):
    if (len(line) < 1):
        return
    if (line[0] == '$'):
        command = line.split()

        global listsContent

        if (command[1] == 'cd'):
            # print(command[1], command[2])
            cdCommand(command[2])
            listsContent = False

        if (command[1] == 'ls'):
            listsContent = True

def cdCommand(value):
    global currentDirectory

    if (value == '/'):
        currentDirectory = head
    elif (value == '..'):
        currentDirectory = currentDirectory.parent
    else:
        for i in currentDirectory.directories:
            if i.name == value:
                currentDirectory = i
                # print(currentDirectory.name, value)

def lsCommand(line):
    global currentDirectory

    if (line[0] == 'd'):
        dir = line.split()
        newDir = Directory(dir[1], currentDirectory)
        currentDirectory.directories.append(newDir)
        directories.append(newDir)
        # print(dir[1], currentDirectory.name, currentDirectory.parent)
    elif (line[0].isdigit()):
        file = line.split()
        currentDirectory.files.append(File(file[1], file[0]))
        currentDirectory.size += int(file[0])

        tmp = currentDirectory.parent
        while (tmp is not None):
            tmp.size += int(file[0])
            tmp = tmp.parent

with open('day7_input.txt') as f:
    for line in f:
        if (listsContent == True):
            lsCommand(line.strip())
        identifyCommand(line.strip())

currentDirectory = head
size = 0

for i in directories:
    if i.size <= 100000:
        size += i.size


size2 = 70000000
neededSize = 70000000 - directories[0].size
smallestSize = (neededSize - 30000000) * -1

for i in directories:
    if i.size >= smallestSize and size2 >= i.size:
        size2 = i.size

print(size)
print(size2)