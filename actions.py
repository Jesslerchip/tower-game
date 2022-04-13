from random import randint
from entity import Mob
from misc import rng
from mob_data import ritual_mobs, ritual_actions
import status
import strings


def get_mods(attacker, defender_mods):
    if "Axe0" in attacker.status:
        defender_mods[0] = 0.5
        attacker.status.remove("Axe0")
    elif "Axe1" in attacker.status:
        attacker.status = list(
            map(lambda status_name: status_name.replace("Axe1", "Axe0"), attacker.status))

    return attacker, defender_mods


def get_critical(entity):
    critical = rng(100)
    if (critical < entity.perks[0]) or (critical - 50 < entity.perks[0] and "Focus" in entity.status):
        print("Critical hit!")
        mod_critical = 2
        if "Focus" in entity.status:
            entity.status.remove("Focus")
    else:
        mod_critical = 1

    return mod_critical


def get_pickpocket_crystals(attacker, defender):
    crystals = randint(int(defender.xp_yield / 2), defender.xp_yield)  # Calculates crystal yield
    if crystals <= 0:  # Ensures a crystal is always stolen
        crystals = 1
    attacker.crystals += crystals  # Gives player crystals
    print(f"{attacker.name} stole {crystals} crystals!")

    return attacker


# Calculates cost
def get_action_cost(entity, action):
    # Standard Weapon Cost
    low_stat_mod = 1
    if action[0] == entity.actions[0][0]:
        if action[1] == 0:
            if "Might" not in entity.status:
                entity.stamina -= int(entity.level * 1.75)
            else:
                entity.power += int(entity.level * 1.75)
        elif action[1] == 1:
            entity.mana -= int(entity.level * 1.75)
            # else:
            # Code for Status-Type Standard weapons will go here, if it ever exists

    # Special cost
    if action[0] == entity.actions[1][0]:

        # Player Specials
        if action[0] == "Axe":
            if "Might" not in entity.status:
                entity.stamina -= int(entity.level * 1.75 * 5)
            else:
                entity.power += int(entity.level * 1.75)
        elif action[0] == "Crossbow":
            entity.stamina -= int(entity.level * 1.75 * 2)
        elif action[0] == "Dash":
            entity.stamina -= int(entity.level * 1.75)
        elif action[0] == "Poison":
            entity.mana -= int(entity.level * 1.75)
        elif action[0] == "Pact":
            entity.hp -= int(entity.level * 1.75 * entity.power / 3)
            if entity.hp <= 0:
                entity.hp = 1

        # Mob Specials
        elif action[0] == "Scream":
            entity.mana -= int(entity.level * 1.75)
        elif action[0] == "Stomp":
            entity.stamina -= int(entity.level * 1.75) * 2
        elif action[0] == "Toxic Brew":
            entity.mana -= int(entity.level * 1.75)
            entity.stamina -= int(entity.level * 1.75)

    # Ability cost
    if action[0] == entity.actions[2][0]:

        # Player abilities
        if action[0] == "Might":
            entity.speed -= 1 * entity.level
            if entity.speed <= 0:  # Ensures Speed never drops below 1
                entity.speed = 1
            entity.mana -= int(entity.level * 1.75 * 2)
        elif action[0] == "Focus":
            entity.defense -= 2 * entity.level
            entity.stamina -= int(entity.max_stamina / 2)
            if entity.stamina < 0:
                entity.stamina = 0
            if entity.defense <= 0:  # Ensures attacker Defense never drops below 1
                entity.defense = 1
            entity.mana -= int(entity.level * 1.75 * 2)
        elif action[0] == "Potion":
            entity.mana -= int(entity.level * 1.75)
            entity.stamina -= int(entity.level * 1.75)
        elif action[0] == "Pickpocket":
            entity.mana -= int(entity.level * 1.75 * 2)
        elif action[0] == "Ritual":
            entity.mana -= int(entity.level * 1.75)
            entity.hp -= int(entity.level * 1.75 * 2)

        # Mob abilities
        elif action[0] == "Cower":
            entity.speed -= 1 * entity.level
            if entity.speed <= 0:  # Ensures Speed never drops below 1
                entity.speed = 1
        elif action[0] == "Rest":
            entity.mana -= int(entity.level * 1.75)
        elif action[0] == "Magic Broom":
            entity.mana -= int(entity.level * 1.75 * 2)
            entity.stamina -= int(entity.level * 1.75 * 2)
        elif action[0] == "Last Resort":
            entity.hp = 1
        elif action[0] == "Skill Swap":
            entity.mana -= int(entity.level * 1.75 * 2)
            entity.stamina -= int(entity.level * 1.75 * 2)

    # Checks if attacker went below stamina or mana minimum
    if entity.stamina >= 0 and entity.mana >= 0:
        low_stat_mod = 1
    if entity.stamina < 0:
        print(f"WARNING: {entity.name}'s Stamina is too low! Damage is halved. Abilities may fail.")
        entity.stamina = 0
        low_stat_mod = 0.5
    if entity.mana < 0:
        print(f"WARNING: {entity.name}'s Mana is too low! Damage is halved. Abilities may fail.")
        entity.mana = 0
        low_stat_mod = 0.5

    if "Might" in entity.status:  # Disables Might
        entity.status.remove("Might")

    return entity, low_stat_mod


