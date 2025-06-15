def get_champion_slices(champions):
    slice1 = champions[2:]
    slice2 = champions[:-1]
    slice3 = champions[::2]
    return slice1, slice2, slice3