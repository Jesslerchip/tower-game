import battle
import entity
from tkinter import *

import player_data


def create_player(name, player_class):  # Attempts to set class. If successful, creates player entity and starts game
    if name == "":
        my_label.config(text="You need a name!")
    else:
        player_class = player_class.lower()
        chosen_class = class_dict.get(player_class)
        if chosen_class in player_data.class_list:
            new_player = entity.Player(name, chosen_class)
            new_player.set_stats()
            mainframe.destroy()
            battle.game(new_player)
        else:
            my_label.config(text="Invalid class!")


class_dict = {"warrior": player_data.warrior, "archer": player_data.archer, "healer": player_data.healer,
              "thief": player_data.thief, "necromage": player_data.necromage}  # Dictionary for class names

main = Tk()
main.title("Tower Game")

mainframe = Frame(main)
mainframe.pack(padx=5, pady=5)

Label(mainframe, text="Enter your name:").pack(padx=5, pady=5)
name_entry = Entry(mainframe)
name_entry.pack(padx=5, pady=5)

Label(mainframe, text="Enter your class:").pack(padx=5, pady=5)
class_entry = Entry(mainframe)
class_entry.pack(padx=5, pady=5)

my_label = Label(mainframe, text="", fg="red")
Button(mainframe, text="Submit", command=lambda: (create_player(name_entry.get(), class_entry.get()))).pack(padx=10,
                                                                                                            pady=10)
my_label.pack()

main.mainloop()
