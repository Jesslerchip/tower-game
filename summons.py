# Warrior Gear
warrior_slot_1 = [("Rusted sword", "Well, it's better than your fists.", 100),
                  ("Iron shortsword", "A decent weapon that feels well-weighted in your hands.", 100)]

warrior_slot_2 = [("Blunt axe", "Basically a rock on a stick.", 100),
                  ("Hatchet", "Capable of chopping off stray limbs, of trees and trolls alike.", 100)]
warrior_slot_3 = ["none"]

# Archer Gear
archer_slot_1 = [("Bent longbow", "Hardly an upgrade from a child's slingshot.", 100),
                 ("Reinforced longbow", "A little bit of TLC has made this bow... usable.", 100)]
archer_slot_2 = [("Crooked crossbow", "Shoddy craftsmanship makes for shoddy aim. Shame on you.", 100),
                 ("Precise crossbow", "Guaranteed to get a bullseye, or your crystals back! (Depends on user's skill "
                                      "and aim. No refunds.)"), 100]
archer_slot_3 = ["none"]

# Healer Gear
healer_slot_1 = [("Weakened curse", "Hurts the enemy's tender little feewings.", 100),
                 ("Dark hex", "An incantation that does damage. What more can you really ask for?", 100)]
healer_slot_2 = [("Poison berries", "Where did you find these, in your backyard?", 100),
                 ("Belladonna", "A plant that actually does damage. Now we're talking.", 100)]

# Thief Gear
thief_slot_1 = [("Pocket knife", "Care to do a whittle whittling?", 100),
                (
                "Sharp dagger", "A light, sharp weapon. Less damage than a sword, but it doesn't weigh you down.", 100)]
thief_slot_2 = ["none"]
thief_slot_3 = ["none"]

# Armor
armor = [("Cotton rags", "", 100),
         ("Thin armor", "", 100),
         ("Gambeson", "", 100),
         ("Chain mail", "", 100),
         ("Cuirass", "", 100),
         ("Plated armor", "", 100)]


def summon_menu(player):
    if player.player_class[0] == "Warrior":
        if player.weapon < (len(warrior_slot_1) - 1):
            print("Weapon: ".ljust(10) + warrior_slot_1[player.weapon + 1][0].ljust(20)
                  + str(warrior_slot_1[player.weapon + 1][2]) + " crystals")  # next main weapon available to player
        else:
            print("--Max weapon achieved--")
        if player.special < (len(warrior_slot_2) - 1):
            print("Special: ".ljust(10) + warrior_slot_2[player.special + 1][0].ljust(20)
                  + str(warrior_slot_2[player.special + 1][2]) + " crystals")  # next special weapon available to player
        else:
            print("--Max special achieved--")

    if player.player_class[0] == "Archer":
        if player.weapon < (len(archer_slot_1) - 1):
            print("Weapon: ".ljust(10) + archer_slot_1[player.weapon + 1][0].ljust(20)
                  + str(archer_slot_1[player.weapon + 1][2]) + " crystals")  # next main weapon available to player
        else:
            print("--Max weapon achieved--")
        if player.special < (len(archer_slot_2) - 1):
            print("Special: ".ljust(10) + archer_slot_2[player.special + 1][0].ljust(20)
                  + str(archer_slot_2[player.special + 1][2]) + " crystals")  # next special weapon available to player
        else:
            print("--Max special achieved--")

    if player.player_class[0] == "Healer":
        if player.weapon < (len(healer_slot_1) - 1):
            print("Weapon: ".ljust(10) + healer_slot_1[player.weapon + 1][0].ljust(20)
                  + str(healer_slot_1[player.weapon + 1][2]) + " crystals")  # next main weapon available to player

        else:
            print("--Max weapon achieved--")
        if player.special < (len(healer_slot_2) - 1):
            print("Special: ".ljust(10) + healer_slot_2[player.special + 1][0].ljust(20)
                  + str(healer_slot_2[player.special + 1][2]) + " crystals")  # next special weapon available to player
        else:
            print("--Max special achieved--")

    if player.player_class[0] == "Thief":
        if player.weapon < (len(thief_slot_1) - 1):
            print("Weapon: ".ljust(10) + thief_slot_1[player.weapon + 1][0].ljust(20)
                  + str(thief_slot_1[player.weapon + 1][2]) + " crystals")  # next main weapon available to player
        else:
            print("--Max weapon achieved--")
        if player.special < (len(thief_slot_2) - 1):
            print("Special: ".ljust(10) + thief_slot_2[player.special + 1][0].ljust(20)
                  + str(thief_slot_2[player.special + 1][2]) + " crystals")  # next special weapon available to player
        else:
            print("--Max special achieved--")

    if player.armor < (len(armor) - 1):
        print("Armor: ".ljust(10) + armor[player.armor + 1][0].ljust(20)
              + str(armor[player.armor + 1][2]) + " crystals")
    else:
        print("--Max armor achieved--")

    print("Exit\n")

    # TODO: actually make the buying system work
    choice = ""
    while choice != "exit":
        choice = input("Make a selection (gear type): ").lower()

        if choice == "weapon":
            if player.crystals >= 0:
                player.crystals -= 0
                player.weapon += 1

        if choice == "special":
            if player.crystals >= 100:
                player.crystals -= 100
                player.special += 1

        elif choice == "armor":
            if player.crystals >= 100:
                player.crystals -= 100
                player.armor += 1

    return
