from random import randint
import status


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
                player = status.get_potion_health(player)
            else:
                print("Ability failed!")
        else:  # Player had enough mana and stamina
            player = status.get_potion_health(player)

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
