#Constants:
EMPTY = ' '
PLAYER = 'X'
COMPUTER = 'O'

#Global variables:
mainBoard = []

'''
@brief check if a space is available
@param pos - the position to check
'''
def spaceIsFree(pos):
    return mainBoard[pos] == EMPTY

'''
@brief print out the current status of mainBoard
'''
def printBoard():
    print('    _____________')
    print('(1) | ' + mainBoard[1] + ' | ' +mainBoard[2]+ ' | ' + mainBoard[3]+ ' |')
    print('    -------------')
    print('(4) | ' + mainBoard[4] + ' | ' +mainBoard[5]+ ' | ' + mainBoard[6]+ ' |')
    print('    -------------')
    print('(7) | ' + mainBoard[7] + ' | ' +mainBoard[8]+ ' | ' + mainBoard[9]+ ' |')
    pass

'''
@brief
    check if any possible line for a winner
@param
    board = the board to check
    le    = the player to check for a winner
'''
def isWinner(board, le) -> bool:
    #check the columns:
    for i in range(1,4):
        if board[i]==le and board[i+3]==le and board[i+6]==le:
            return True

    #check the rows
    for i in range(1, 8, 3):
        #print(i)
        if board[i] == le and board[i + 1] == le and board[i + 2] == le:
            return True

    #check the diagonals
    if board[1]==le and board[5]==le and board[9]==le:
        return True

    if board[3] == le and board[5] == le and board[7] == le:
        return True

    return False

'''
@brief handles player moves
'''
def playerMove():
    moveString = input("Please select a position (1-9): ")
    move = 0

    validPos: bool = moveString.isnumeric()
    
    if validPos:
        move = int(moveString)
        validPos = (move >= 1) and (move <= 9) and mainBoard[move] == ' '

    while not validPos:
        moveString = input("Invalid selection, try again (1-9): ")

        if not moveString.isnumeric():
            validPos = False
            continue

        move = int(moveString)

        if move < 1 or move > 9:
            validPos = False
            continue

        validPos = mainBoard[move] == ' '

    mainBoard[move] = PLAYER
'''
@brief handles computer movies
'''
def compMove():
    """
    this expression enumerates the board.
    Letter - iterates through the board where letter == ' '
    x - the index in the board, skipping the 0th
    assigns this list of indexes to possibleMoves
    """
    possibleMoves = [x for x, letter in enumerate(mainBoard) if letter == ' ' and x != 0]

    # if we can't find a move, return 0
    move = 0

    # first check if there is a move that makes us a winner, or the player a winner
    for let in ['O', 'X']:
        for i in possibleMoves:
            # if we don't include the [:], boardCopy will be assigned the reference of 'board'
            boardCopy = mainBoard[:]
            boardCopy[i] = let
            if isWinner(boardCopy, let):
                return i

    cornersOpen = []
    for i in possibleMoves:
        if i in [1,3,7,9]:
            cornersOpen.append(i)

    # if there is a corner open, chose a random one
    if len(cornersOpen) > 0:
        move = selectRandom(cornersOpen)
        return move

    # if the center is open
    if 5 in possibleMoves:
        move = 5
        return move

    # find the available edge moves
    edgesOpen = []
    for i in possibleMoves:
        if i in [2,4,6,8]:
            edgesOpen.append(i)

    # if there is an available edge, chose that for the move
    if len(edgesOpen) > 0:
        move = selectRandom(edgesOpen)

    return move

def selectRandom(board):
    import random

    return random.choice(board)

def isBoardFull() -> bool:
    return mainBoard.count(' ') <= 1

def playGame():
    print("Welcome to Tic Tac Toe!","You are player X, the computer is player O", sep="\n")
    printBoard()

    #player will be an X
    while not isBoardFull():
        playerMove()

        if isWinner(mainBoard, "X"):
            printBoard()
            print("You win!")
            break

        move = compMove()
        mainBoard[move] = COMPUTER

        if move == 0:
            printBoard()
            print("Tie game!")
            break

        if isWinner(mainBoard, "O"):
            printBoard()
            print("Sorry, O\'s won the game!")
            break

        printBoard()

'''
Script starts here.
'''
play = True
while play:
    mainBoard = [EMPTY for x in range(10)]
    playGame()
    playAgain = input("Play again? (y/n) ")
    play = playAgain.lower() == "y"
