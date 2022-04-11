# Standard attack, special attack, ability - 0 for physical, 1 for magical, 2 for status
goblin_actions = [("Slash", 0), ("Scream", 2), ("Cower", 2)]
troll_actions = []
witch_actions = []
grendel_actions = []


# Class = [Name (0), HP (1), Mana (2), Stamina (3), Power (4), Defense (5), Speed (6), Actions (7)]

goblin = ["Goblin", 10, 10, 10, 10, 10, 10, goblin_actions]
troll = ["Troll", 10, 10, 10, 10, 10, 10, troll_actions]
witch = ["Witch", 10, 11, 10, 11, 9, 11, witch_actions]
grendel = ["Grendel", 7, 5, 10, 13, 9, 20, grendel_actions]

floor_mobs = [[goblin],  # Floor 1
              [goblin, troll],  # Floor 2
              [goblin, troll, witch],  # Floor 3
              [goblin, troll, witch],  # Floor 4
              [goblin, troll, witch, grendel]]  # Floor 5
