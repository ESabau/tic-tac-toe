board = ["-", "-", "-", "-", "-", "-", "-", "-", "-"]
currentPlayer = "X"
winner = None
gameRunning = True


#printing the board
def printBoard(board):
    print(" | " + board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(" -------------")
    print(" | " + board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(" -------------")
    print(" | " + board[6] + " | " + board[7] + " | " + board[8] + " | \n" ) 


#take player input
def playerChoice(board):
    inpt = int(input("\nEnter a number from 1 - 9 : "))
    if inpt >= 1 and inpt <= 9 and board[inpt-1] == "-":
        board[inpt-1] = currentPlayer;
    else:
        print("\n NU POTI ALEGE ACEASTA CASUTA")
        playerChoice(board)

#check for win or tie
def checkHorizontal(board):
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[5] == board[4] and board[3] != "-":
        winner = board[3]
        return True 
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True 
    
def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True 
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True 

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True 

def checkTie(board):
    global gameRunning
    if "-" not in board:
        printBoard(board)
        print("Tie")
        gameRunning = False

def checkWin():
    global gameRunning
    if(checkDiagonal(board) or checkHorizontal(board) or checkRow(board)):
        print(f"The winner is {winner} \n")
        printBoard(board)
        gameRunning = False

#switch the player
def switchPlayer():
    global currentPlayer
    if gameRunning == True:
        if currentPlayer == "X":
            currentPlayer = "O"
            print(" Player O is moving \n ")
        else:
            currentPlayer = "X"
            print("Player X is moving \n")
        




while gameRunning:
    printBoard(board)
    playerChoice(board)
    checkWin()
    checkTie(board)
    switchPlayer()
