class Player:



class Mob:
    def __init__(self, name, hp, mana, stamina, power, defense, speed):
        self.name = name
        self.hp = hp
        self.mana = mana
        self.stamina = stamina
        self.power = power
        self.defense = defense
        self.speed = speed

        self.level = 1 #TODO: add formula to change level based on floor #
        self.xp_yield = 1


    def set_stats(self):
        #Stat = base stat * level
        self.hp *= self.level
        self.mana *= self.level
        self.stamina *= self.level
        self.power *= self.level
        self.defense *= self.level
        self.speed *= self.level

        #Experience yield = average of stats
        self.xp_yield = (self.hp + self.mana + self.stamina + self.power + self.defense + self.speed) / 6
