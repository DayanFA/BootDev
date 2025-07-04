from collections import defaultdict
def count_enemies(enemy_names):
    enemies_dict = defaultdict(int)
    for enemy_name in enemy_names:
        enemies_dict[enemy_name] += 1
    return enemies_dict
