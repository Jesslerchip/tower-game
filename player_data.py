# Standard attack, special attack, ability - 0 for physical, 1 for magical, 2 for status
warrior_actions = [("Sword", 0), ("Axe", 0), ("Might", 2)]  # Axe halves mob's defense for next hit. Might decreases
# player speed by 1 and eliminates stamina cost on next hit.
archer_actions = [("Longbow", 0), ("Crossbow", 0), ("Focus", 2)]  # Crossbow deals double crit damage. Focus halves
# defense but gives archer x2 crit chance.
healer_actions = [("Hex", 1), ("Poison", 2), ("Potion", 2)]  # Poison deals 40 % of Hex for 3 turns. Potion costs
# normal amount of  mana, heals the healer by its max hp, and heal amount is halved each use.
thief_actions = [("Dagger", 0), ("Dash", 2), ("Pickpocket", 2)]  # Dash costs same stamina as dagger but decreases
# mob's stamina and mana. Pickpocket steals crystals and uses up mana.


# Class = ["Name" (0), HP (1), Mana (2), Stamina (3), Power (4), Defense (5), Speed (6), Actions(7)]
warrior = ["Warrior", 10, 8, 12, 15, 10, 8, warrior_actions]
archer = ["Archer", 10, 10, 10, 13, 10, 12, archer_actions]
healer = ["Healer", 15, 12, 8, 8, 12, 10, healer_actions]
thief = ["Thief", 8, 10, 13, 12, 7, 15, thief_actions]
