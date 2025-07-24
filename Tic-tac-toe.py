# # TIC-TAC-TOE AI GAME: Human vs AI (Minimax)

import math

# Initial empty board
board = [" " for _ in range(9)]

# Print the board
def print_board():
    print()
    for i in range(3):
        row = board[i*3:(i+1)*3]
        print(" | ".join(row))
        if i < 2:
            print("--+---+--")
    print()

# Check winner
def check_winner(brd):
    win_combos = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),
        (0, 3, 6), (1, 4, 7), (2, 5, 8),
        (0, 4, 8), (2, 4, 6)
    ]
    for a, b, c in win_combos:
        if brd[a] == brd[b] == brd[c] and brd[a] != " ":
            return brd[a]
    if " " not in brd:
        return "Draw"
    return None

# Human move
def human_move():
    while True:
        move = input("Enter your move (1-9): ")
        if move.isdigit():
            move = int(move) - 1
            if 0 <= move < 9 and board[move] == " ":
                board[move] = "X"
                break
            else:
                print("Invalid move! Try again.")
        else:
            print("Please enter a number between 1-9.")

# AI move using Minimax
def ai_move():
    best_score = -math.inf
    best_move = None
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i
    board[best_move] = "O"

# Minimax Algorithm
def minimax(brd, is_maximizing):
    result = check_winner(brd)
    if result == "X":
        return -1
    elif result == "O":
        return 1
    elif result == "Draw":
        return 0

    if is_maximizing:
        best = -math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "O"
                score = minimax(brd, False)
                brd[i] = " "
                best = max(best, score)
        return best
    else:
        best = math.inf
        for i in range(9):
            if brd[i] == " ":
                brd[i] = "X"
                score = minimax(brd, True)
                brd[i] = " "
                best = min(best, score)
        return best

# Game loop
def play_game():
    print("Welcome to Tic-Tac-Toe AI (You: X, AI: O)")
    print_board()

    while True:
        human_move()
        print_board()
        winner = check_winner(board)
        if winner:
            break

        print("AI is thinking...")
        ai_move()
        print_board()
        winner = check_winner(board)
        if winner:
            break

    if winner == "Draw":
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

# Run game
play_game()