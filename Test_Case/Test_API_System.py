import sys
import pytest
sys.path.append('..')
from Test_Action.Pokemon import *


def setup():
    pass
    
def teardown():
    pass


class Test_Pokemon(object):

    @classmethod
    def setup_class(self):
        self.pokemon = Pokemon()
    
    def test_No1(self):
        print("\n1. 列出 id 為 6 的寶可夢名稱（name）:")
        self.pokemon.No1(6)
    
    def test_No2(self):
        print("\n2. 列出 id < 20, id > 0 的寶可夢名稱（name）以及其寶可夢的屬性（types），依照 id 由小至大排序:")
        self.pokemon.No2(19)

    def test_No3(self):
        print("\n3. 列出 id < 100, id > 0 的寶可夢中，體重（weight） < 50 的寶可夢名稱（name）及寶可夢體重（weight），並且依照體重由大至小排序:")
        self.pokemon.No3(99)

