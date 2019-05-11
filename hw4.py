#hw4.py v1.0
#Grant Ludwig
#5/17/19

import sys

def readFile(fileName):
    board = []
    for line in open(fileName):
        line = line.rstrip()
        board.append(line.split())
    return board

def printBoard(board):
    rowCount = 0
    for row in board:
        if rowCount == 3:
            print('---------------------')
            rowCount = 0
        output = ''
        colCount = 0
        for num in row:
            if colCount == 3:
                output += '| '
                colCount = 0
            if num == 0:
                output += '_ '
            else:
                output += str(num) + ' '
            colCount += 1
        print(output)
        rowCount += 1

#driver code
fileName = sys.argv[1]
test = readFile(fileName)
print('\n')
printBoard(test)