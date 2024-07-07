number = 42

def doLocal():
    number = 27

doLocal()
print(number)

def doGlobal():
    global number
    number = 10

doGlobal()
print(number)
