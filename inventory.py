def printInventory(inventory):
    totalItems = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalItems += v
    print('Total items: ' + str(totalItems))


def addToInventory(inventory, addedItems):
    for item in addedItems:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 1)
    return inventory


stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
inv = {'gold coin': 42, 'rope': 1}


printInventory(stuff)
print()
addToInventory(inv, dragonLoot)
printInventory(inv)
