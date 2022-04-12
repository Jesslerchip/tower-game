import battle
from player_data import warrior, archer, healer, thief, necromage
import entity


def choose_class():
    chosen_class = None
    class_choice = ""
    while class_choice != "warrior" and class_choice != "archer" and class_choice != "healer" \
            and class_choice != "thief" and class_choice != "necromage":
        print("Classes: Warrior, Archer, Healer, Thief, Necromage\n")
        class_choice = input("What class are you?\n").lower()
    if class_choice == "warrior":
        chosen_class = warrior
    elif class_choice == "archer":
        chosen_class = archer
    elif class_choice == "healer":
        chosen_class = healer
    elif class_choice == "thief":
        chosen_class = thief
    elif class_choice == "necromage":
        chosen_class = necromage
    else:
        print("Error: Invalid Class.")

    return chosen_class


def create_player():  # Creates a new player
    name = input("What is your name?\n")
    chosen_class = choose_class()
    new_player = entity.Player(name, chosen_class)
    new_player.set_stats()

    return new_player


player = create_player()
battle.game(player)
