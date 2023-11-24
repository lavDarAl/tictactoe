def board_func():
    # Initialize the game board
    board =[[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    return board

def display_board(board):
    # Display the game board
    for i in range(len(board)):
        print(" |".join(board[i]))

def get_move(currentPlayer):
    # Get the move from the current player
   
    move = input("Enter the coordinates for your move, " + currentPlayer + ": ")
    return move


def update_board(board, move, currentPlayer):
    # Update the game board with the current player's move
    row, col = map(int, move.split())
    board[row][col] = currentPlayer
    return board

def hasWon(board, currentPlayer):
    if board[0][0] == currentPlayer and board[0][1] == currentPlayer and board[0][2] == currentPlayer:
        return True
    elif board[1][0] == currentPlayer and board[1][1] == currentPlayer and board[1][2] == currentPlayer:
        return True
    elif board[2][0] == currentPlayer and board[2][1] == currentPlayer and board[2][2] == currentPlayer:
        return True
    elif board[0][0] == currentPlayer and board[1][0] == currentPlayer and board[2][0] == currentPlayer:
        return True
    elif board[0][1] == currentPlayer and board[1][1] == currentPlayer and board[2][1] == currentPlayer:   
        return True     
    elif board[0][2] == currentPlayer and board[1][2] == currentPlayer and board[2][2] == currentPlayer:    
        return True
    elif board[0][0] == currentPlayer and board[1][1] == currentPlayer and board[2][2] == currentPlayer:
        return True
    elif board[0][2] == currentPlayer and board[1][1] == currentPlayer and board[2][0] == currentPlayer:
        return True
    else:
        return False
    
def isDraw(board):
    # Check if the game is a draw
    if board[0][0] != " " and board[0][1] != " " and board[0][2] != " " and board[1][0] != " " and board[1][1] != " " and board[1][2] != " " and board[2][0] != " " and board[2][1] != " " and board[2][2] != " ":
        return True
    else:
        return False

def switchPlayer(currentPlayer):
    # Switch the current player
    if currentPlayer == "X":
        currentPlayer = "O" 
    else:
        currentPlayer = "X"
    return currentPlayer

def isValid(board, move):
    # Check if the move is valid
    row, col = map(int, move.split())
    if board[row][col] == " ":
        return True
    else:
        return False

if __name__ == "__main__":

    over = True
    currentPlayer = input("Enter the name of the first player: ").upper()

    # Check if the player name is valid
    while currentPlayer != "X" and currentPlayer != "O":
        print("Invalid player name. Please enter X or O.")
        currentPlayer = input("Enter the name of the first player: ").upper()
        

    print("Welcome to Tic Tac Toe, " + currentPlayer + "!")
    board = board_func()

    while over:
        display_board(board)
        move = get_move(currentPlayer)
        while not isValid(board, move):
            print("Invalid move. Please try again.")
            move = get_move(currentPlayer)
        board = update_board(board, move, currentPlayer)

        if hasWon(board, currentPlayer):
            display_board(board)
            print(currentPlayer + " has won the game!")
            over = False

        if isDraw(board):
            display_board(board)
            print("The game is a draw!")
            over = False
        currentPlayer = switchPlayer(currentPlayer)        


    
    