# Get effects for unique actions. Standard attacks only do damage so they aren't checked
def get_action_effects(attacker, defender, action, attacker_mods):
    ritual_mob = Mob(1, ["null", 0, 0, 0, 0, 0, 0, ritual_actions])
    # If action is special

    # Player actions
    # Axe
    if action[0] == "Axe":
        attacker.status.append("Axe1")  # Axe effect will be triggered next turn
        print(f"{attacker.name}'s Axe breaks the enemy's Defenses!")

    if action[0] == "Crossbow":
        if attacker_mods[0] >= 2:
            attacker.power += attacker.level
            attacker.speed += attacker.level
            print(f"{attacker.name}'s Crossbow makes their arrows sharper and faster!")

        attacker_mods[2] = 0.75

    # Poison
    elif action[0] == "Poison":
        print(f"{defender.name} was Poisoned by {attacker.name}!")

        # Appends different poisons based on modifiers
        if attacker_mods[0] >= 2 and attacker_mods[1] == 1:
            defender.status.append("CritPsn")
            defender.counter[0] = 3
        elif (attacker_mods[0] >= 2 and attacker_mods[1] == 0.5) or (attacker_mods[0] == 1 and attacker_mods[1] == 1):
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
            print(f"{attacker.name} Dashed around and exhausted {defender.name}!")

            # Crit
            if attacker_mods[0] >= 2:
                defender.stamina -= int(attacker.level * 1.75) + 1
                defender.mana -= int(attacker.level * 1.75) + 1

            # Normal
            else:
                defender.stamina -= int(attacker.level * 1.75 / 2) + 1
                defender.mana -= int(attacker.level * 1.75 / 2) + 1
        else:
            print(strings.ability_failed)
        # Sets misc multiplier to 0 to prevent damage being dealt

        attacker_mods[2] = 0

    # Might
    elif action[0] == "Might":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            print(f"{attacker.name}'s Might gives them adrenaline and boosts attacks!")
            attacker.status.append("Might")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    elif action[0] == "Focus":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            print(f"{attacker.name} Focused on getting a Critical next turn!")
            attacker.status.append("Focus")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    elif action[0] == "Potion":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            attacker = status.get_potion_health(attacker)
        else:
            print(strings.ability_failed.format(attacker.name))
        attacker_mods[2] = 0
    elif action[0] == "Pickpocket":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            attacker = get_pickpocket_crystals(attacker, defender)
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    elif action[0] == "Pact":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            if attacker_mods[0] >= 2:
                defender.hp -= int(defender.level * 1.75 * defender.power / 3 * 2)
            else:
                defender.hp -= int(defender.level * 1.75 * defender.power / 3)
            print(f"A dark Pact drains {attacker.name} and {defender.name}'s blood!")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    elif action[0] == "Ritual":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            ritual_number = rng(5) - 1
            ritual_class = ritual_mobs[ritual_number]
            if attacker_mods[0] >= 2:
                ritual_mob = Mob(attacker.level, ritual_class)
            else:
                ritual_level = int(attacker.level / 2)
                if ritual_level <= 0:
                    ritual_level = 1
                ritual_mob = Mob(ritual_level, ritual_class)
            attacker.status.append("Ritual")
            ritual_mob.counter[1] = 5
            print(f"{attacker.name}'s Ritual summoned a Level {ritual_mob.level} {ritual_mob.name}!")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    # Mob actions

    elif action[0] == "Scream":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            if attacker_mods[0] >= 2:
                defender.power -= 2 * defender.level
            else:
                defender.power -= defender.level
            if defender.power <= 0:
                defender.power = 1
                print(f"{defender.name}'s Power has reached its minimum!")
            else:
                print(f"{attacker.name}'s Scream scared {defender.name} into submission!")
                print(f"{defender.name} lost Power!")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    elif action[0] == "Cower":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            if attacker_mods[0] >= 2:
                attacker.defense += 2 * attacker.level
            else:
                attacker.defense += attacker.level
                print(f"{attacker.name} Cowered in a protective stance!")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    elif action[0] == "Stomp":
        if attacker_mods[0] >= 2:
            defender.speed -= 2 * defender.level
        else:
            defender.speed -= 1 * defender.level
        if defender.speed <= 0:
            defender.speed = 1
            print(f"{defender.name}'s Speed has reached its minimum!")
        else:
            print(f"Stomp startled {defender.name} and slowed them down!")

    elif action[0] == "Rest":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            attacker.stamina += 5 * attacker.level
            if attacker.stamina >= attacker.max_stamina:
                attacker.stamina = attacker.max_stamina
            print(f"{attacker.name} took a Rest!")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    elif action[0] == "Toxic Brew":
        if attacker_mods[0] >= 2:
            defender.mana -= 2 * defender.level
        else:
            defender.mana -= 1 * defender.level
        if defender.mana <= 0:
            defender.mana = 0
            print(f"{defender.name}'s Mana has reached its minimum!")
        print(f"{attacker.name}'s Toxic Brew suppressed {defender.name}'s magical abilities!")

    elif action[0] == "Magic Broom":
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            defender.stamina = int(defender.stamina / 2)
            if defender.stamina <= 0:
                defender.stamina = 0
            print(f"{attacker.name} tired out {defender.name} with their Magic Broom!")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    elif action[0] == "Last Resort":
        damage = int(attacker.max_hp / 2)
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            defender.hp -= damage
            print(f"{attacker.name} is desperate! Last Resort deals {damage} damage!")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    elif action[0] == "Skill Swap":
        new_power = attacker.defense
        new_defense = attacker.power
        if attacker_mods[1] == 0.5:
            success = rng(2)
        else:
            success = 1
        if success == 1:
            defender.power = new_power
            defender.defense = new_defense
            print(f"{attacker.name}'s Skill Swap switched their Power and Defense!")
        else:
            print(strings.ability_failed.format(attacker.name))

        attacker_mods[2] = 0

    return attacker, defender, attacker_mods, ritual_mob


