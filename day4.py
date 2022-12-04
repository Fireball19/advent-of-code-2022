current = 0
current2 = 0

def fullyContainsSection(min1, max1, min2, max2):
    x = range(min1, max1 + 1)
    y = range(min2, max2 + 1)
    xSet = set(x)  
    if (len(xSet.intersection(y)) == len(x) or len(xSet.intersection(y)) == len(y)):
        return True
    else:
        return False

def overlapAtAll(min1, max1, min2, max2):
    x = range(min1, max1 + 1)
    y = range(min2, max2 + 1)
    xSet = set(x)  
    if (len(xSet.intersection(y)) > 0):
        return True
    else:
        return False

with open('day4_input.txt') as f:
    for line in f:
        newStr = line.replace('-', ' ').replace(',', ' ')
        numbers = list(map(int, newStr.split()))
        if (fullyContainsSection(numbers[0], numbers[1], numbers[2], numbers[3])):
            current += 1
        if (overlapAtAll(numbers[0], numbers[1], numbers[2], numbers[3])):    
            current2 += 1

print(current)
print(current2)