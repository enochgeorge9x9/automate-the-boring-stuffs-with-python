theBoard = { 'top-L' : ' ' , 'top-M' : ' ', 'top-R' : ' ',
                     'mid-L' : ' ' , 'mid-M' : ' ', 'mid-R' : ' ',
                     'low-L' : ' ' , 'low-M' : ' ', 'low-R' : ' '}


def printBoard(board):
    print(theBoard['top-L'] + '   I  ' + theBoard['top-M'] + 'I  ' + theBoard['top-R'])
    print(' --+--+-- ')
    print(theBoard['mid-L'] + '   I  ' + theBoard['mid-M'] + 'I  ' + theBoard['mid-R'])
    print(' --+--+-- ')
    print(theBoard['low-L'] + '   I  ' + theBoard['low-M'] + 'I  ' + theBoard['low-R'])
    

turn ='X'
for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn+ '. Move on which space?'+  '(top-L,M or R, mid-L,M or R, low-L,M or R)')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'
        
printBoard(theBoard)
