import battle
import entity


def create_player():
    name = input("What is your name?\n")
    chosen_class = entity.basic_class
    new_player = entity.Player(name, chosen_class)

    return new_player


player = create_player()
battle.game(player)
