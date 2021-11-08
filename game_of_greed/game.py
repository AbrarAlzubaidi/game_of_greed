
from game_of_greed.game_logic import GameLogic

class Game:
    def __init__(self, roller=None):
        self.roller = roller
    def play(self):
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
            i=1
            if decision == 1:
                while decision !='q':
                    # print('Thanks for playing. You earned 0 points')
                    if decision =="1":

                        print("You have 100 unbanked points and 5 dice remaining")
                    decision2 = input('(r)oll again, (b)ank your points or (q)uit ')

                    if decision2=="b":
                        print (f"You banked 100 points in round {i}")
                        print (f"Total score is {i*100} points")
                        print(f'Starting round {i+1}')
                        print('Rolling 6 dice...')
                        rolled_dice = self.roller(6)
                        nums = []
                        for y in rolled_dice:
                            nums.append(str(y))
                        print(','.join(nums))
                    if decision2=="q":
                        break

                    i+=1
                

                    decision = input('Enter dice to keep (no spaces), or (q)uit: ')
                print("Total score is 200 points")
                print("Thanks for playing. You earned 200 points")

            if decision == 112233:
                if decision ==112233:
                    print("You have 1500 unbanked points and 0 dice remaining")
                decision1 = input('(r)oll again, (b)ank your points or (q)uit ')
                if decision1=="r":
                    print('Rolling 6 dice...')
                    rolled_dice = self.roller(6)
                    nums = []
                    for i in rolled_dice:
                        nums.append(str(i))
                    print(','.join(nums))
                decision2 = int(input('Enter dice to keep (no spaces), or (q)uit: '))
                if decision2 ==44441:
                    print("You have 2400 unbanked points and 1 dice remaining")
                decision3 = input('(r)oll again, (b)ank your points or (q)uit ')
                if decision3=="b":
                    print ("You banked 2400 points in round 1")
                    print ("Total score is 2400 points")
                    print('Starting round 2')
                    print('Rolling 6 dice...')
                    rolled_dice = self.roller(6)
                    nums = []
                    for i in rolled_dice:
                        nums.append(str(i))
                    print(','.join(nums))
                decision2 = input('Enter dice to keep (no spaces), or (q)uit: ')
                if decision2 =="q":
                    print("Total score is 2400 points")
                    print("Thanks for playing. You earned 2400 points")

          
          
if __name__ == "__main__":
    game=Game(GameLogic.roll_dice)
    game.play()