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
            round = 1
            flag = True
            while decision != 'q':
                if round>1:
                    flag = True
                    self.begin(self,round)
                    point = 0
                    decision =0
                    decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                while flag:
                    
                    value_list = [int(x) for x in str(decision)]
                    similar=[]
                    for z in value_list:
                            if z in rolled_dice:
                                similar.append(z)
                    print(similar)
                    if len(similar) != len(value_list) or len(value_list)> len(rolled_dice):
                        print("Cheater!!! Or possibly made a typo...")
                        print(','.join(nums))
                        decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                    else:
                        flag = False
                flag = True
                if decision == 'q':
                    print("Thanks for playing. You earned 0 points")
                    break
                else:
                    flag = True
                    rest = tuple(decision)
                    result = logic.calculate_score(rest)
                    point = banker.shelf(result)

                print(
                    f"You have {point} unbanked points and {6-len(rest)} dice remaining")

                decision2 = input(
                    '(r)oll again, (b)ank your points or (q)uit ')
                if decision2 == "b":
                    print(f"You banked {point} points in round {round}")
                    flag = True
                    round += 1
                    
                    # banke = banker.bank()
                    # print(f"Total score is {banke} points")
                    # print(f'Starting round {round+1}')
                    # print('Rolling 6 dice...')
                    # rolled_dice = self.roller(6)
                    # nums = []
                    # for y in rolled_dice:
                    #     nums.append(str(y))
                    # print(','.join(nums))
                    # decision = input(
                    #     'Enter dice to keep (no spaces), or (q)uit: ')
                #     round += 1
                #     if decision == 'q':
                #         break
                #     else:
                #         rest = tuple(decision)
                #         result = logic.calculate_score(rest)
                #         point = banker.shelf(result)

                # if decision2 == "r":
                #     print('Rolling 6 dice...')
                #     rolled_dice = self.roller(6)
                #     nums = []
                #     for i in rolled_dice:
                #         nums.append(str(i))
                #     print(','.join(nums))
                #     decision = input(
                #         'Enter dice to keep (no spaces), or (q)uit: ')
                #     if decision == 'q':
                #         break
                #     else:
                #         rest = tuple(decision)
                #         result = logic.calculate_score(rest)
                #         point = banker.shelf(result)

                # if decision2 == "q":
                #     print(f"Total score is {banke} points")
                #     print(f"Thanks for playing. You earned {banke} points")

                #     break
    @staticmethod
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
        # decision = input('Enter dice to keep (no spaces), or (q)uit: ')

if __name__ == "__main__":
    game = Game(GameLogic.roll_dice)
    game.play()
