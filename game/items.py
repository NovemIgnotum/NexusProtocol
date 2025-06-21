import random

class Items:
    def __init__(self, name, damage, dice):
        self.name = name
        self.damage = damage
        self.dice = dice

        rarity_number = random.randint(1, 100)
        
        # Mythic : add one dice and multiply damage by 5
        # Legendary : Multiply damage by 3
        # Rare : Multiply damage by 2
        # Common : Do nothing
        if rarity_number > 95 : 
            self.rarity = "Mythic"
            self.damage = self.damage * 5
            self.dice = self.dice + 1
        elif rarity_number > 75 :
            self.rarity = "Legendary"
            self.damage = self.damage * 3
        elif rarity_number > 40 :
            self.rarity = "Rare"
            self.damage = self.damage * 2
        else :
            self.rarity = "Common"