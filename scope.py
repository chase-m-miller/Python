word = 'global'

def doLocal():
    word = 'Altered by: doLocal'

def doGlobal():
    global word
    word = 'Altered by: doGlobal'

def printLocal():
    word = 'local'
    print(word)

def printGlobal():
    print(word)

doLocal()
print(word)

doGlobal()
print(word)

printLocal()
printGlobal()
