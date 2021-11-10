from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter

class Game:
    def __init__(self, roller=None):
        
        self.diceNumber=6
        self.zilch = None
        self.last=False
        self.result = 0
        self.point=0
        self.banker = Banker()
        self.logic = GameLogic()
        self.roller = roller or self.logic.roll_dice()
    def play(self):
        
        print('Welcome to Game of Greed')
        wanna_play = input('Wanna play? ')
        if wanna_play == 'n':
            print('OK. Maybe another time')
        else:
            round=1
            while self.diceNumber !=0:
                nums=self.begin(round)
                counterNumber = Counter(nums)
                if counterNumber.most_common(1)[0][1]>2 or "1" in nums or "5" in nums:
                    decision=self.Cheater(nums)
                   
                    if self.last:
                        print('Total score is 0 points')
                    if decision == 'q' :
                        
                        print ("Thanks for playing. You earned 0 points")
                        self.diceNumber =0
                    else:
                        rest = tuple(decision)
                        self.result = self.logic.calculate_score(rest)
                        self.point = self.banker.shelf(self.result)

                    while decision != 'q':
                        
                        self.last = True
                        print(f"You have {self.point} unbanked points and {self.diceNumber-len(rest)} dice remaining")
                        if (len(rest)) == 6 :
                            self.diceNumber=12

                        decision2 = input('(r)oll again, (b)ank your points or (q)uit ')

                        if decision2== "b":
                            print (f"You banked {self.point} points in round {round}")
                            banke = self.banker.bank()
                            print (f"Total score is {banke} points")
                            round+=1
                            nums=self.begin(round)
                            counterNumber = Counter(nums)
                            if not counterNumber.most_common(1)[0][1]>2 and "1" not in nums and "5" not in nums:
                                break
                            decision=self.Cheater(nums)
                            if decision == 'q':
                                self.diceNumber=0
                                break
                            else:
                                rest = tuple(decision)
                                self.result = self.logic.calculate_score(rest)
                                self.point = self.banker.shelf(self.result)
                        if decision2=="r":
                            self.diceNumber-=len(rest)
                            print(f'Rolling {self.diceNumber} dice...')
                            rolled_dice = self.roller(self.diceNumber)
                            nums = []
                            for i in rolled_dice:
                                nums.append(str(i))
                            print(','.join(nums))
                            counterNumber = Counter(nums)
                            
                            
                            if not counterNumber.most_common(1)[0][1]>2 and "1" not in nums and "5" not in nums:
                                self.zilch = 'zilch'
                                break
                            decision=self.Cheater(nums)
                            if decision == 'q':
                                self.diceNumber=0
                                break
                            else:
                                rest = tuple(decision)
                                self.result = self.logic.calculate_score(rest)
                                self.point = self.banker.shelf(self.result)
                        if decision2=="q":
                            banke = self.banker.bank()
                            print(f"Total score is 0 points")
                            print(f"Thanks for playing. You earned 0 points")
                            self.diceNumber = 0
                            break
                        if self.diceNumber == 0:
                            break

                    if self.zilch == 'zilch':
                            print('Zilch!!! Round over')
                            print(f'You banked 0 points in round {round}')
                            print('Total score is 0 points')
                            round+=1

                else:
                    print('Zilch!!! Round over')
                    print('You banked 0 points in round 1')
                    print('Total score is 0 points')
                    round+=1
                
          
    def Cheater(self,nums):
        cheater = Counter(nums)
        while True : 
            decision = input('Enter dice to keep (no spaces), or (q)uit: ')
            if decision == 'q':
                break
            cheat = Counter(decision)
            resultCheater=[]
            for i in cheat.keys():
                if cheater[i]>=cheat[i]:
                    resultCheater.append('yes')
                else:
                    resultCheater.append('no')
            
            if('no' in resultCheater):
                print('Cheater!!! Or possibly made a typo...')
                print(','.join(nums))
            else :
                break
        return decision

    def begin(self, x):
        banker = Banker()
        logic = GameLogic()
        print(f'Starting round {x}')
        print('Rolling 6 dice...')
        rolled_dice = self.roller(6)
        nums = []
        for i in rolled_dice:
            nums.append(str(i))
        print(','.join(nums))
        return nums
if __name__ == "__main__":
    game=Game(GameLogic.roll_dice)
    game.play()
