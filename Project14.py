# Tic tac toe (X-O) game

board = [" " for _ in range(9)]

def display_board():
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]}")
    print("---|---|---")
    print(f" {board[3]} | {board[4]} | {board[5]}")
    print("---|---|---")
    print(f" {board[6]} | {board[7]} | {board[8]}")

def make_change(player):
    while True:
        pos = int(input(f"\nPlayer {player}, enter your choice (1-9): ")) - 1
        if board[pos] == " ":
            board[pos] = player
            break
        else:
            print("\nThis position is already taken. Try again.")

def winner(player):
    win_pos = [
        [0,1,2], [3,4,5], [6,7,8],
        [0,3,6], [1,4,7], [2,5,8],
        [0,4,8], [2,4,6]
    ]

    for pos in win_pos:
        if board[pos[0]] == player and board[pos[1]] == player and board[pos[2]] == player:
            return True
    
    return False

def check_full():
    return " " not in board

def game():
    current_player = "x"
    while True:
        display_board()
        make_change(current_player)
        if winner(current_player):
            display_board()
            print(f"\nPlayer {current_player} wins!")
            break
        elif check_full():
            display_board()
            print("\nIt's a tie!")
            break
        
        current_player = "o" if current_player == "x" else "x"

# Starting game
game()