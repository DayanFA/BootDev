def check_ingredient_match(recipe, ingredients):
    have_count = 0
    missing = []
    for item in recipe:
        if item in ingredients:
            have_count += 1
        else:
            missing.append(item)
    percentage = (have_count / len(recipe)) * 100
    return percentage, missing