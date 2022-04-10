from random import randint
import actions
import entity
from misc import rng
import mobs
import status
import summons


# TODO: Make save file that can be loaded

# Generates a new mob
def generate_mob(floor):
    mob_class = mobs.floor_mobs[floor - 1][randint(0, len(mobs.floor_mobs[floor - 1]) - 1)]
    new_mob = entity.Mob(floor, mob_class)

    return new_mob


def output_stats(player, mob):
    player_header = "[" + player.name + "]"
    mob_header = "[" + mob.name + "]"
    player_health_bar = str(player.hp) + "/" + str(player.max_hp)
    mob_health_bar = str(mob.hp) + "/" + str(mob.max_hp)
    player_mana_bar = str(player.mana) + "/" + str(player.max_mana)
    mob_mana_bar = str(mob.mana) + "/" + str(mob.max_mana)
    player_stamina_bar = str(player.stamina) + "/" + str(player.max_stamina)
    mob_stamina_bar = str(mob.stamina) + "/" + str(mob.max_stamina)

    print("        " + player_header.center(10) + "|" + mob_header.center(10))
    print("HP:     " + player_health_bar.center(10) + "|" + mob_health_bar.center(10))
    print("Mana:   " + player_mana_bar.center(10) + "|" + mob_mana_bar.center(10))
    print("Stamina:" + player_stamina_bar.center(10) + "|" + mob_stamina_bar.center(10) + "\n")


def help_menu(player):
    # Weapon
    if player.player_class[0] == "Healer":
        print(player.actions[0][0] + ": Standard attack. Damage depends on power. Costs mana.")
    else:
        print(player.actions[0][0] + ": Standard attack. Damage depends on power. Costs stamina.")

    # Special
    if player.player_class[0] == "Warrior":
        print(player.actions[1][0] + ": Halves mob defense against next hit. Costs stamina.")
    elif player.player_class[0] == "Archer":
        print(player.actions[1][0] + ": Deals double damage on a crit. Costs stamina.")
    elif player.player_class[0] == "Healer":
        print(player.actions[1][0] + ": Deals 40% of hex for 3 turns. Costs mana.")
    else:
        print(player.actions[1][0] + ": Decreases enemy's stamina and mana. Costs stamina.")

    # Ability
    if player.player_class[0] == "Warrior":
        print(player.actions[2][0] + ": Decreases speed by 1, but eliminates stamina cost of next hit.")
    elif player.player_class[0] == "Archer":
        print(player.actions[2][0] + ": Decreases defense by 2, but doubles crit chance of next hit.")
    elif player.player_class[0] == "Healer":
        print(player.actions[2][0] + ": Heals the user. Healing is halved after each use. Costs mana.")
    else:
        print(player.actions[2][0] + ": Steals extra crystals, but costs mana.")

    # Summon
    print("Summon: Opens shop menu.\n")


# Player turn
def player_turn(player, mob):
    output_stats(player, mob)

    turn_results = None
    turn_complete = False
    while not turn_complete:  # TODO: add other actions
        print("Available actions:")
        for i in player.actions:
            print(i[0])
        print("Summon")
        print("Help\n")
        action = input("What will " + player.name + " do?\n").lower()
        if action == player.actions[0][0].lower():  # Standard Weapon
            turn_results = actions.player_action(player, mob, 0)  # Go to action zero function
            turn_complete = True
        if action == player.actions[1][0].lower():  # Special Weapon

            # Ensures Healer hasn't already poisoned
            if "Psn" in mob.status or "WeakPsn" in mob.status or "CritPsn" in mob.status:
                print("Mob already poisoned!")
            else:
                turn_results = actions.player_action(player, mob, 1)
                turn_complete = True
        if action == player.actions[2][0].lower():  # Ability
            turn_results = actions.player_action(player, mob, 2)
            turn_complete = True
        if action == "summon":
            summons.summon_menu(player)  # Shop
        if action == "help":
            help_menu(player)  # Help menu

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
    perk_list = ["critical", "hp", "mana", "stamina", "power", "defense", "speed"]
    perk_choice = ""
    player.level += 1
    player.xp -= player.max_xp
    print(player.name + " leveled up to Level " + str(player.level) + "!")
    while perk_choice not in perk_list:
        perk_choice = input("Choose a stat to upgrade: Critical, HP, Mana, Stamina, Power, Defense, Speed\n").lower()
    if perk_choice == "critical":
        player.player_perks[0] += 5
    else:
        player.player_perks[perk_list.index(perk_choice)] += 1

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
                turn_order = rng(2)

            # Decides who attacks first
            if turn_order == 1:  # Player goes first
                player_turn(player, mob)
                if mob.hp > 0:
                    turn_results = mob_turn(player, mob)
                    player = turn_results[0]
                    mob = turn_results[1]
            elif turn_order == 2:  # Mob goes first
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
            player.set_stats()

    print("Game over!")
