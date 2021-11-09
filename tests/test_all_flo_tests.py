from game_of_greed.game import Game
from tests.flow.flo import Flo


def test_bank1():
    Flo.test('tests/flow/bank_first_for_two_rounds.sim.txt')

def test_no_for_wanna_play():
    Flo.test('tests/flow/quitter.sim.txt')

def test_bank2():
    Flo.test('tests/flow/bank_one_roll_then_quit.sim.txt')
   
def test_bank3():
    Flo.test('tests/flow/hot_dice.txt') 

def test_yes_for_wanna_play2():
    Flo.test('tests/flow/one_and_done.sim.txt')

def test_zilch():
    Flo.test('tests/flow/zilcher.sim.txt')
    
def test_cheater():
    Flo.test('tests/flow/cheat_and_fix.sim.txt')