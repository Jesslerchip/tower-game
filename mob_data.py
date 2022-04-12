# Standard attack, special attack, ability - 0 for physical, 1 for magical, 2 for status
goblin_actions = [("Slash", 0), ("Scream", 2), ("Cower", 2)]
troll_actions = [("Club", 0), ("Stomp", 0), ("Rest", 2)]
witch_actions = [("Incantation", 1), ("Toxic Brew", 1), ("Magic Broom", 2)]
grendel_actions = [("Slash", 0), ("Stomp", 0), ("Last Resort", 2)]
orc_actions = [("Smash", 0), ("Stomp", 0), ("Skill Swap", 2)]


# Class = [Name (0), HP (1), Mana (2), Stamina (3), Power (4), Defense (5), Speed (6), Actions (7)]

goblin = ["Goblin", 10, 10, 10, 10, 10, 10, goblin_actions]
troll = ["Troll", 10, 10, 10, 10, 10, 10, troll_actions]
witch = ["Witch", 10, 11, 10, 11, 9, 11, witch_actions]
grendel = ["Grendel", 5, 5, 10, 13, 7, 20, grendel_actions]
orc = ["Orc", 16, 6, 10, 8, 16, 8, orc_actions]

floor_mobs = [[goblin],  # Floor 1
              [goblin, troll],  # Floor 2
              [goblin, troll, witch],  # Floor 3
              [goblin, troll, witch],  # Floor 4
              [goblin, troll, witch, grendel],  # Floor 5
              [troll, witch, grendel, orc]]  # Floor 6

ritual_actions = [("Slash", 0), ("Scream", 2), ("Skill Swap", 2)]

# Classes for the ritual mobs
zombie = ["Zombie", 10, 8, 10, 10, 8, 10, ritual_actions]
skeleton = ["Skeleton", 8, 8, 10, 10, 10, 10, ritual_actions]
ghost = ["Ghost", 8, 10, 8, 10, 10, 10, ritual_actions]
demon = ["Demon", 10, 10, 10, 10, 8, 8, ritual_actions]
ghoul = ["Ghoul", 10, 10, 8, 10, 8, 10, ritual_actions]

ritual_mobs = [zombie, skeleton, ghost, demon, ghoul]
