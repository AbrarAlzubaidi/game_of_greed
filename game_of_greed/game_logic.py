import random

class GameLogic():

    def __init__(self, rollValue):
        self.rollValue=rollValue

    @staticmethod
    def roll_dice(rollValue):
        randomList=[]
        i=0
        while i<rollValue:
            randomNumber= random.randint(1,6)
            randomList.append(randomNumber)
            i+=1
        return tuple(randomList)

if __name__ == "__main__":
    values = GameLogic.roll_dice(4)
    print (values)
    print(len(values) == 4)
    value = values[0]
    print(1 <= value <= 6)
