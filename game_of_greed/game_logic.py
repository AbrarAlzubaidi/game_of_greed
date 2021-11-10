import random
from collections import Counter


class GameLogic():

    # def __init__(self, rollValue):
    #     pass

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
                if int(i) == 1:
                    score = 1500
        if len(item) == 3:
            for i in item.values():
                if all(int(i) == 2 for i in item.values()):
                    score = 750 * 2
        if score == 0:
            for i in item:
                
                happened = int(item[i])
                if happened >= 3:
                    if int(i) == 1:
                        score += (int(i) * 1000) * (happened-2)
                    else:
                        score += (int(i) * 100) * (happened-2)
                else:
                    if int(i) == 1:
                        score += 100*happened
                    if int(i) == 5:
                        score += 50*happened
        return score

if __name__ == "__main__":
#    testl = GameLogic()
# #    s
#    stry='444'
#    rest = tuple(stry)
#    result = testl.calculate_score(rest)
   rest2 =(Counter([1,2,1,2,3]).most_common(1)[0][1])
   print(rest2)
# if 3 in rest2:
#     print('hello')


