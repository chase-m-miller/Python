def incrementBy(n):
    return lambda a: a + n


addTwo = incrementBy(2)
print(addTwo(25))
