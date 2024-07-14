spam = ['apples', 'bananas', 'tofu', 'cats']
spam2 = ['dog']

def printList(list):
    if len(list) == 1:
        print(list[0])
        return

    for i in list:
        if i == list[len(list) - 1]:
            print('and ' + i)
            break
        print(i, end=', ')

printList(spam)
printList(spam2)
