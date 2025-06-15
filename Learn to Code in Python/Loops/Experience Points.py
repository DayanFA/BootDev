def calculate_experience_points(level):
    f = lambda level: sum(x * 5 for x in range(1, level))
    return f(level)