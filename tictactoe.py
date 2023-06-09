import random
import copy

board = [' ' for x in range(10)]


# Title: printBoard(board)
def printBoard(board):
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('----------')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('----------')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])


# Title: clearBoard(board)
def clearBoard(board):
    for i in range(10):
        board[i] = ' '


# Title: isFreeSpace(position)
def isFreeSpace(position):
    return board[position] == ' '


# Title: isBoardFul(Board)
def isBoardFull(board):
    if board.count(' ') == 1:
        return True
    else:
        return False


# Title: insertLetter(letter, position)
def insertLetter(letter, position):
    board[position] = letter


# Title: playerMove(player)
def playerMove(player):
    continueTurn = True
    while continueTurn:
        playerMove = input(player + ' select your move (1-9): ')
        try:
            playerMove = int(playerMove)
            if playerMove > 0 and playerMove < 10:
                if isFreeSpace(playerMove):
                    insertLetter(player, playerMove)
                    continueTurn = False
                else:
                    print("Please choose an empty space")
            else:
                print("Please enter a number 1-9")
        except ValueError:
            print('Please enter a number 1-9')

# Title: checkWinner(board, letter)
def checkWinner(board, letter):
    if ((board[1] == letter and board[2] == letter and board[3] == letter) or
        (board[4] == letter and board[5] == letter and board[6] == letter) or
        (board[7] == letter and board[8] == letter and board[9] == letter) or

        (board[1] == letter and board[4] == letter and board[7] == letter) or
        (board[2] == letter and board[5] == letter and board[8] == letter) or
        (board[3] == letter and board[6] == letter and board[9] == letter) or

        (board[1] == letter and board[5] == letter and board[9] == letter) or
            (board[3] == letter and board[5] == letter and board[7] == letter)):
        return True
    else:
        return False

# Title: getOpenSpaces(board)
def getOpenSpaces(board):
    availMoves = []
    for x, letter in enumerate(board):
        if board[x] == ' ' and x != 0:
            availMoves.append(x)
    return availMoves


# Title: computerMove(completter)
def computerMove(completter):
    possibleMoves = getOpenSpaces(board)
    move = 0
    while True:
        if completter == 'X':
            testLetters = ['X', 'O']
        else:
            testLetters = ['O', 'X']

        for letter in (testLetters):
            for x in possibleMoves:
                boardCopy = copy.copy(board)
                boardCopy[x] = letter
                if checkWinner(boardCopy, letter):
                    move = x
                    insertLetter(completter, move)
                    print('Computer moved to space ' + str(move))
                    return
        if 5 in possibleMoves:
            if testLetters[1]:
                move = 5
                insertLetter(completter, move)
                print('Computer moved to space ' + str(move))
                break
        openCorners = []
        for x in possibleMoves:
            if x in [1, 3, 7, 9]:
                openCorners.append(x)
        if openCorners:
            move = random.choice(openCorners)
            insertLetter(completter, move)
            print('Computer moved to space ' + str(move))
            break
        else:
            openEdges = []
            for x in possibleMoves:
                if x in [2, 4, 6, 8]:
                    openEdges.append(x)
            move = random.choice(openEdges)
            insertLetter(completter, move)
            print('Computer moved to space ' + str(move))
            break


# Title: gameOver()
def gameOver():
    while True:
        playAgain = input('Would you like to play again (y/n): ')
        if playAgain.upper() not in ('Y', 'N', 'YES', 'NO'):
            print("Enter yes or no (y/n)")
            continue
        else:
            if playAgain.upper() in ('Y', 'YES'):
                return True
            else:
                return False


# Title: Main()
def main():
    gameState = True
    print('Use numbers 1-9 to place your X\'s or O\'s.')
    print(' ' + '1' + ' | ' + '2' + ' | ' + '3')
    print('----------')
    print(' ' + '4' + ' | ' + '5' + ' | ' + '6')
    print('----------')
    print(' ' + '7' + ' | ' + '8' + ' | ' + '9')
    while gameState:
        while True:
            player = input('\nWould you like to be X or O: ')
            if player.upper() not in ('X', 'O'):
                continue
            else:
                player = player.upper()
                if player == 'X':
                    computer = 'O'
                    break
                else:
                    computer = 'X'
                    break
        while True:
            playerTurn = input('\nWould you like to go first? Y or N: ')
            if playerTurn.upper() not in ('Y', 'N'):
                continue
            else:
                playerTurn = playerTurn.upper()
                if playerTurn == 'Y':
                    while not (isBoardFull(board)):
                        if not checkWinner(board, computer):
                            playerMove(player)
                            printBoard(board)
                        else:
                            print(computer + ' is the winner')
                            clearBoard(board)
                            gameState = gameOver()
                            break
                        if not checkWinner(board, player):
                            if isBoardFull(board):
                                break
                            else:
                                computerMove(computer)
                                printBoard(board)
                        else:
                            print(player + ' is the winner')
                            clearBoard(board)
                            gameState = gameOver()
                            break
                else:
                    while not (isBoardFull(board)):

                        if not checkWinner(board, player):

                            if isBoardFull(board):
                                break
                            else:
                                computerMove(computer)
                                printBoard(board)
                        else:
                            print(player + ' is the winner')
                            clearBoard(board)
                            gameState = gameOver()
                            break
                        if not checkWinner(board, computer):
                            if isBoardFull(board):
                                break
                            else:
                                playerMove(player)
                                printBoard(board)
                        else:
                            print(computer + ' is the winner')
                            clearBoard(board)
                            gameState = gameOver()
                            break
            break
        if isBoardFull(board):
            printBoard(board)
            print('Its a tie! The board is full')
            clearBoard(board)
            gameState = gameOver()


main()


