import strings


# Handles poison damage
def get_poison_damage(attacker, defender):
    if "Psn" in attacker.status:  # Normal Poison
        damage = int((attacker.power * (attacker.level + 1) - (defender.defense * (defender.level + 1) / 2)) * 0.08)
        if damage < 1:
            damage = 1
        defender.hp -= damage
        defender.counter[0] -= 1  # Subtract from Poison counter
        print(strings.poison_damage.format(defender.name, damage))
        if defender.counter[0] <= 0:
            defender.status.remove("Psn")
            print(strings.poison_removed.format(defender.name))
    elif "CritPsn" in defender.status:  # Critical Poison
        damage = int((attacker.power * (attacker.level + 1) - (defender.defense * (defender.level + 1) / 2)) * 0.16)
        if damage < 1:
            damage = 1
        defender.hp -= damage
        defender.counter[0] -= 1  # Subtract from Poison counter
        print(strings.poison_damage.format(defender.name, damage))
        if defender.counter[0] <= 0:
            defender.status.remove("CritPsn")
            print(strings.poison_removed.format(defender.name))
    elif "WeakPsn" in defender.status:  # Weak Poison
        damage = int((attacker.power * (attacker.level + 1) - (defender.defense * (defender.level + 1) / 2)) * 0.04)
        if damage < 1:
            damage = 1
        defender.hp -= damage
        defender.counter[0] -= 1  # Subtract from Poison counter
        print(strings.poison_damage.format(defender.name, damage))
        if defender.counter[0] <= 0:
            defender.status.remove("WeakPsn")
            print(strings.poison_removed.format(defender.name))

    return defender


# Handles potion healing
def get_potion_health(entity):
    entity.counter[0] += 1  # Increments heal counter
    heal_amount = int(entity.max_hp / entity.counter[0])
    entity.hp += heal_amount
    if entity.hp > entity.max_hp:  # Ensures Healer's hp doesn't exceed their max hp
        entity.hp = entity.max_hp
    print(f"Healed {entity.name} for {heal_amount} HP!")

    return entity
