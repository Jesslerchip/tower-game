from random import randint
import entity
import mobs


# Generates a new mob
def generate_mob(floor):
    mob_class = mobs.floor_mobs[floor - 1][randint(0, len(mobs.floor_mobs[floor - 1]) - 1)]
    new_mob = entity.Mob(floor, mob_class)

    return new_mob


def player_action_zero(player, mob):  # If player chooses action zero
    if "focus" in player.status:  # Checks if archer has focus enabled
        critical = randint(1, 50)
    else:
        critical = randint(1, 100)  # Checks if hit is critical
    if "might" not in player.status:  # If warrior's Might is not enabled, lose stamina

        # Checks if player should lose mana or stamina
        if player.stamina > 0 and player.player_class[0] != "Healer":
            player.stamina -= int(player.level * 1.75)
        elif player.mana > 0 and player.player_class[0] == "Healer":
            player.mana -= int(player.level * 1.75)
    else:  # If warrior's Might is enabled, don't lose stamina and remove might status
        player.status.remove("might")

    # If warrior's axe was used last turn, change the damage formula and remove the axe status
    if "axe" in player.status:
        damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 4)) / 5)
        player.status.remove("axe")
    else:
        damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) / 5)

    # Checks if player got a critical
    if critical <= player.player_perks[0]:
        print("Critical hit!")
        if "focus" in player.status:  # Checks if archer used focus
            damage *= 10
        else:
            damage *= 5
    # Penalizes going below stamina/mana minimum
    if player.stamina <= 0:
        print("WARNING: Stamina is too low! Damage is halved.")
        damage = int(damage / 2)
    if player.mana <= 0:
        print("WARNING: Mana is too low! Damage is halved.")
        damage = int(damage / 2)
    if damage <= 0:  # Makes sure damage is always greater than 0
        damage = 1
    mob.hp -= damage  # Mob's health is decreased
    print(player.name + " attacks " + mob.name + " with " + player.actions[0] + " for " + str(damage) +
          " damage!")

    return player, mob


def player_action_one(player, mob):  # If player chooses action one

    #  Checks to see if the player is a warrior
    if player.player_class[0] == "Warrior":  # Axe
        critical = randint(1, 100)  # Checks if hit is critical
        if "might" not in player.status:  # If warrior's Might is not enabled, lose stamina
            if player.stamina > 0:
                player.stamina -= int(player.level * 1.75) * 5
        else:  # Disables might after skipping stamina check
            player.status.remove("might")

        # Changes damage if axe was used previous turn and removes axe status
        if "axe" in player.status:
            damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 4)) / 10)
            player.status.remove("axe")
        else:
            damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) / 10)

        # Checks if the hit is a critical
        if critical <= player.player_perks[0]:
            print("Critical hit!")
            damage *= 5
        if player.stamina <= 0:  # Stamina penalty
            print("WARNING: Stamina is too low! Damage is halved.")
            damage = int(damage / 2)
        if damage <= 0:  # Makes sure damage is always greater than 0
            damage = 1
        mob.hp -= damage  # Decreases mob's hp
        print(player.name + " attacks " + mob.name + " with " + player.actions[1] + " for " + str(damage) +
              " damage!")
        player.status.append("axe")  # adds axe to player status for the next hit

    # Checks if player class is archer
    elif player.player_class[0] == "Archer":  # Crossbow
        if "focus" not in player.status:  # Doubles crit chance if focus is enabled
            critical = randint(1, 50)
        else:
            critical = randint(1, 100)
        if player.stamina > 0:
            player.stamina -= int(player.level * 1.75) * 2
        damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) / 5)
        if critical <= player.player_perks[0]:  # Checks if player crits, crit damage doubled from crossbow
            print("Critical hit!")
            damage *= 10
        if player.stamina <= 0:  # Stamina penalty
            print("WARNING: Stamina is too low! Damage is halved.")
            damage = int(damage / 2)
        if damage <= 0:
            damage = 1
        mob.hp -= damage  # Decreases mob's hp
        print(player.name + " attacks " + mob.name + " with " + player.actions[1] + " for " + str(damage) +
              " damage!")

    # Checks if player is Healer
    elif player.player_class[0] == "Healer":
        critical = randint(1, 100)
        player.mana -= player.level * 5
        if player.mana <= 0:  # Mana penalty
            if critical <= player.player_perks[0]:  # Checks if player got crit
                mob.status.append("Psn")
                print("Critical hit!")
            else:
                mob.status.append("WeakPsn")  # Weak poison if no crit and not enough mana
            print("WARNING: Poison less effective due to low Mana!")
        else:  # No mana penalty
            if critical <= player.player_perks[0]:  # Checks if player got crit
                mob.status.append("CritPsn")
                print("Critical hit!")
            else:
                mob.status.append("Psn")
        print(player.name + " poisoned " + mob.name + "!")
        mob.counter[0] = 3  # Sets the poison counter on mob
    elif player.player_class[0] == "Thief":
        critical = randint(1, 100)
        if player.stamina >= int(player.level * 1.75):
            player.stamina -= int(player.level * 1.75)
            if critical <= player.player_perks[0]:
                reduction = int(player.level * 1.75) + 1
            else:
                reduction = int(player.level * 1.75 / 2) + 1
        else:
            print("WARNING: Dash less effective due to low stamina!")
            if critical <= player.player_perks[0]:
                reduction = int(player.level * 1.75 / 2) + 1
            else:
                reduction = int(player.level * 1.75 / 4) + 1
        mob.stamina -= reduction
        mob.mana -= reduction
        print(player.name + " reduced " + mob.name + "'s Stamina and Mana by " + str(reduction) + "!")

    return player, mob


