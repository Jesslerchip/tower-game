# Handles poison damage
def get_poison_damage(player, mob):
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


# Handles potion healing
def get_potion_health(player):
    player.counter[0] += 1  # Increments heal counter
    heal_amount = int(player.max_hp / player.counter[0])
    player.hp += heal_amount
    if player.hp > player.max_hp:  # Ensures Healer's hp doesn't exceed their max hp
        player.hp = player.max_hp
    print("Healed " + player.name + " for " + str(heal_amount) + " HP!")

    return player
