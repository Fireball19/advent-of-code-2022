class Move:
    def __init__(self, symbol):
        if (symbol == 'X'):
            self.symbol = 'A'
        elif (symbol == 'Y'):
            self.symbol = 'B'
        elif (symbol == 'Z'):
            self.symbol = 'C'
        else:
            self.symbol = symbol
        if (self.symbol == 'A'):    # Rock
            self.points = 1
        elif (self.symbol == 'B'):  # Paper
            self.points = 2
        elif (self.symbol == 'C'):  # Scissors
            self.points = 3
    
    def compare(self, other):
        if (self.symbol == other.symbol):
            return 3 + self.points
        elif (self.symbol == 'A' and other.symbol == 'B'):
            return 0 + self.points
        elif (self.symbol == 'A' and other.symbol == 'C'):
            return 6 + self.points
        elif (self.symbol == 'B' and other.symbol == 'A'):
            return 6 + self.points
        elif (self.symbol == 'B' and other.symbol == 'C'):
            return 0 + self.points
        elif (self.symbol == 'C' and other.symbol == 'A'):
            return 0 + self.points
        elif (self.symbol == 'C' and other.symbol == 'B'):
            return 6 + self.points

    def calculateSymbol(self, tactic):
        mA = Move('A')
        mB = Move('B')
        mC = Move('C')
        if (tactic == 'X'): # loose
            if (self.symbol == 'A'):
                return mC.compare(self)
            if (self.symbol == 'B'):
                return mA.compare(self)     
            if (self.symbol == 'C'):
                return mB.compare(self)     
        elif (tactic == 'Y'): # draw
            if (self.symbol == 'A'):
                return 3 + 1
            if (self.symbol == 'B'):
                return 3 + 2   
            if (self.symbol == 'C'):
                return 3 + 3 
        elif (tactic == 'Z'): # win
            if (self.symbol == 'A'):
                return mB.compare(self)
            if (self.symbol == 'B'):
                return mC.compare(self)     
            if (self.symbol == 'C'):
                return mA.compare(self) 

points = 0
points2 = 0

with open('day2_input.txt') as f:
    for line in f:
        enemyMove = Move(line[0])
        myMove = Move(line[2])
        points += myMove.compare(enemyMove)
        points2 += enemyMove.calculateSymbol(line[2])

print(points)
print(points2)