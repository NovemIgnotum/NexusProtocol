from termcolor import colored, cprint

class Character:
    CLASSES = {
        "Magicien": {"max_health" : 75,"health": 75, "attack_power": 10, "defense": 5, "speed": 5, "weight_limit" : 20},
        "Voleur": {"max_health" : 80, "health": 80, "attack_power": 8, "defense" : 5, "speed": 10, "weight_limit" : 15},
        "Guerrier": {"max_health" : 100,"health": 100, "attack_power": 10, "defense": 8, "speed": 3, "weight_limit" : 25},
    }

    def __init__(self, name, classe):
        if classe not in self.CLASSES:
            raise ValueError(f"Classe inconnue: {classe}")
        self.name = name
        self.race = classe
        self.health = self.CLASSES[classe]["health"]
        self.attack_power = self.CLASSES[classe]["attack_power"]
        self.defense = self.CLASSES[classe]["defense"]
        self.speed = self.CLASSES[classe]["speed"]
        self.weight_limit = self.CLASSES[classe]["weight_limit"]
        self.max_health = self.CLASSES[classe]["max_health"]
        self.inventory = []

    def attack(self, other_character):
        other_character.health -= self.attack_power
        print(f"{self.name} attaque {other_character.name} pour {self.attack_power} dégâts !")
        print(f"La santé de {other_character.name} est maintenant {other_character.health}.")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} ajoute {item} à son inventaire.")

    def remove_item(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            print(f"{self.name} retire {item} de son inventaire.")
        else:
            print(f"{item} n'est pas dans l'inventaire de {self.name}.")

    def show_inventory(self):
        print(f"Inventaire de {self.name}: {', '.join(self.inventory) if self.inventory else 'vide'}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} se soigne de {amount} points. Santé actuelle: {self.health}")

    def defend(self):
        print(f"{self.name} se met en position de défense.")
    
    def dipaly_life(self):
        print("[", end="")
        life_percent = (self.health / self.max_health) * 100
        life_cube = "■" * int(life_percent / 5) + " " * int((100-life_percent) / 5)

        if life_percent < 20 : color = "red"
        elif life_percent < 50 : color = "light_red"
        else : color = "green"

        cprint(life_cube, color, attrs=["bold"], end="")
        print("]")

# Exemple d'utilisation :
# joueur = Character("Baptiste", "elfe")
# joueur.add_item("épée")
# joueur.show_inventory()
# joueur.heal(10)
# joueur.defend()