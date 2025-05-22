class Character:
    RACES = {
        "humain": {"health": 100, "attack_power": 10, "defense": 5, "speed": 5, "weight_limit" : 20},
        "elfe": {"health": 5, "attack_power": 8, "defense" : 5, "speed": 10, "weight_limit" : 15},
        "nain": {"health": 110, "attack_power": 12, "defense": 8, "speed": 3, "weight_limit" : 25},
    }

    def __init__(self, name, race):
        if race not in self.RACES:
            raise ValueError(f"Race inconnue: {race}")
        self.name = name
        self.race = race
        self.health = self.RACES[race]["health"]
        self.attack_power = self.RACES[race]["attack_power"]
        self.defense = self.RACES[race]["defense"]
        self.speed = self.RACES[race]["speed"]
        self.weight_limit = self.RACES[race]["weight_limit"]
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

# Exemple d'utilisation :
# joueur = Character("Baptiste", "elfe")
# joueur.add_item("épée")
# joueur.show_inventory()
# joueur.heal(10)
# joueur.defend()