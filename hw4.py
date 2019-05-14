#hw4.py v1.0
#Grant Ludwig
#5/17/19

#assumes board in 9x9

import sys
import copy

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
            rowM = 8 - key[0]
            colM =8 - key[1]
            rowRange = None
            colRange = None
                #find row range
            if rowM > 5:
                rowRange = (0,2)
            elif rowM > 2:
                rowRange = (3,5)
            else:
                rowRange = (6,8)
                #find col range
            if colM > 5:
                colRange = (0,2)
            elif colM > 2:
                colRange = (3,5)
            else:
                colRange = (6,8)
            for rowI in range(rowRange[0],rowRange[1] + 1):
                for colI in range(colRange[0],colRange[1] + 1):
                    if int(board[rowI][colI]) in domainList:
                        domainList.remove(int(board[rowI][colI]))

def goodValue(domains, space, value):
    row, col = space
    for rowI in range(boardSize):
        if row != rowI and value in domains[(rowI, col)]:
            if len(domains[(rowI, col)]) > 1:
                domains[(rowI, col)].remove(value)
            else:
                return False
    for colI in range(boardSize):
        if col != colI and value in domains[(row, colI)]:
            if len(domains[(row, colI)]) > 1:
                domains[(row, colI)].remove(value)
            else:
                return False
    rowM = 8 - row
    colM = 8 - col
    rowRange = None
    colRange = None
        #find row range
    if rowM > 5:
        rowRange = (0,2)
    elif rowM > 2:
        rowRange = (3,5)
    else:
        rowRange = (6,8)
        #find col range
    if colM > 5:
        colRange = (0,2)
    elif colM > 2:
        colRange = (3,5)
    else:
        colRange = (6,8)
    for rowI in range(rowRange[0],rowRange[1] + 1):
        for colI in range(colRange[0],colRange[1] + 1):
            if row != rowI and col != colI and value in domains[(rowI, colI)]:
                if len(domains[(rowI, colI)]) > 1:
                    domains[(rowI, colI)].remove(value)
                else:
                    return False
    return True

def backTrack(domains, space, first):
    row, col = space
    if col >= boardSize:
        row = row + 1
        col = 0
    if row >= boardSize:
        return True, domains
    if first:
        first = False
        maxDomain = ((0,0), 0)
        for key in domains:
            domainSize = len(domains[key])
            if domainSize > maxDomain[1]:
                maxDomain = (key, len(domains[key]))
        print(maxDomain)

    #choose first in list
    oldDict = copy.deepcopy(domains)
    for value in domains[(row, col)]:
        if goodValue(domains, (row,col), value):
            domains[(row, col)] = [value]
            found, solution = backTrack(domains, (row,col+1), first)
            if found:
                return found, solution
            else:
                domains = copy.deepcopy(oldDict)
        else:
            domains = copy.deepcopy(oldDict)
    return False, None

#driver code
fileName = sys.argv[1]
board = readFile(fileName)
print('\n')
print('Initial Board')
print('-------------', '\n')
printBoard(board)
print('\n')
domains = buildDomains(board)
pruneDomain(domains, board)
found, solution = backTrack(domains, (0,0), True)
if found:
    print('There is a solution')
    print('-------------------', '\n')
    completeBoard = []
    for rowI in range(boardSize):
        rowList = []
        for colI in range(boardSize):
            rowList.append(str(solution[rowI, colI][0]))
        completeBoard.append(rowList)
    printBoard(completeBoard)
else:
    print('There is no solution')