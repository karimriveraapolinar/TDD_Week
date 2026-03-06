import pytest
from inventory import add_item, remove_item, get_item_count


def test_add_to_empty(empty_inventory):
    result = add_item(empty_inventory, "Potion")
    assert "Potion" in result["items"]


def test_add_rejects_empty_name(empty_inventory):
    with pytest.raises(ValueError):
        add_item(empty_inventory, "")


def test_add_fails_full(full_inventory):
    with pytest.raises(ValueError):
        add_item(full_inventory, "Key")


def test_locked_ignores_add(locked_inventory):
    result = add_item(locked_inventory, "Axe")
    assert len(result["items"]) == 1


def test_remove_from_multi(empty_inventory):
    empty_inventory["items"] = ["apple", "banana", "apple"]
    result = remove_item(empty_inventory, "apple")
    assert result["items"] == ["banana", "apple"]


def test_remove_raises_missing(full_inventory):
    with pytest.raises(ValueError):
        remove_item(full_inventory, "xyz")


def test_locked_ignores_remove(locked_inventory):
    result = remove_item(locked_inventory, "sword")
    assert "sword" in result["items"]


def test_count_full(full_inventory):
    assert get_item_count(full_inventory) == 10
