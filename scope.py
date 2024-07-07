word = 'global'

def doLocal():
    word = 'Altered by: doLocal'

def doGlobal():
    global word
    word = 'Altered by: doGlobal'

doLocal()
print(word)

doGlobal()
print(word)
