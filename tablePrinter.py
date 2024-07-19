#! python3
tableData = [['apples', 'oranges', 'cherries', 'banana'],
             ['Alice', 'Bob', 'Carol', 'David'],
             ['dogs', 'cats', 'moose', 'goose']]


def printTable(table):
    # Create a list entry for each column in table
    colWidths = [0] * len(table)
    # Find the longest word in each column
    for column in range(len(table)):
        for entry in range(len(table[column])):
            if len(table[column][entry]) > colWidths[column]:
                colWidths[column] = len(table[column][entry])
    for row in range(len(table[0])):
        for column in range(len(table)):
            print(table[column][row].rjust(colWidths[column]), end=' ')
        print()


printTable(tableData)
