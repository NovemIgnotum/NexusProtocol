class Enemies:
    TYPES = {
        "goblin": {
            "name": "Goblin",
            "health": 50,
            "attack_power": 5,
            "defense": 2,
            "speed": 4,
            "description": "Un petit monstre vert, rapide et sournois.",
        },
        "skeleton": {
            "name": "Squelette",
            "health": 40,
            "attack_power": 7,
            "defense": 3,
            "speed": 3,
            "description": "Un squelette animé, lent mais résistant.",
        },
        "orc": {
            "name": "Orc",
            "health": 80,
            "attack_power": 10,
            "defense": 5,
            "speed": 2,
            "description": "Un grand monstre vert, fort et brutal.",
        },
        "dragon": {
            "name": "Dragon",
            "health": 200,
            "attack_power": 25,
            "defense": 20,
            "speed": 5,
            "description": "Une créature légendaire, puissante et majestueuse.",
        },
    }
    def __init__(self, enemy_type):
        if enemy_type not in self.TYPES:
            raise ValueError(f"Type d'ennemi inconnu: {enemy_type}")
        self.name = self.TYPES[enemy_type]["name"]
        self.health = self.TYPES[enemy_type]["health"]
        self.attack_power = self.TYPES[enemy_type]["attack_power"]
        self.defense = self.TYPES[enemy_type]["defense"]
        self.speed = self.TYPES[enemy_type]["speed"]
        self.description = self.TYPES[enemy_type]["description"]
        
    def attack(self, other_character):
        damage = self.attack_power - other_character.defense
        if damage < 0:
            damage = 0
        other_character.health -= damage
        print(f"{self.name} attaque {other_character.name} pour {damage} dégâts !")
        print(f"La santé de {other_character.name} est maintenant {other_character.health}.")
        if other_character.health <= 0:
            print(f"{other_character.name} est vaincu !")
        else:
            print(f"{other_character.name} reste en vie avec {other_character.health} points de vie.")
            
    def defend(self):
        print(f"{self.name} se met en position de défense.")
    
    def show_info(self):
        print(f"{self.name}: {self.description}")
        print(f"Vie: {self.health}, Attaque: {self.attack_power}, Défense: {self.defense}, Vitesse: {self.speed}")
    
