current = 0
current2 = 0

def findSharedLetter(string1, string2):
    for i in range(0, len(string1)):
        for j in range(0, len(string2)):
            if (string1[i] == string2[j]):
                return string1[i]

def calculateLetterValue(letter):
    if (letter.isupper()):
        return ord(letter) - 38
    elif (letter.islower()):
        return ord(letter) - 96

with open('day3_input.txt') as f:
    for line in f:
        s1 = line[:len(line)//2]
        s2 = line[len(line)//2:]
        current += calculateLetterValue(findSharedLetter(s1, s2))

lines = []

with open('day3_input.txt') as f:
    for line in f:
        lines.append(line.strip())
        if (len(lines) == 3):
            current2 += calculateLetterValue(set.intersection(*map(set,lines)).pop())
            lines.clear()

print(current)
print(current2)