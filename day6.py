processedCharacters = 0
processedCharacters2 = 0

def findUniqueCharacters(line, size):
    characters = 0
    if (len(line) > (size - 1)):
        for i in range(0, len(line) - (size - 1)):
            s = line[i:i+size:1]
            if (len(set(s)) == len(s)):
                # print(s)
                return characters + size
            characters += 1
    else:
        return -1

def findMarker(line):
    return findUniqueCharacters(line, 4)

def findMessage(line):
    return findUniqueCharacters(line, 14)

with open('day6_input.txt') as f:
    for line in f:
        processedCharacters = findMarker(line)
        processedCharacters2 = findMessage(line)

print(processedCharacters)
print(processedCharacters2)