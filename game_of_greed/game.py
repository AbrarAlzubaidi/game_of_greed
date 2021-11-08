
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
            while decision !='q':
                # print('Thanks for playing. You earned 0 points')
                if decision =="1":

                    print("You have 100 unbanked points and 5 dice remaining")
                decision = input('(r)oll again, (b)ank your points or (q)uit ')

                if decision=="b":
                    print (f"You banked 100 points in round {i}")
                    print (f"Total score is {i*100} points")
                    print(f'Starting round {i+1}')
                    print('Rolling 6 dice...')
                    rolled_dice = self.roller(6)
                    nums = []
                    for y in rolled_dice:
                        nums.append(str(y))
                    print(','.join(nums))
                if decision=="q":
                    break

                i+=1
              

                decision = input('Enter dice to keep (no spaces), or (q)uit: ')
            print("Total score is 200 points")
            print("Thanks for playing. You earned 200 points")
                

          
          
if __name__ == "__main__":
    game=Game(GameLogic.roll_dice)
    game.play()