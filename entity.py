max_xp = [0, 10, 30, 60, 100, 150]  # TODO: Array that sets players exp goals


class Player:  # Creates the player instance

    def __init__(self, name, player_class):  # Only takes player class because class determines base stats

        self.name = name
        self.player_class = player_class
        self.hp = player_class[1]  # base HP from player class
        self.mana = player_class[2]  # base mana from player class
        self.stamina = player_class[3]  # base stamina from player class
        self.power = player_class[4]  # base power from player class
        self.defense = player_class[5]  # base defense from player class
        self.speed = player_class[6]  # base speed from player class
        self.player_perks = [0, 0, 0, 0, 0, 0, 0]  # perks towards each base stat (0 is critical chance, 1-6 are stats)
        self.actions = self.player_class[7]  # List for storing available actions based on class and gear
        self.level = 1
        self.xp = 0
        self.max_xp = 10  # Set by max_exp array
        self.crystals = 0
        self.status = []

    def set_stats(self):
        self.hp = (self.player_class[1] + self.player_perks[1]) * self.level
        self.mana = (self.player_class[2] + self.player_perks[2]) * self.level
        self.stamina = (self.player_class[3] + self.player_perks[3]) * self.level
        self.power = (self.player_class[4] + self.player_perks[4]) * self.level
        self.defense = (self.player_class[5] + self.player_perks[5]) * self.level
        self.speed = (self.player_class[6] + self.player_perks[6]) * self.level
        self.max_xp = max_xp[self.level]


class Mob:
    def __init__(self, floor, stats):
        self.level = floor
        self.status = []
        self.counter = [0]

        # Stat value = base stat * level
        self.name = stats[0]
        self.hp = stats[1] * self.level
        self.mana = stats[2] * self.level
        self.stamina = stats[3] * self.level
        self.power = stats[4] * self.level
        self.defense = stats[5] * self.level
        self.speed = stats[6] * self.level

        # Experience yield = average of stats
        self.xp_yield = int((self.hp + self.mana + self.stamina + self.power + self.defense + self.speed) / 6)
