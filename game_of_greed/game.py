from game_of_greed.game_logic import GameLogic
from game_of_greed.banker import Banker

class Game:
    def __init__(self, roller=None):
        self.roller = roller
    def play(self):
        banker = Banker()
        logic = GameLogic()
        print('Welcome to Game of Greed')
        wanna_play = input('Wanna play? ')
        if wanna_play == 'n':
            print('OK. Maybe another time')
        else:
            print('Starting round 1')
            print('Rolling 6 dice...')
            rolled_dice = self.roller(6)
            nums = []
            for i in rolled_dice:
                nums.append(str(i))
            print(','.join(nums))
            decision = input('Enter dice to keep (no spaces), or (q)uit: ')
            round=1
            if decision != 'q':
                rest = tuple(decision)
                result = logic.calculate_score(rest)
                point = banker.shelf(result)
            while decision != 'q':
                
                
                print(f"You have {point} unbanked points and {6-len(rest)} dice remaining")
                
                decision2 = input('(r)oll again, (b)ank your points or (q)uit ')
                if decision2== "b":
                    print (f"You banked {point} points in round {round}")
                    banke = banker.bank()
                    print (f"Total score is {banke} points")
                    print(f'Starting round {round+1}')
                    print('Rolling 6 dice...')
                    rolled_dice = self.roller(6)
                    nums = []
                    for y in rolled_dice:
                        nums.append(str(y))
                    print(','.join(nums))
                    decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                    round+=1
                    if decision == 'q':
                        break
                    else:
                        rest = tuple(decision)
                        result = logic.calculate_score(rest)
                        point = banker.shelf(result)
                
                if decision2=="r":
                    print('Rolling 6 dice...')
                    rolled_dice = self.roller(6)
                    nums = []
                    for i in rolled_dice:
                        nums.append(str(i))
                    print(','.join(nums))
                    decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                    if decision == 'q':
                        break
                    else:
                        rest = tuple(decision)
                        result = logic.calculate_score(rest)
                        point = banker.shelf(result)

                if decision2=="q":
                    print(f"Total score is {banke} points")
                    print(f"Thanks for playing. You earned {banke} points")

                    break
          
          
if __name__ == "__main__":
    game=Game(GameLogic.roll_dice)
    game.play()