def add_points(game, amount):
    if amount < 0:
        raise ValueError("Please enter a positive number")
    elif game["active"] == False:
        return game
    else:
        game["score"] += (amount * game["multiplier"])
        return

def apply_multiplier(game, multiplier):
    if multiplier < 1:
        raise ValueError("Multiplier must be greater than or equal to 1")
    elif game["active"] == False:
        return game
    else:
        game["multiplier"] = multiplier
        return game

def reset_score(game):
    pass

def is_high_score(game, threshold):
    pass
