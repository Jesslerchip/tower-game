# Standard attack, special attack, ability
warrior_actions = ["Sword", "Axe", "Might"]  # Axe halves mob's defense for next hit. Might decreases player speed by
# 1 and eliminates stamina cost on next hit.
archer_actions = ["Longbow", "Crossbow", "Focus"]  # Crossbow deals double crit damage. Focus halves defense but
# gives archer x2 crit chance.
healer_actions = ["Hex", "Poison", "Potion"]  # Poison deals 40 % of Hex for 3 turns. Potion costs normal amount of
# mana, heals the healer by its max hp, and heal amount is halved each use.
thief_actions = ["Dagger", "Dash", "Pickpocket"]  # Dash costs same stamina as dagger but decreases mob's stamina and
# mana. Pickpocket steals crystals and uses up mana.


# class = ["Name" (0), HP (1), Mana (2), Stamina (3), Power (4), Defense (5), Speed (6), Actions(7)]
warrior_class = ["Warrior", 10, 8, 12, 15, 10, 8, warrior_actions]
archer_class = ["Archer", 10, 10, 10, 13, 10, 12, archer_actions]
healer_class = ["Healer", 15, 12, 8, 8, 12, 10, healer_actions]
thief_class = ["Thief", 8, 10, 13, 12, 7, 15, thief_actions]
