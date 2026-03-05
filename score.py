def add_points(game, amount):
    if amount < 0:
        raise ValueError("Please enter a positive number")
    elif game["active"] == False:
        return game
    else:
        game["score"] += (amount * game["multiplier"])
        return game
def apply_multiplier(game, multiplier):
    pass

def reset_score(game):
    pass

def is_high_score(game, threshold):
    pass
