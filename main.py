



damage = 1
mob_hp = 5

print("Mob appeared!")

while mob_hp > 0:
    print("Mob's HP: " + str(mob_hp))
    attack = input("Attack?\n")
    if attack.lower() == "attack":
        mob_hp -= damage
        print("Mob took " + str(damage) + " damage!")

print("Mob defeated!")
