from random import randint
import entity
import mobs
import player_classes


# Generates a new mob
def generate_mob(floor):
    mob_class = mobs.floor_mobs[floor - 1][randint(0, len(mobs.floor_mobs[floor - 1]) - 1)]
    new_mob = entity.Mob(floor, mob_class)

    return new_mob


# Player turn
def player_turn(player, mob):
    action = ""
    while action not in player.actions:  # TODO: add other actions
        action = input("What will " + player.name + " do?\n").lower()
    if action == player.actions[0].lower():  # Standard weapon
        critical = randint(1, 100)  # Checks if hit is critical
        if "might" not in player.status:  # If warrior's Might is not enabled, lose stamina
            if player.stamina > 0 and player.player_class[0] != "Healer":
                player.stamina -= int(player.level * 1.75)
            elif player.mana > 0 and player.player_class[0] == "Healer":
                player.mana -= int(player.level * 1.75)
        else:
            player.status.remove("might")
        if "axe" in player.status:
            damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 4)) / 5)
            player.status.remove("axe")
        else:
            damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) / 5)
        if critical <= player.player_perks[0]:
            print("Critical hit!")
            if "focus" in player.status:
                damage *= 10
            else:
                damage *= 5
        if player.stamina <= 0 and "might" not in player.status:  # Stamina penalty
            print("WARNING: Stamina is too low! Damage is halved.")
            damage = int(damage / 2)
        if player.mana <= 0:
            print("WARNING: Mana is too low! Damage is halved.")
            damage = int(damage / 2)
        if damage <= 0:
            damage = 1
        mob.hp -= damage
        print(player.name + " attacks " + mob.name + " with " + player.actions[0] + " for " + str(damage) +
              " damage!")
    if action == player.actions[1].lower():  # Special Weapon
        if player.player_class[0] == "Warrior":  # Axe
            critical = randint(1, 100)  # Checks if hit is critical
            if "might" not in player.status:  # If warrior's Might is not enabled, lose stamina
                if player.stamina > 0:
                    player.stamina -= int(player.level * 1.75) * 5
            else:  # Disables might after skipping stamina check
                player.status.remove("might")
            if "axe" in player.status:
                damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 4)) / 10)
                player.status.remove("axe")
            else:
                damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) / 10)
            if critical <= player.player_perks[0]:
                print("Critical hit!")
                damage *= 5
            if player.stamina <= 0 and "might" not in player.status:  # Stamina penalty
                print("WARNING: Stamina is too low! Damage is halved.")
                damage = int(damage / 2)
            if damage <= 0:
                damage = 1
            mob.hp -= damage
            print(player.name + " attacks " + mob.name + " with " + player.actions[1] + " for " + str(damage) +
                  " damage!")
            player.status.append("axe")
        elif player.player_class[0] == "Archer":  # Crossbow
            if "focus" not in player.status:
                critical = randint(1, 50)  # Crit chance doubled
            else:
                critical = randint(1, 100)
            if player.stamina > 0:
                player.stamina -= int(player.level * 1.75) * 2
            damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) / 5)
            if critical <= player.player_perks[0]:  # Crit damage doubled
                print("Critical hit!")
                damage *= 10
            if player.stamina <= 0:  # Stamina penalty
                print("WARNING: Stamina is too low! Damage is halved.")
                damage = int(damage / 2)
            if damage <= 0:
                damage = 1
            mob.hp -= damage
            print(player.name + " attacks " + mob.name + " with " + player.actions[1] + " for " + str(damage) +
                  " damage!")
        elif player.player_class[0] == "Healer":  # Poison
            if "Psn" in mob.status or "WeakPsn" in mob.status or "CritPsn" in mob.status:
                print("Mob already poisoned!")  # TODO: Edit so this doesn't waste a turn
            else:
                critical = randint(1, 100)
                player.mana -= player.level * 5
                if player.mana <= 0:
                    if critical <= player.player_perks[0]:
                        mob.status.append("Psn")
                        print("Critical hit!")
                    else:
                        mob.status.append("WeakPsn")
                    print("WARNING: Poison less effective due to low Mana!")
                else:
                    if critical <= player.player_perks[0]:
                        mob.status.append("CritPsn")
                        print("Critical hit!")
                    else:
                        mob.status.append("Psn")
                print(player.name + " poisoned " + mob.name + "!")
                mob.counter = 3
        elif player.player_class[0] == "Thief":  # Dash
            critical = randint(1, 100)
            if player.stamina >= int(player.level * 1.75):
                player.stamina -= int(player.level * 1.75)
                if critical <= player.player_perks[0]:
                    reduction = int(player.level * 1.75 * 2) + 1
                else:
                    reduction = int(player.level * 1.75) + 1
            else:
                print("WARNING: Dash less effective due to low stamina!")
                if critical <= player.player_perks[0]:
                    reduction = int(player.level * 1.75) + 1
                else:
                    reduction = int(player.level * 1.75 / 2) + 1
            mob.stamina -= reduction
            mob.mana -= reduction
            print(player.name + " reduced " + mob.name + "'s Stamina and Mana by " + str(reduction) + "!")

    return player, mob


