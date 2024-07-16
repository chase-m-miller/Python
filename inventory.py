stuff = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}


def printInventory(inventory):
    totalItems = 0
    for k, v in inventory.items():
        print(str(v) + ' ' + k)
        totalItems += v
    print('Total items: ' + str(totalItems))


printInventory(stuff)
