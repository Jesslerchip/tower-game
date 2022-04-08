from random import randint
import entity
import mobs


# Generates a new mob
def generate_mob():  # TODO: Make a mob list to pull from instead of test mob
    test_mob = entity.Mob("Goblin", 10, 10, 10, 10, 10, 10)
    entity.Mob.set_stats(test_mob)

    return test_mob


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


# Mob turn
def mob_turn(player, mob):
    damage = mob.power - player.defense
    if damage <= 0:
        damage = 1
    player.hp -= damage
    print(mob.name + " attacks " + player.name + " for " + str(damage) + " damage!")


# Main game loop
def game(player):
    floor = 0
    while player.hp > 0:
        floor += 1
        mob = generate_mob()  # Generates the mob for the floor
        player.set_stats()

        print("Floor " + str(floor))
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
                    mob_turn(player, mob)
            elif turn_order == 1:
                mob_turn(player, mob)
                if player.hp > 0:
                    player_turn(player, mob)

        print("Level " + str(mob.level) + " " + mob.name + " was defeated!")

    print("Game over!")
