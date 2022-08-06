from tkinter import *
import entity
import mob_data
import player_data


def make_player(name, player_class):
    player_class.lower()
    if player_class in ["warrior", "archer", "healer", "thief", "necromage"]:
        if name == "":
            my_label['text'] = "You need a name!"
            return
        if player_class == "warrior":
            new_player = entity.Player(name, player_data.warrior)
        elif player_class == "archer":
            new_player = entity.Player(name, player_data.archer)
        elif player_class == "healer":
            new_player = entity.Player(name, player_data.healer)
        elif player_class == "thief":
            new_player = entity.Player(name, player_data.thief)
        else:
            new_player = entity.Player(name, player_data.necromage)

        new_player.set_stats()
        mainframe.destroy()
        battle_gui(new_player)
    else:
        my_label['text'] = "Invalid class."


def hit(hp, button, mob):
    mob.hp -= 1
    if mob.hp <= 0:
        button['state'] = DISABLED
    hp.set("HP: " + str(mob.hp) + "/" + str(mob.max_hp))

    return hp


def battle_gui(player):
    battle_main = Frame(main)
    battle_main.pack(padx=5, pady=5)

    new_mob = entity.Mob(1, mob_data.goblin)
    mob_hp = StringVar(battle_main, ("HP: " + str(new_mob.hp) + "/" + str(new_mob.max_hp)))

    p_name_label = Label(battle_main, text="Name: " + player.name, fg="gray11")
    p_name_label.grid(row=0, column=0, sticky=W)

    p_class_label = Label(battle_main, text="Class: " + player.player_class[0], fg="gray11")
    p_class_label.grid(row=0, column=1, sticky=W)

    p_hp_label = Label(battle_main, text="hp: " + str(player.hp) + "/" + str(player.max_hp), fg="gray11")
    p_hp_label.grid(row=0, column=2, sticky=W)

    p_mana_label = Label(battle_main, text="mana: " + str(player.mana) + "/" + str(player.max_mana), fg="gray11")
    p_mana_label.grid(row=0, column=3, sticky=W)

    p_stamina_label = Label(battle_main, text="stamina: " + str(player.stamina) + "/" + str(player.stamina),
                            fg="gray11")
    p_stamina_label.grid(row=0, column=4, sticky=W)

    m_name_label = Label(battle_main, text="Name: " + new_mob.name, fg="gray11")
    m_name_label.grid(row=1, column=0, sticky=W)

    m_hp_label = Label(battle_main, textvariable=mob_hp, fg="green")
    m_hp_label.grid(row=1, column=2, sticky=W)

    m_mana_label = Label(battle_main, text="mana: " + str(new_mob.mana) + "/" + str(new_mob.max_mana), fg="gray11")
    m_mana_label.grid(row=1, column=3, sticky=W)

    m_stamina_label = Label(battle_main, text="stamina: " + str(new_mob.stamina) + "/" + str(new_mob.stamina),
                            fg="gray11")
    m_stamina_label.grid(row=1, column=4, sticky=W)

    button = Button(battle_main, text="Attack", command=lambda: hit(mob_hp, button, new_mob))
    button.grid(row=3, column=2, padx=5, pady=5)


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
Button(mainframe, text="Submit", command=lambda: (make_player(name_entry.get(), class_entry.get()))).pack(padx=10,
                                                                                                          pady=10)
my_label.pack()

main.mainloop()
