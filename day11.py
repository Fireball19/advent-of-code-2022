from functools import reduce
import copy, math

monkeys = {}

class Monkey:
    def __init__(self):
        self.id = -1
        self.items = []
        self.operation = ''
        self.operationValue = ''
        self.testValue = -1
        self.toMonkeyIfTrue = -1
        self.toMonkeyIfFalse = -1
        self.inspectItemCount = 0

    def __str__(self):
        return f"{self.id}, {self.items}, {self.operation}, {self.operationValue}, {self.testValue}, {self.toMonkeyIfTrue}, {self.toMonkeyIfFalse}"

    def inspectItems(self, monkeys, divided, lcm):
        i = 0
        while i < len(self.items):
            if (self.operation == '+'):
                if (self.operationValue == 'old'):
                    self.items[i] += self.items[i]
                else:
                    self.items[i] += int(self.operationValue)
            elif (self.operation == '-'):
                if (self.operationValue == 'old'):
                    self.items[i] -= self.items[i]
                else:
                    self.items[i] -= int(self.operationValue)
            elif (self.operation == '*'):
                if (self.operationValue == 'old'):
                    self.items[i] *= self.items[i]
                else:
                    self.items[i] *= int(self.operationValue)
            elif (self.operation == '/'):
                if (self.operationValue == 'old'):
                    self.items[i] //= self.items[i]
                else:
                    self.items[i] //= int(self.operationValue)

            # Monkey gets bored
            if (divided == True): 
                self.items[i] //= 3
            else:
                self.items[i] = self.items[i] % lcm
            
            if (self.items[i] % self.testValue == 0):
                monkeys[self.toMonkeyIfTrue].items.append(self.items.pop(0))
            else:
                monkeys[self.toMonkeyIfFalse].items.append(self.items.pop(0))
            
            self.inspectItemCount += 1

lines = open('day11_input.txt').readlines()
i = 0
while i < len(lines):
    currentMonkey = Monkey()
    currentMonkey.id = int(''.join(filter(str.isdigit, lines[i].split()[1])))
    currentMonkey.items = (list(map(int, lines[i + 1].replace(',', '').split()[2:])))
    currentMonkey.operation = lines[i + 2].split()[4]
    currentMonkey.operationValue = lines[i + 2].split()[5]
    currentMonkey.testValue = int(lines[i + 3].split()[3]) 
    currentMonkey.toMonkeyIfTrue = int(lines[i + 4].split()[5])
    currentMonkey.toMonkeyIfFalse = int(lines[i + 5].split()[5])

    monkeys[currentMonkey.id] = currentMonkey
    i += 7

monkeys2 = copy.deepcopy(monkeys)
testValues = []
for i in range(len(monkeys)):
    testValues.append(int(monkeys[i].testValue))
lcm = reduce(math.lcm, testValues)

rounds = 20
rounds2 = 10000

for i in range(rounds):
    for j in range(len(monkeys)):
        monkeys[j].inspectItems(monkeys, True, 0)

for i in range(rounds2):
    for j in range(len(monkeys2)):
        monkeys2[j].inspectItems(monkeys2, False, lcm)

inspectedItemCounts = []
inspectedItemCounts2 = []
for i in range(len(monkeys)):
    inspectedItemCounts.append(monkeys[i].inspectItemCount)
    inspectedItemCounts2.append(monkeys2[i].inspectItemCount)

inspectedItemCounts.sort()
print(inspectedItemCounts[-1] * inspectedItemCounts[-2])

inspectedItemCounts2.sort()
print(inspectedItemCounts2[-1] * inspectedItemCounts2[-2])