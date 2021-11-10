from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker
from collections import Counter

class Game:
    def __init__(self, roller=None):
        self.roller = roller
        self.diceNumber=6
        self.zilch = None
        self.last=False
    def play(self):
        banker = Banker()
        logic = GameLogic()
        print('Welcome to Game of Greed')
        wanna_play = input('Wanna play? ')
        if wanna_play == 'n':
            print('OK. Maybe another time')
        else:
            round=1
            while self.diceNumber !=0:
                print(f'Starting round {round}')
                print('Rolling 6 dice...')
                
                rolled_dice = self.roller(6)
                nums = []
                for i in rolled_dice:
                    nums.append(str(i))
                print(','.join(nums))
                counterNumber = Counter(nums)
                cheater = Counter(nums)

                if counterNumber.most_common(1)[0][1]>2 or "1" in nums or "5" in nums:
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
                    
                    
                        

                    if self.last:
                        print('Total score is 0 points')
                    if decision == 'q' :
                        
                        print ("Thanks for playing. You earned 0 points")
                        self.diceNumber =0
                    else:
                        rest = tuple(decision)
                        result = logic.calculate_score(rest)
                        point = banker.shelf(result)

                    while decision != 'q':
                        
                        self.last = True
                        print(f"You have {point} unbanked points and {self.diceNumber-len(rest)} dice remaining")
                        if (len(rest)) == 6 :
                            self.diceNumber=12

                        decision2 = input('(r)oll again, (b)ank your points or (q)uit ')

                        if decision2== "b":
                            print (f"You banked {point} points in round {round}")
                            banke = banker.bank()
                            print (f"Total score is {banke} points")
                            round+=1
                            print(f'Starting round {round}')
                            print('Rolling 6 dice...')
                            rolled_dice = self.roller(self.diceNumber)
                            nums = []
                            for y in rolled_dice:
                                nums.append(str(y))
                            print(','.join(nums))
                            counterNumber = Counter(nums)
                            if not counterNumber.most_common(1)[0][1]>2 and "1" not in nums and "5" not in nums:
                                break
                            while True : 
                                decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                                if decision == 'q':
                                    self.diceNumber=0
                                    break
                                else:
                                    rest = tuple(decision)
                                    result = logic.calculate_score(rest)
                                    point = banker.shelf(result)
                                cheater = Counter(nums)
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
                                else:
                                    break
                            
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
                            while True : 
                                decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                                if decision == 'q':
                                    self.diceNumber=0
                                    break
                                else:
                                    rest = tuple(decision)
                                    result = logic.calculate_score(rest)
                                    point = banker.shelf(result)
                                cheater = Counter(nums)
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
                                else:
                                    break
                        if decision2=="q":
                            banke = banker.bank()
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
                
          
          
if __name__ == "__main__":
    game=Game(GameLogic.roll_dice)
    game.play()
