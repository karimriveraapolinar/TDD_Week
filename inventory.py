def add_item(inventory, item):
    if not item:
        raise ValueError("Item name cannot be empty")
    if len(inventory["items"]) == inventory["capacity"]:
        raise ValueError("No room left in inventory")
    if inventory["locked"]:
        return inventory
    inventory["items"].append(item)
    return inventory


def remove_item(inventory, item):
    if item not in inventory["items"]:
        raise ValueError("That item isn't in your inventory")
    if inventory["locked"] is True:
        return inventory
    inventory["items"].pop(inventory["items"].index(item))
    return inventory


def get_item_count(inventory):
    return len(inventory["items"])
