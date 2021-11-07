import random

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

if __name__ == "__main__":
    pass