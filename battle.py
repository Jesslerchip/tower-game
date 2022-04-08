from random import randint
import entity
import mobs


# Generates a new mob
def generate_mob(floor):
    mob_class = mobs.floor_mobs[floor - 1][randint(0, len(mobs.floor_mobs[floor - 1]) - 1)]
    new_mob = entity.Mob(floor, mob_class)

    return new_mob


# Player turn
def player_turn(player, mob):
    action = ""
    while action.lower() != "attack":  # TODO: add other actions
        action = input("What will " + player.name + " do?\n")
        if action.lower() == "attack":
            damage = player.power - mob.defense
            if damage <= 0:
                damage = 1
            mob.hp -= damage
            print(player.name + " attacks " + mob.name + " for " + str(damage) + " damage!")

            return player, mob


# Mob turn
def mob_turn(player, mob):
    damage = mob.power - player.defense
    if damage <= 0:
        damage = 1
    player.hp -= damage
    print(mob.name + " attacks " + player.name + " for " + str(damage) + " damage!")

    return player, mob


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
        player.set_stats()

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

        if mob.hp <= 0:
            print("Level " + str(mob.level) + " " + mob.name + " was defeated!")
            floor = get_floor(player, floor)

    print("Game over!")
