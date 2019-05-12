#hw4.py v1.0
#Grant Ludwig
#5/17/19

#assumes board in 9x9

import sys

boardSize = 9

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

def buildDomains(board):
    domainDict = {}
    for rowI in range(boardSize):
        for colI in range(boardSize):
            if board[rowI][colI] == '0':
                domainDict[(rowI,colI)] = [1,2,3,4,5,6,7,8,9]
            else:
                domainDict[(rowI,colI)] = [int(board[rowI][colI])]
    return domainDict

def pruneDomain(domains, board):
    for key in domains:
        domainList = domains[key]
        if len(domainList) != 1:
            #row
            for colI in range(boardSize):
                if int(board[key[0]][colI]) in domainList:
                    domainList.remove(int(board[key[0]][colI]))
            #col
            for rowI in range(boardSize):
                if int(board[rowI][key[1]]) in domainList:
                    domainList.remove(int(board[rowI][key[1]]))
            #square
            rowMod = key[0] % 8
            colMod = key[1] % 8
            rowRange = None
            colRange = None
                #find row range
            if rowMod > 5:
                rowRange = (0,2)
            elif rowMod > 2:
                rowRange = (3,5)
            else:
                rowRange = (6,8)
                #find col range
            if colMod > 5:
                colRange = (0,2)
            elif colMod > 2:
                colRange = (3,5)
            else:
                colRange = (6,8)
            for rowI in range(rowRange[0],rowRange[1] + 1):
                for colI in range(colRange[0],colRange[1] + 1):
                    if int(board[rowI][colI]) in domainList:
                        domainList.remove(int(board[rowI][colI]))

#driver code
fileName = sys.argv[1]
board = readFile(fileName)
print('\n')
printBoard(board)
domains = buildDomains(board)
print(domains)
print('\n')
pruneDomain(domains, board)