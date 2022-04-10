from random import randint
from misc import rng
import status


def get_mods(attacker, defender_mods):
    if "Axe0" in attacker.status:
        defender_mods[0] = 0.5
        attacker.status.remove("Axe0")
    elif "Axe1" in attacker.status:
        attacker.status = list(
            map(lambda status_name: status_name.replace("Axe1", "Axe0"), attacker.status))

    return attacker, defender_mods


def get_critical(entity):
    if "Focus0" in entity.status:
        critical = rng(50)
        entity.status.remove("Focus0")
    else:
        critical = rng(100)
    if critical < entity.player_perks[0]:
        print("Critical Hit!")
        if entity.action == "crossbow":
            mod_critical = 10
        else:
            mod_critical = 5
    else:
        mod_critical = 1
    if "Focus1" in entity.status:
        entity.status = list(
            map(lambda status_name: status_name.replace("Focus1", "Focus0"), entity.status))

    return mod_critical


def get_pickpocket_crystals(attacker, defender):
    print("Ability succeeded!")
    crystals = randint(defender.xp_yield / 2, defender.xp_yield * 2)  # Calculates crystal yield
    if crystals <= 0:  # Ensures a crystal is always stolen
        crystals = 1
    attacker.crystals += crystals  # Gives player crystals
    print(attacker.name + " stole " + str(crystals) + " crystals!")

    return attacker


# Calculates cost
def get_action_cost(entity, action):
    # Standard Weapon Cost
    low_stat_mod = 1
    if "Might" not in entity.status:
        if action[0] == entity.actions[0][0]:
            if action[1] == 0:
                entity.stamina -= int(entity.level * 1.75)
            elif action[1] == 1:
                entity.mana -= int(entity.level * 1.75)
            # else:
            # Code for Status-Type Standard weapons will go here, if it ever exists

    # Special cost
    if action[0] == entity.actions[1][0]:
        if action[0] == "Axe":
            if "Might" not in entity.status:
                entity.stamina -= int(entity.level * 1.75 * 5)
        elif action[0] == "Crossbow":
            entity.stamina -= int(entity.level * 1.75 * 2)
        elif action[0] == "Dash":
            entity.stamina -= int(entity.level * 1.75)
        elif action[0] == "Poison":
            entity.mana -= int(entity.level * 1.75)

    # Ability cost
    if action[0] == entity.actions[2][0]:
        if action[0] == "Might":
            if entity.speed <= 0:  # Ensures speed never drops below 1
                entity.speed = 1
            entity.mana -= int(entity.level * 1.75 * 2)
        elif action[0] == "Focus":
            entity.defense -= 2
            if entity.defense <= 0:  # Ensures player defense never drops below 1
                entity.defense = 1
            entity.mana -= int(entity.level * 1.75 * 2)
        elif action[0] == "Potion":
            entity.mana -= int(entity.level * 1.75)
            entity.stamina -= int(entity.level * 1.75)
        elif action[0] == "Pickpocket":
            entity.mana -= int(entity.level * 1.75 * 2)

    # Checks if player went below stamina or mana minimum
    if entity.stamina >= 0 and entity.mana >= 0:
        low_stat_mod = 1
    if entity.stamina < 0:
        print("WARNING: Stamina is too low! Damage is halved. Abilities may fail.")
        entity.stamina = 0
        low_stat_mod = 0.5
    if entity.mana < 0:
        print("WARNING: Mana is too low! Damage is halved. Abilities may fail.")
        entity.mana = 0
        low_stat_mod = 0.5

    if "Might" in entity.status:
        entity.status.remove("Might")

    return entity, low_stat_mod


