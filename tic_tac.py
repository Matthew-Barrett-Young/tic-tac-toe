board = ["-", "-", "-",
         "-", "-", "-",
         "-","-","-"]

turn = 1

game_finished = False

def board_state(): #prints the current board state
    print(board[0] + " | " + board[1] + " | " + board[2] + " | ")
    print(board[3] + " | " + board[4] + " | " + board[5] + " | ")
    print(board[6] + " | " + board[7] + " | " + board[8] + " | ")

def game_start(): #begins the game and assigns the player's name to a tuple
    print("Welcome to Tic Tac Toe.\nThe first player to move will be X.")
    
    player_one = input("What is the first player's name?: ")
    player_two = input("What is the second player's name?: ")
    
    board_state()

    return player_one, player_two

def move(): #function for players to make moves

    if turn % 2 == 0: #determines which symbol to place given the turn
        symbol = "O"
    else:
        symbol = "X"

    choice = input("Please select a move. (1 through 9): ")
    
    while choice not in ["1","2","3","4","5","6","7","8","9"] or board[int(choice)-1] != "-": #ensures valid move
        choice = input("Please make a valid selection. (1 through 9): ")
    
    board[int(choice)-1] = symbol

    return symbol

def game_over(symbol): #function to check if game has been completed

    if turn % 2 == 0: #determines who the winning player is
        winner = player_names[0]
    
    else:
        winner = player_names[1]

    if turn == 10: #determined if the game has finished
        print("It's a tie!")
        return True
    
    elif board[0] + board[1] + board[2] == symbol*3:
        print(winner +" wins!!!")
        return True
    
    elif board[3] + board[4] + board[5] == symbol*3:
        print(winner +" wins!!!")
        return True

    elif board[6] + board[7] + board[8] == symbol*3:
        print(winner +" wins!!!")
        return True
    
    elif board[0] + board[4] + board[8] == symbol*3:
        print(winner +" wins!!!")
        return True
    
    elif board[6] + board[4] + board[2] == symbol*3:
        print(winner +" wins!!!")
        return True
    
    elif board[0] + board[3] + board[6] == symbol*3:
        print(winner +" wins!!!")
        return True

    elif board[1] + board[4] + board[7] == symbol*3:
        print(winner +" wins!!!")
        return True
    
    elif board[2] + board[5] + board[8] == symbol*3:
        print(winner +" wins!!!")
        return True

    else:
        return False

player_names = game_start()

while game_finished != True:
    symbol = move()
    board_state()
    turn += 1
    game_finished = game_over(symbol)
    

