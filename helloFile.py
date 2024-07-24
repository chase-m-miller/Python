helloFile = open('.\\etc\\hello.txt')
helloContent = helloFile.read()
print(str(helloContent))
helloFile.close()
