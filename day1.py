current = 0
elfes = []

with open('day1_input.txt') as f:
    for line in f:
        if len(line.strip()) == 0:
            elfes.append(current)
            current = 0
        else:
            current += int(line)

elfes.sort()
elfes.reverse()

print(elfes[0])
print(elfes[0] + elfes[1] + elfes[2])