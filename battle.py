from random import randint
import actions
import entity
import mobs
import status


# TODO: Make save file that can be loaded

# Generates a new mob
def generate_mob(floor):
    mob_class = mobs.floor_mobs[floor - 1][randint(0, len(mobs.floor_mobs[floor - 1]) - 1)]
    new_mob = entity.Mob(floor, mob_class)

    return new_mob


# Player turn
def player_turn(player, mob):
    # TODO: Change the way stats are printed
    # Prints player stats
    print("[" + player.name + "]\nHP: " + str(player.hp) + "/" + str(player.max_hp) + "\nMana: " +
          str(player.mana) + "/" + str(player.max_mana) + "\nStamina: " + str(player.stamina) + "/" +
          str(player.max_stamina))

    # Prints mob stats
    print("[" + mob.name + "]\nHP: " + str(mob.hp) + "/" + str(mob.max_hp) + "\nMana: " + str(mob.mana) +
          "/" + str(mob.max_mana) + "\nStamina: " + str(mob.stamina) + "/" + str(mob.max_stamina) + "\n")

    turn_results = None
    turn_complete = False
    while not turn_complete:  # TODO: add other actions
        print("Actions:", *player.actions)
        action = input("What will " + player.name + " do?\n").lower()
        if action == player.actions[0].lower():  # Standard Weapon
            turn_results = actions.player_action_zero(player, mob)  # Go to action zero function
            turn_complete = True
        if action == player.actions[1].lower():  # Special Weapon

            # Ensures Healer hasn't already poisoned
            if "Psn" in mob.status or "WeakPsn" in mob.status or "CritPsn" in mob.status:
                print("Mob already poisoned!")
            else:
                turn_results = actions.player_action_one(player, mob)
                turn_complete = True
        if action == player.actions[2].lower():  # Ability
            turn_results = actions.player_action_two(player, mob)
            turn_complete = True

        # TODO: These functions :3
        # if action == "summon:
            # Summon function goes here
        # if action == "help":
            # help function goes here

    return turn_results


# Mob turn
def mob_turn(player, mob):  # TODO: Make mob attacks unique and cost stamina/mana
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
    while will_continue != "up" and will_continue != "down" and will_continue != "stay":  # Allows player to choose
        will_continue = input("Would you like to move up, down, or stay?\n").lower()

        # Player goes down
        if floor == 1 and will_continue == "down":  # Player can't go down
            print("Can't go any lower!")
            will_continue = ""

    # Player goes up
    if will_continue == "up":
        floor += 1
        print(player.name + " has reached Floor " + str(floor) + ".")

    # Player goes down
    elif will_continue == "down":
        floor -= 1
        print(player.name + " has returned to Floor " + str(floor) + ".")

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
            if turn_order == 0:  # Player goes first
                player_turn(player, mob)
                if mob.hp > 0:
                    turn_results = mob_turn(player, mob)
                    player = turn_results[0]
                    mob = turn_results[1]
            elif turn_order == 1:  # Mob goes first
                mob_turn(player, mob)
                if player.hp > 0:
                    turn_results = player_turn(player, mob)
                    player = turn_results[0]
                    mob = turn_results[1]

            # If mob is poisoned
            if mob.hp > 0 and mob.counter[0] != 0:
                mob = status.get_poison_damage(player, mob)

            if player.mana < 0:
                player.mana = 0
            if player.stamina < 0:
                player.stamina = 0
            if mob.mana < 0:
                mob.mana = 0
            if mob.stamina < 0:
                mob.stamina = 0

        if mob.hp <= 0:  # Mob is defeated
            print("Level " + str(mob.level) + " " + mob.name + " was defeated!")
            player = get_crystals_xp(player, mob)
            floor = get_floor(player, floor)

    print("Game over!")