# Gets effects for unique actions. Standard attacks only do damage so they aren't checked
def get_action_effects(attacker, defender, action, attacker_mods):
    # If action is special

    # Axe
    if action[0] == "Axe":
        attacker.status.append("Axe1")  # Axe effect will be triggered next turn
        print(attacker.name + "'s Axe halved the enemy's Defense for the next hit!")

    # Poison
    elif action[0] == "Poison":
        print(defender.name + " was Poisoned by " + attacker.name + "!")
        if attacker_mods[0] == 5 and attacker_mods[1] == 1:
            defender.status.append("CritPsn")
            defender.counter[0] = 3
        elif (attacker_mods[0] == 5 and attacker_mods[1] == 0.5) or (attacker_mods[0] == 1 and attacker_mods[1] == 1):
            defender.status.append("Psn")
            defender.counter[0] = 3
        else:
            defender.status.append("WeakPsn")
            defender.counter[0] = 3
        attacker_mods[2] = 0

    # Dash
    elif action[0] == "Dash":

        # If low_stat_mod is changed, ability may fail
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            print(attacker.name + " Dashed and reduced " + defender.name + "'s Stamina and Mana!")

            # Crit
            if attacker_mods[0] == 5 and attacker_mods[1] == 1:
                defender.stamina -= int(attacker.level * 1.75) + 1
                defender.mana -= int(attacker.level * 1.75) + 1

            # Crit and low_stat_mod, or normal
            elif (attacker_mods[0] == 5 and attacker_mods[1] == 0.5) or (
                    attacker_mods[0] == 1 and attacker_mods[1] == 1):
                defender.stamina -= int(attacker.level * 1.75 / 2) + 1
                defender.mana -= int(attacker.level * 1.75 / 2) + 1

            # no crit and low_stat_mod
            else:
                defender.stamina -= int(attacker.level * 1.75 / 4) + 1
                defender.mana -= int(attacker.level * 1.75 / 4) + 1
        else:
            print("Ability failed due to low stats!")
        # Sets misc multiplier to 0 to prevent damage being dealt
        attacker_mods[2] = 0

    # Might
    elif action[0] == "Might":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            print(attacker.name + "'s Might eliminates Stamina costs for them next turn!")
            attacker.status.append("Might")
        else:
            print("Ability failed due to low stats!")
        attacker_mods[2] = 0
    elif action[0] == "Focus":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            print(attacker.name + "'s Focus doubles their Critical chance for the next turn!")
            attacker.status.append("Focus1")
        else:
            print("Ability failed due to low stats!")
        attacker_mods[2] = 0
    elif action[0] == "Potion":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            attacker = status.get_potion_health(attacker)
        else:
            print("Ability failed due to low stats!")
        attacker_mods[2] = 0
    elif action[0] == "Pickpocket":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            attacker = get_pickpocket_crystals(attacker, defender)
        else:
            print("Ability failed due to low stats!")
        attacker_mods[2] = 0

    return attacker, defender, attacker_mods


def player_action(player, mob, action):  # If player chooses action zero

    # = [crit_multiplier, low_stat_multiplier, misc_multiplier]
    player_mods = [1, 1, 1]  # Modifiers for player

    # = [defense multiplier]
    mob_mods = [1]  # Modifiers for mobs

    # Handles setting multipliers
    player_multiplier = 1
    mob_multiplier = 1
    player_mods[0] = get_critical(player)
    action_cost = get_action_cost(player, player.actions[action])
    player = action_cost[0]
    player_mods[1] = action_cost[1]
    action_results = get_action_effects(player, mob, player.actions[action], player_mods)
    player = action_results[0]
    mob = action_results[1]
    player_mods = action_results[2]
    extra_mods = get_mods(player, mob_mods)
    player = extra_mods[0]
    mob_mods = extra_mods[1]

    # Combines multipliers
    for i in player_mods:
        player_multiplier *= i
    for i in mob_mods:
        mob_multiplier *= i

    # If action should damage mob
    if player_multiplier != 0:
        damage = int(((player.power * player_multiplier * (player.level + 1)) - (mob.defense * mob_multiplier *
                                                                                 (mob.level + 1) / 2)) / 5)
        if damage <= 0:
            damage = 1
        mob.hp -= damage  # Mob's health is decreased
        print(player.name + " attacks " + mob.name + " with " + player.actions[action][0] + " for " + str(damage) +
              " damage!")

    return player, mob
