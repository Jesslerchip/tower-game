# Warrior Gear
warrior_slot_1 = [("Rusted sword", "Well, it's better than your fists.", 100),
                  ("Iron shortsword", "A decent weapon that feels well-weighted in your hands.", 100)]

warrior_slot_2 = [("Blunt axe", "Basically a rock on a stick.", 100),
                  ("Hatchet", "Capable of chopping off stray limbs, of trees and trolls alike.", 100)]
warrior_gear = [warrior_slot_1, warrior_slot_2]

# Archer Gear
archer_slot_1 = [("Bent longbow", "Hardly an upgrade from a child's slingshot.", 100),
                 ("Reinforced longbow", "A little bit of TLC has made this bow... usable.", 100)]
archer_slot_2 = [("Crooked crossbow", "Shoddy craftsmanship makes for shoddy aim. Shame on you.", 100),
                 ("Precise crossbow", "Guaranteed to get a bullseye, or your crystals back! (Depends on user's skill "
                                      "and aim. No refunds.)"), 100]
archer_gear = [archer_slot_1, archer_slot_2]

# Healer Gear
healer_slot_1 = [("Weakened curse", "Hurts the enemy's tender little feewings.", 100),
                 ("Dark hex", "An incantation that does damage. What more can you really ask for?", 100)]
healer_slot_2 = [("Poison berries", "Where did you find these, in your backyard?", 100),
                 ("Belladonna", "A plant that actually does damage. Now we're talking.", 100)]
healer_gear = [healer_slot_1, healer_slot_2]

# Thief Gear
thief_slot_1 = [("Pocket knife", "Care to do a whittle whittling?", 100),
                (
                "Sharp dagger", "A light, sharp weapon. Less damage than a sword, but it doesn't weigh you down.", 100)]
thief_slot_2 = ["none"]
thief_gear = [thief_slot_1, thief_slot_2]

# Armor
armor = [("Cotton rags", "", 100),
         ("Thin armor", "", 100),
         ("Gambeson", "", 100),
         ("Chain mail", "", 100),
         ("Cuirass", "", 100),
         ("Plated armor", "", 100)]


def summon_menu(player):
    choice = ""
    while choice != "exit":
        print_shop(player)
        print(player.name + "'s crystals: " + str(player.crystals))

        choice = input("Make a selection (gear type): ").lower()

        if choice == "weapon":
            buy(player, 0)

        if choice == "special":
            buy(player, 1)

        elif choice == "armor":
            buy(player, 2)

    return


def print_shop(player):
    i = 0
    for gear_type in player.gear:
        if player.gear_level[i] < len(gear_type) - 1:
            print(gear_type[i][0].ljust(20, ".") + str(gear_type[i][2]) + " crystals")
            print("    " + gear_type[i][1])
        else:
            print("--Max gear achieved--")
        i += 1

    if player.gear_level[i] < len(armor) - 1:
        print(armor[i + 1][0].ljust(20, ".") + str(armor[i][2]) + " crystals")
        # print("    " + gear_type[i][1])

    print("[Exit]\n")


def buy(player, choice):
    if choice == len(player.gear_level) - 1:  # Armor
        if player.crystals >= armor[len(player.gear_level) - 1][2]:
            player.gear_level[choice] += 1
            player.crystals -= armor[len(player.gear_level) - 1][2]
        else:
            print("You don't have enough crystals!")
    else:
        if player.crystals >= player.gear[choice][player.gear_level[choice]][2]:
            player.gear_level[choice] += 1
            player.crystals -= player.gear[choice][player.gear_level[choice]][2]
        else:
            print("You don't have enough crystals!")

