max_exp = [0, 30, 60, 90, 120, 150]  # TODO: Array that sets players exp goals


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
        self.level = 1
        self.xp = 0
        self.max_exp = 30  # Set by max_exp array
        self.crystals = 0

    def set_stats(self):
        self.hp = (self.player_class[1] + self.player_perks[1]) * self.level
        self.mana = (self.player_class[2] + self.player_perks[2]) * self.level
        self.stamina = (self.player_class[3] + self.player_perks[3]) * self.level
        self.power = (self.player_class[4] + self.player_perks[4]) * self.level
        self.defense = (self.player_class[5] + self.player_perks[5]) * self.level
        self.speed = (self.player_class[6] + self.player_perks[6]) * self.level
        self.max_exp = max_exp[self.level]


class Mob:
    def __init__(self, name, hp, mana, stamina, power, defense, speed):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.stamina = stamina
        self.power = power
        self.defense = defense
        self.speed = speed

        self.level = 1  # TODO: add formula to change level based on floor #
        self.xp_yield = 1

    def set_stats(self):
        # Stat = base stat * level
        self.hp *= self.level
        self.mana *= self.level
        self.stamina *= self.level
        self.power *= self.level
        self.defense *= self.level
        self.speed *= self.level

        # Experience yield = average of stats
        self.xp_yield = (self.hp + self.mana + self.stamina + self.power + self.defense + self.speed) / 6
