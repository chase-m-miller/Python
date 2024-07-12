catNames = []
while True:
    print('Enter the name of cat ' + str((len(catNames) + 1)) + ' (or nothing to stop):')
    name = input()
    if name == '':
        break
    else:
        catNames = catNames + [name]

print('All my cats\' names are:')
for cats in range(len(catNames)):
    print('   ' + catNames[cats])
