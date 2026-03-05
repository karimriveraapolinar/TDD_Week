import pytest
from score import *
def test_add_points(game,amount):
    result = add_points(game, 10)
    assert result["score"] == 20

def test_apply_multiplier(game, multiplier):
    result = apply_multiplier(game, 3)
    assert result["multiplier"] == 3

def test_reset_score(game):
    result = reset_score(game)
    assert result["score"] == 0

def test_is_high_score(game):
    result = is_high_score(game, 50)
    assert result is False
