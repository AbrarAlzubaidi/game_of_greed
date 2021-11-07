import random
from collections import Counter


class GameLogic():

    def __init__(self, rollValue):
        self.rollValue=rollValue

    @staticmethod
    def roll_dice(rollValue):
        """
        this method to generate random numbres between 1 to 6
        """
        randomList=[]
        i=0
        while i<rollValue:
            randomNumber= random.randint(1,6)
            randomList.append(randomNumber)
            i+=1
        return tuple(randomList)
        
    @staticmethod
    def calculate_score(item):
        item = Counter(item)
        score = 0
        if len(item) == 6:
            for i in item.values():
                if i == 1:
                    score = 1500
        if len(item) == 3:
            for i in item.values():
                if all(i == 2 for i in item.values()):
                    score = 750 * 2
        if score == 0:
            for i in item:
                happened = item[i]
                if happened >= 3:
                    if i == 1:
                        score += (i * 1000) * (happened-2)
                    else:
                        score += (i * 100) * (happened-2)
                else:
                    if i == 1:
                        score += 100*happened
                    if i == 5:
                        score += 50*happened
        return score

if __name__ == "__main__":
    pass