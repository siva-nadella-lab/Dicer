from Die import ADie

class DiceGroup:

    def __init__(self, defaultSides=6) -> None:
        
        self.dieGroup = []
        self.defaultSides = defaultSides
        self.rollResults = []
        self.maxRollResult = 0
        self.minRollResult = 0

    
    def addDie(self, sides=6):

        dieSides = self.defaultSides
        if (sides > self.defaultSides):
            dieSides = sides
        
        die = ADie(dieSides)
        self.dieGroup.append(die)
        self.maxRollResult += dieSides
        self.minRollResult = len(self.dieGroup)

    def rollAllDice(self):

        allDieResult = 0
        for die in self.dieGroup:
            allDieResult += die.roll()
        
        self.rollResults.append(allDieResult)

    def getFrequencies(self):

        frequencies = []
        for i in range(self.minRollResult, self.maxRollResult+1, 1):
            frequencyOfi = self.rollResults.count(i)
            frequencies.append(frequencyOfi)
        
        return frequencies

