import sys
import os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))

from game import player
from game import utils

def test_damage_check() :
    p1 = player.Character("Nicolas", "Magicien") # Le magicien à une attaque de 10 et 75 point de vie
    p2 = player.Character("Baptiste" , "Magicien")
    p1.attack(p2)
    
    assert p2.health == 65

def test_heal() :
    p1 = player.Character("Nicolas", "Magicien")
    p1.attack(p1)
    p1.heal(5)

    assert p1.health == 70