# Mob turn
def mob_turn(player, mob):
    damage = int((mob.power * (mob.level + 1) - (player.defense * (player.level + 1) / 2)) / 5)
    if damage <= 0:
        damage = 1
    player.hp -= damage
    print(mob.name + " attacks " + player.name + " for " + str(damage) + " damage!")

    return player, mob


# Levels up the player
def level_up(player):
    perk_choice = ""
    player.level += 1
    player.xp -= player.max_xp
    print(player.name + " leveled up to Level " + str(player.level) + "!")
    while perk_choice not in ["critical", "hp", "mana", "stamina", "power", "defense", "speed"]:
        perk_choice = input("Choose a stat to upgrade: Critical, HP, Mana, Stamina, Power, Defense, Speed\n").lower()
    if perk_choice == "critical":
        player.player_perks[0] += 5
    elif perk_choice == "hp":
        player.player_perks[1] += 1
    elif perk_choice == "mana":
        player.player_perks[2] += 1
    elif perk_choice == "stamina":
        player.player_perks[3] += 1
    elif perk_choice == "power":
        player.player_perks[4] += 1
    elif perk_choice == "defense":
        player.player_perks[5] += 1
    elif perk_choice == "speed":
        player.player_perks[6] += 1
    else:
        print("An error has occurred. Adding perk to HP.")
        player.player_perks[1] += 1

    return player


# Gives crystals and xp to the player
def get_crystals_xp(player, mob):
    crystals_gained = randint(mob.xp_yield / 2, mob.xp_yield * 2)
    if crystals_gained <= 0:
        crystals_gained = 1
    player.crystals += crystals_gained
    print(player.name + " found " + str(crystals_gained) + " crystals!")
    player.xp += mob.xp_yield
    print(player.name + " earned " + str(mob.xp_yield) + " XP!")
    if player.xp >= player.max_xp:
        player = level_up(player)

    player.set_stats()

    return player


# Asks player if they want to advance floors
def get_floor(player, floor):
    will_continue = ""
    while will_continue != "y" and will_continue != "yes" and will_continue != "n" and will_continue != "no":
        will_continue = input("Would you like to move to the next floor?\nYou can't return if you do. Y/N\n").lower()
    if will_continue == "y" or will_continue == "yes":
        floor += 1
        print(player.name + " has reached Floor " + str(floor) + ".")

    return floor


# Main game loop
def game(player):
    floor = 1
    print(player.name + " has reached Floor " + str(floor) + ".")
    while player.hp > 0:
        mob = generate_mob(floor)  # Generates the mob for the floor

        print("Level " + str(mob.level) + " " + mob.name + " appeared!")
        while mob.hp > 0 and player.hp > 0:  # Checks to ensure neither player or mob have died

            # Sets turn order
            if player.speed > mob.speed:
                turn_order = 0
            elif mob.speed > player.speed:
                turn_order = 1
            else:
                turn_order = randint(0, 1)

            # Decides who attacks first
            if turn_order == 0:
                player_turn(player, mob)
                if mob.hp > 0:
                    turn_results = mob_turn(player, mob)
                    player = turn_results[0]
                    mob = turn_results[1]
            elif turn_order == 1:
                mob_turn(player, mob)
                if player.hp > 0:
                    turn_results = player_turn(player, mob)
                    player = turn_results[0]
                    mob = turn_results[1]
                    print(str(mob.hp))
            if mob.hp > 0 and ("Psn" in mob.status or "CritPsn" in mob.status or "WeakPsn" in mob.status):
                if "Psn" in mob.status:
                    damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) * 0.08) + 1
                    mob.hp -= damage
                    mob.counter -= 1
                    print(mob.name + " took " + str(damage) + " Poison damage!")
                    if mob.counter <= 0:
                        mob.status.remove("Psn")
                elif "CritPsn" in mob.status:
                    damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) * 0.16) + 1
                    mob.hp -= damage
                    mob.counter -= 1
                    print(mob.name + " took " + str(damage) + " Poison damage!")
                    if mob.counter <= 0:
                        mob.status.remove("CritPsn")
                elif "WeakPsn" in mob.status:
                    damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) * 0.04) + 1
                    mob.hp -= damage
                    mob.counter -= 1
                    print(mob.name + " took " + str(damage) + " Poison damage!")
                    if mob.counter <= 0:
                        mob.status.remove("WeakPsn")

        if mob.hp <= 0:
            print("Level " + str(mob.level) + " " + mob.name + " was defeated!")
            player = get_crystals_xp(player, mob)
            floor = get_floor(player, floor)

    print("Game over!")
