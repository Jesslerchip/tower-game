from random import randint

max_xp = [0, 10, 30, 60, 100, 150, 200, 250, 300, 400, 500]  # TODO: xp goals for higher floors


class Player:  # Creates the player instance

    def __init__(self, name, player_class):  # Only takes player class because class determines base stats

        self.name = name
        self.player_class = player_class
        self.perks = [0, 0, 0, 0, 0, 0, 0]  # perks towards each base stat (0 is critical chance, 1-6 are stats)
        self.actions = self.player_class[7]  # List for storing available actions based on class and gear
        self.gear = self.player_class[8]
        self.level = 1
        self.xp = 0
        self.max_xp = 10  # Set by max_exp array
        self.hp = player_class[1]  # base HP from player class
        self.mana = player_class[2]  # base mana from player class
        self.stamina = player_class[3]  # base stamina from player class
        self.power = player_class[4]  # base power from player class
        self.defense = player_class[5]  # base defense from player class
        self.speed = player_class[6]  # base speed from player class
        self.max_hp = self.hp
        self.max_mana = player_class[1]
        self.max_stamina = player_class[1]
        self.crystals = 0
        self.status = []
        self.gear_level = [0, 0, 0]  # Weapon, Special, Armor

        # 0 = Heal counter, 1 = Burn counter
        self.counter = [0, 0]

    def set_stats(self):
        self.hp = (self.player_class[1] + self.perks[1]) * int(pow(self.level, 2) / 2) + 10
        self.mana = (self.player_class[2] + self.perks[2]) * self.level
        self.stamina = (self.player_class[3] + self.perks[3]) * self.level
        self.power = (self.player_class[4] + self.perks[4]) * self.level
        self.defense = (self.player_class[5] + self.perks[5]) * self.level
        self.speed = (self.player_class[6] + self.perks[6]) * self.level
        self.max_xp = max_xp[self.level]
        self.max_hp = self.hp
        self.max_mana = self.mana
        self.max_stamina = self.stamina
        self.counter = [0, 0]


class Mob:
    def __init__(self, floor, stats):
        self.mob_class = stats
        self.level = floor
        self.status = []
        self.actions = self.mob_class[7]
        self.last_action = 3
        self.perks = [0, 0, 0, 0, 0, 0, 0]

        # Calculates mob perks
        random_perk = 0
        while (sum(self.perks) < int(self.level / 2)) and 0 in self.perks:
            random_perk = randint(0, 6)
            if self.perks[random_perk] == 0:
                self.perks[random_perk] = randint(0, (int(self.level / 2 + 1) - sum(self.perks)))
        if random_perk == 0:
            self.perks[random_perk] *= 4

        # 0 = Poison counter, 1 = Ritual counter, 2 = Turn counter
        self.counter = [0, 0, 1]

        # Stat value = base stat * level
        self.name = stats[0]
        self.hp = (stats[1] + self.perks[1]) * int(pow(self.level, 2) / 2) + 10
        self.mana = (stats[2] + self.perks[2]) * self.level
        self.stamina = (stats[3] + self.perks[3]) * self.level
        self.power = (stats[4] + self.perks[4]) * self.level
        self.defense = (stats[5] + self.perks[5]) * self.level
        self.speed = (stats[6] + self.perks[6]) * self.level
        self.max_hp = self.hp
        self.max_mana = self.mana
        self.max_stamina = self.stamina

        # Experience yield = average of stats
        self.xp_yield = int((self.hp + self.mana + self.stamina + self.power + self.defense + self.speed) / 6)
