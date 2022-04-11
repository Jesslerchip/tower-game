import battle
import player_data
import entity
import player_data


def choose_class():
    chosen_class = None
    class_choice = ""
    while class_choice != "warrior" and class_choice != "archer" and class_choice != "healer" \
            and class_choice != "thief":
        print("Classes: Warrior, Archer, Healer, Thief\n")
        class_choice = input("What class are you?\n").lower()
    if class_choice == "warrior":
        chosen_class = player_data.warrior
    elif class_choice == "archer":
        chosen_class = player_data.archer
    elif class_choice == "healer":
        chosen_class = player_data.healer
    elif class_choice == "thief":
        chosen_class = player_data.thief
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
