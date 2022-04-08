import entity


def generate_mob():
    test_mob = entity.Mob("Goblin", 10, 10, 10, 10, 10, 10)
    entity.Mob.set_stats(test_mob)

    return test_mob
