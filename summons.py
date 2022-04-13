import strings

# Warrior Gear
warrior_slot_1 = [("Rusted Sword", "(Standard)", 100, strings.rusted_sword_desc),
                  ("Iron Shortsword", "(Standard)", 100, strings.iron_shortsword_desc)]

warrior_slot_2 = [("Blunt Axe", "(Special)", 100, strings.blunt_axe_desc),
                  ("Hatchet", "(Special)", 100, strings.hatchet_desc)]
warrior_gear = [warrior_slot_1, warrior_slot_2]

# Archer Gear
archer_slot_1 = [("Bent Longbow", "(Standard)", 100, strings.bent_longbow_desc),
                 ("Reinforced Longbow", "(Standard)", 100, strings.reinforced_longbow_desc,)]
archer_slot_2 = [("Crooked Crossbow", "(Special)", 100, strings.crooked_crossbow_desc,),
                 ("Precise Crossbow", "(Special)", 100, strings.precise_crossbow_desc)]
archer_gear = [archer_slot_1, archer_slot_2]

# Healer Gear
healer_slot_1 = [("Weakened Curse", "(Standard)", 100, strings.weakened_curse_desc),
                 ("Dark Hex", "(Standard)", 100, strings.dark_hex_desc)]
healer_slot_2 = [("Poison Berries", "(Special)", 100, strings.poison_berries_desc),
                 ("Belladonna", "(Special)", 100, strings.belladonna_desc)]
healer_gear = [healer_slot_1, healer_slot_2]

# Thief Gear
thief_slot_1 = [("Pocketknife", "(Standard)", 100, strings.pocketknife_desc),
                ("Sharp Dagger", "(Standard)", 100, strings.sharp_dagger_desc)]
thief_slot_2 = [("Magic Sandals", "(Special)", 100, strings.magic_sandals_desc),
                ("Leather Boots", "(Special)", 100, strings.leather_boots_desc)]
thief_gear = [thief_slot_1, thief_slot_2]

# Necromage Gear
necromage_slot_1 = [("Paper Athame", "(Standard)", 100, strings.paper_athame_desc),
                    ("Bloody Athame", "(Standard)", 100, strings.bloody_athame_desc)]
necromage_slot_2 = [("Straw", "(Special)", 100, strings.straw_desc),
                    ("Orange", "(Special)", 100, strings.orange_desc)]
necromage_gear = [necromage_slot_1, necromage_slot_2]

# Armor
armor = [("Cotton Rags", "", 100),
         ("Thin Armor", "", 100),
         ("Gambeson", "", 100),
         ("Chainmail", "", 100),
         ("Cuirass", "", 100),
         ("Plated Armor", "", 100)]


# Menu fo choose a summon
def summons_menu(player):
    choice = ""
    while choice != "exit":
        print_shop(player)
        print(f"{player.name}'s crystals: {player.crystals}")

        choice = input("Make a selection (gear type): ").lower()

        if choice == "standard":
            buy(player, 0)

        if choice == "special":
            buy(player, 1)

        elif choice == "armor":
            buy(player, 2)

    return


# Prints the available items
def print_shop(player):
    i = 0
    for gear_type in player.gear:
        if player.gear_level[i] < len(gear_type) - 1:
            print(f"{gear_type[i][0]} {gear_type[i][1]}".ljust(30, ".") + f"{gear_type[i][2]} crystals")
            print("    " + gear_type[i][3])
        else:
            print("--Max gear achieved--")
        i += 1

    if player.gear_level[i] < len(armor) - 1:
        print(f"{armor[i + 1][0]}".ljust(30, ".") + f"{armor[i][2]} crystals")
        # print("    " + gear_type[i][1])

    print("[Exit]\n")


# Player selects an item to buy
def buy(player, choice):
    if choice == len(player.gear_level) - 1:  # Armor
        if player.crystals >= armor[len(player.gear_level) - 1][2]:
            player.gear_level[choice] += 1
            player.crystals -= armor[len(player.gear_level) - 1][2]
        else:
            print(strings.not_enough_crystals)
    else:
        if player.crystals >= player.gear[choice][player.gear_level[choice]][2]:
            player.gear_level[choice] += 1
            player.crystals -= player.gear[choice][player.gear_level[choice]][2]
        else:
            print(strings.not_enough_crystals)
