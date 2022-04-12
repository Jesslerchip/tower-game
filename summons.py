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
    # TODO: actually make the buying system work
    choice = ""
    while choice != "exit":
        print_shop(player)
        print(player.name + "'s crystals: " + str(player.crystals))
        choice = input("Make a selection (gear type): ").lower()

        if choice == "weapon":
            buy_weapon(player)

        if choice == "special":
            buy_special(player)

        elif choice == "armor":
            buy_armor(player)

    return


def print_shop(player):
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


def buy_weapon(player):
    if player.player_class[0] == "Warrior":
        if player.crystals >= warrior_slot_1[player.weapon + 1][2]:
            player.crystals -= warrior_slot_1[player.weapon + 1][2]
            player.weapon += 1
        else:
            print("You don't have enough crystals for that!\n")
    elif player.player_class == "Archer":
        if player.crystals >= archer_slot_1[player.weapon + 1][2]:
            player.crystals -= archer_slot_1[player.weapon + 1][2]
            player.weapon += 1
        else:
            print("You don't have enough crystals for that!\n")
    elif player.player_class == "Healer":
        if player.crystals >= healer_slot_1[player.weapon + 1][2]:
            player.crystals -= healer_slot_1[player.weapon + 1][2]
            player.weapon += 1
        else:
            print("You don't have enough crystals for that!\n")
    else:
        if player.crystals >= healer_slot_1[player.weapon + 1][2]:
            player.crystals -= healer_slot_1[player.weapon + 1][2]
            player.weapon += 1
        else:
            print("You don't have enough crystals for that!\n")


def buy_special(player):
    if player.player_class[0] == "Warrior":
        if player.crystals >= warrior_slot_2[player.special + 1][2]:
            player.crystals -= warrior_slot_2[player.special + 1][2]
            player.weapon += 1
        else:
            print("You don't have enough crystals for that!\n")
    elif player.player_class == "Archer":
        if player.crystals >= archer_slot_2[player.special + 1][2]:
            player.crystals -= archer_slot_2[player.special + 1][2]
            player.weapon += 1
        else:
            print("You don't have enough crystals for that!\n")
    elif player.player_class == "Healer":
        if player.crystals >= healer_slot_2[player.special + 1][2]:
            player.crystals -= healer_slot_2[player.special + 1][2]
            player.weapon += 1
        else:
            print("You don't have enough crystals for that!\n")
    else:
        if player.crystals >= healer_slot_2[player.special + 1][2]:
            player.crystals -= healer_slot_2[player.special + 1][2]
            player.special += 1
        else:
            print("You don't have enough crystals for that!\n")


def buy_armor(player):
    if player.crystals >= armor[player.armor + 1][2]:
        player.crystals -= armor[player.armor + 1][2]
        player.armor += 1
    else:
        print("You don't have enough crystals for that!\n")