# Determines result of actions
def turn_action(attacker, defender, action):
    # = [crit_multiplier, low_stat_multiplier, misc_multiplier]
    attacker_mods = [1, 1, 1]  # Modifiers for attacker
    # = [defense multiplier]
    defender_mods = [1]  # Modifiers for defender

    # Handles setting multipliers
    attacker_multiplier = 1
    defender_multiplier = 1
    attacker_mods[0] = get_critical(attacker)
    action_cost = get_action_cost(attacker, attacker.actions[action])
    attacker = action_cost[0]
    attacker_mods[1] = action_cost[1]
    action_results = get_action_effects(attacker, defender, attacker.actions[action], attacker_mods)
    attacker = action_results[0]
    defender = action_results[1]
    attacker_mods = action_results[2]
    ritual_mob = action_results[3]
    extra_mods = get_mods(attacker, defender_mods)
    attacker = extra_mods[0]
    defender_mods = extra_mods[1]

    # Combines multipliers
    for i in attacker_mods:
        attacker_multiplier *= i
    for i in defender_mods:
        defender_multiplier *= i

    # If action should damage defender
    if attacker_multiplier != 0:

        # Damage formula
        damage = int(((attacker.power * attacker_multiplier * (attacker.level + 1)) -
                      (defender.defense * defender_multiplier * (defender.level + 1) / 2)) / 5)

        if damage <= 0:
            damage = 1
        defender.hp -= damage  # Defender's health is decreased
        print(f"{attacker.name} attacks {defender.name} with {attacker.actions[action][0]} for {damage} damage!")

    return attacker, defender, ritual_mob
