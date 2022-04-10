# Warrior Gear
warrior_slot_1 = [["Rusted sword", "Iron shortsword"],  # Item name
                  ["Well, it's better than your fists.",  # Descriptions
                   "A decent weapon that feels well-weighted in your hands."]]

warrior_slot_2 = [["Blunt axe", "Hatchet"],  # Item name
                  ["Basically a rock on a stick.",  # Descriptions
                   "Capable of chopping off stray limbs, of trees and trolls alike."]]
warrior_slot_3 = ["none"]

# Archer Gear
archer_slot_1 = [["Bent longbow", "Reinforced longbow"],  # Item name
                 ["Hardly an upgrade from a child's slingshot.",  # Descriptions
                  "A little bit of TLC has made this bow... usable."]]
archer_slot_2 = [["Crooked crossbow", "Precise crossbow"],  # Item name
                 ["Shoddy craftsmanship makes for shoddy aim. Shame on you.",  # Descriptions
                  "Guaranteed to get a bullseye, or your crystals back! (Depends on user's skill and aim. No refunds.)"]]
archer_slot_3 = ["none"]

# Healer Gear
healer_slot_1 = [["Weakened curse", "Dark hex"],  # Item name
                 ["Hurts the enemy's tender little feewings.",  # Descriptions
                  "An incantation that does damage. What more can you really ask for?"]]
healer_slot_2 = [["Poison berries", "Belladonna"],  # Item name
                 ["Where did you find these, in your backyard?",  # Descriptions
                  "A plant that actually does damage. Now we're talking."]]
healer_slot_3 = ["none"]

# Thief Gear
thief_slot_1 = [["Pocket knife", "Sharp dagger"],  # Item name
                ["Care to do a whittle whittling?",  # Descriptions
                 "A light, sharp weapon. Less damage than a sword, but it doesn't weigh you down."]]
thief_slot_2 = ["none"]
thief_slot_3 = ["none"]

# Armor
armor = ["Cotton rags", "Thin armor", "Gambeson", "Chain mail", "Cuirass", "Plated armor"]


def summon_menu(player):
    if player.player_class[0] == "Warrior":
        print(warrior_slot_1[0][player.weapon + 1])  # Prints name of next main weapon available to player
        print(warrior_slot_2[0][player.special + 1])  # Prints name of next special weapon available to player
        print(armor[player.armor + 1])  # Prints name of next armor class available to player
    if player.player_class[0] == "Archer":
        print(archer_slot_1[0][player.weapon + 1])  # Prints name of next main weapon available to player
        print(archer_slot_2[0][player.special + 1])  # Prints name of next special weapon available to player
        print(armor[player.armor + 1])  # Prints name of next armor class available to player
    if player.player_class[0] == "Healer":
        print(healer_slot_1[0][player.weapon + 1])  # Prints name of next main weapon available to player
        print(healer_slot_2[0][player.special + 1])  # Prints name of next special weapon available to player
        print(armor[player.armor + 1])  # Prints name of next armor class available to player
    if player.player_class[0] == "Thief":
        print(thief_slot_1[0][player.weapon + 1])  # Prints name of next main weapon available to player
        print(thief_slot_2[0][player.special + 1])  # Prints name of next special weapon available to player
        print(armor[player.armor + 1])  # Prints name of next armor class available to player

    return 0
