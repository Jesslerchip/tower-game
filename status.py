# Handles poison damage
def get_poison_damage(player, mob):
    if "Psn" in mob.status:  # Normal Poison
        damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) * 0.08)
        if damage < 1:
            damage = 1
        mob.hp -= damage
        mob.counter[0] -= 1  # Subtract from Poison counter
        print(mob.name + " took " + str(damage) + " Poison damage!")
        if mob.counter[0] <= 0:
            mob.status.remove("Psn")
            print("Poison removed!")
    elif "CritPsn" in mob.status:  # Critical Poison
        damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) * 0.16)
        if damage < 1:
            damage = 1
        mob.hp -= damage
        mob.counter[0] -= 1  # Subtract from Poison counter
        print(mob.name + " took " + str(damage) + " Poison damage!")
        if mob.counter[0] <= 0:
            mob.status.remove("CritPsn")
            print("Poison removed!")
    elif "WeakPsn" in mob.status:  # Weak Poison
        damage = int((player.power * (player.level + 1) - (mob.defense * (mob.level + 1) / 2)) * 0.04)
        if damage < 1:
            damage = 1
        mob.hp -= damage
        mob.counter[0] -= 1  # Subtract from Poison counter
        print(mob.name + " took " + str(damage) + " Poison damage!")
        if mob.counter[0] <= 0:
            mob.status.remove("WeakPsn")
            print("Poison removed!")

    return mob


# Handles potion healing
def get_potion_health(entity):
    entity.counter[0] += 1  # Increments heal counter
    heal_amount = int(entity.max_hp / entity.counter[0])
    entity.hp += heal_amount
    if entity.hp > entity.max_hp:  # Ensures Healer's hp doesn't exceed their max hp
        entity.hp = entity.max_hp
    print("Healed " + entity.name + " for " + str(heal_amount) + " HP!")

    return entity