def player_action_two(player, mob):  # If player chooses action two
    # Checks if player is warrior
    if player.player_class[0] == "Warrior":  # Might
        player.speed -= 1
        if player.speed <= 0:  # Ensures speed never drops below 1
            player.speed = 1
        player.mana -= int(player.level * 1.75 * 2)
        if player.mana <= 0:  # Checks if player has enough mana
            print("WARNING: Low Mana! Chance of ability failure!")
            coin = randint(0, 1)  # Flips a coin to decide if ability works
            if coin == 0:
                print("Ability succeeded!")
                player.status.append("Might")
                print(player.name + " activated Might!")
            else:
                print("Ability failed!")
        else:  # Player had enough mana
            player.status.append("Might")
            print(player.name + " activated Might!")

    # Checks if player is Archer
    elif player.player_class[0] == "Archer":  # Focus
        player.defense = int(player.defense / 2)
        if player.defense <= 0:  # Ensures player defense never drops below 1
            player.defense = 1
        player.mana -= int(player.level * 1.75 * 2)
        if player.mana <= 0:  # Checks if player has enough mana
            print("WARNING: Low Mana! Chance of ability failure!")
            coin = randint(0, 1)  # Flips a coin to decide if ability works
            if coin == 0:
                print("Ability succeeded!")
                player.status.append("Focus")
                print(player.name + " activated Focus!")
            else:
                print("Ability failed!")
        else:  # Player has enough mana
            player.status.append("Focus")
            print(player.name + " activated Focus!")

    # Checks if player is Healer
    elif player.player_class[0] == "Healer":  # Potion
        player.mana -= int(player.level * 1.75)
        player.stamina -= int(player.level * 1.75)
        if player.mana <= 0 or player.stamina <= 0:  # Checks if player has enough mana
            print("WARNING: Low Mana or Stamina! Chance of ability failure!")
            coin = randint(0, 1)  # Flips a coin to see if ability works
            if coin == 0:
                print("Ability succeeded!")
                player.counter[0] += 1  # Increments heal counter
                heal_amount = int(player.max_hp / player.counter[0])
                player.hp += heal_amount
                if player.hp > player.max_hp:  # Ensures Healer's hp doesn't exceed their max hp
                    player.hp = player.max_hp
                print("Healed " + player.name + " for " + str(heal_amount) + " HP!")
            else:
                print("Ability failed!")
        else:  # Player had enough mana and stamina
            player.counter[0] += 1  # Increments heal counter
            heal_amount = int(player.max_hp / player.counter[0])
            player.hp += heal_amount
            if player.hp > player.max_hp:  # Ensures Healer's hp doesn't exceed their max hp
                player.hp = player.max_hp
            print("Healed " + player.name + " for " + str(heal_amount) + " HP!")

    # Checks if player is Thief
    elif player.player_class[0] == "Thief":
        player.mana -= int(player.level * 1.75 * 2)
        if player.mana <= 0:
            print("WARNING: Low Mana! Chance of ability failure!")
            coin = randint(0, 1)  # Flips a coin to see if ability works
            if coin == 0:
                print("Ability succeeded!")
                crystals_gained = randint(mob.xp_yield / 2, mob.xp_yield * 2)  # Calculates crystal yield
                if crystals_gained <= 0:  # Ensures a crystal is always stolen
                    crystals_gained = 1
                player.crystals += crystals_gained  # Gives player crystals
                print(player.name + " stole " + str(crystals_gained) + " crystals!")
            else:
                print("Ability failed!")
        else:  # Player has enough mana
            crystals_gained = randint(mob.xp_yield / 2, mob.xp_yield * 2)
            if crystals_gained <= 0:
                crystals_gained = 1
            player.crystals += crystals_gained
            print(player.name + " stole " + str(crystals_gained) + " crystals!")

    return player, mob


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
            turn_results = player_action_zero(player, mob)  # Go to action zero function
            turn_complete = True
        if action == player.actions[1].lower():  # Special Weapon

            # Ensures Healer hasn't already poisoned
            if "Psn" in mob.status or "WeakPsn" in mob.status or "CritPsn" in mob.status:
                print("Mob already poisoned!")
            else:
                turn_results = player_action_one(player, mob)
                turn_complete = True
        if action == player.actions[2].lower():  # Ability
            turn_results = player_action_two(player, mob)
            turn_complete = True

    return turn_results


def get_poison_damage(player, mob):  # Handles poison damage
    if "Psn" in mob.status:  # Normal Poison
        damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) * 0.08) + 1
        mob.hp -= damage
        mob.counter[0] -= 1  # Subtract from Poison counter
        print(mob.name + " took " + str(damage) + " Poison damage!")
        if mob.counter[0] <= 0:
            mob.status.remove("Psn")
            print("Poison removed!")
    elif "CritPsn" in mob.status:  # Critical Poison
        damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) * 0.16) + 1
        mob.hp -= damage
        mob.counter[0] -= 1  # Subtract from Poison counter
        print(mob.name + " took " + str(damage) + " Poison damage!")
        if mob.counter[0] <= 0:
            mob.status.remove("CritPsn")
            print("Poison removed!")
    elif "WeakPsn" in mob.status:  # Weak Poison
        damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) * 0.04) + 1
        mob.hp -= damage
        mob.counter[0] -= 1  # Subtract from Poison counter
        print(mob.name + " took " + str(damage) + " Poison damage!")
        if mob.counter[0] <= 0:
            mob.status.remove("WeakPsn")
            print("Poison removed!")

    return mob


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
                mob = get_poison_damage(player, mob)

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
