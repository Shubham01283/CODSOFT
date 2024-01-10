import math

def print_board(board):
    # Function to print the Tic Tac Toe board
    for row in board:
        print(" ".join(row))
    print()

def is_winner(board, player):
    # Check if a player has won by examining rows, columns, and diagonals
    for i in range(3):
        if all(cell == player for cell in board[i]) or all(board[j][i] == player for j in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2 - i] == player for i in range(3)):
        return True

    return False

def is_full(board):
    # Check if the board is full
    return all(cell != ' ' for row in board for cell in row)

def evaluate(board):
    # Evaluate the current state of the board
    if is_winner(board, 'O'):
        return 1
    elif is_winner(board, 'X'):
        return -1
    elif is_full(board):
        return 0
    else:
        return None

def minimax(board, depth, maximizing_player, alpha, beta):
    # Minimax algorithm with alpha-beta pruning
    score = evaluate(board)

    if score is not None:
        return score

    if maximizing_player:
        max_eval = float('-inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'O'
                    eval = minimax(board, depth + 1, False, alpha, beta)
                    board[i][j] = ' '
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break  # Beta cut-off
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(3):
            for j in range(3):
                if board[i][j] == ' ':
                    board[i][j] = 'X'
                    eval = minimax(board, depth + 1, True, alpha, beta)
                    board[i][j] = ' '
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break  # Alpha cut-off
        return min_eval

def find_best_move(board):
    # Find the best move for the computer using the minimax algorithm
    best_val = float('-inf')
    best_move = None

    for i in range(3):
        for j in range(3):
            if board[i][j] == ' ':
                board[i][j] = 'O'
                move_val = minimax(board, 0, False, float('-inf'), float('inf'))
                board[i][j] = ' '

                if move_val > best_val:
                    best_move = (i, j)
                    best_val = move_val

    return best_move

def play_tic_tac_toe():
    # Main function to play Tic Tac Toe
    board = [[' ' for _ in range(3)] for _ in range(3)]
    game_over = False

    while not game_over:
        print_board(board)

        # Player's move
        row = int(input("Enter row (0, 1, or 2): "))
        col = int(input("Enter column (0, 1, or 2): "))

        if board[row][col] == ' ':
            board[row][col] = 'X'
        else:
            print("Cell already occupied. Try again.")
            continue

        # Check if player wins
        if is_winner(board, 'X'):
            print_board(board)
            print("You win!")
            game_over = True
            break

        # Check for a tie
        if is_full(board):
            print_board(board)
            print("It's a tie!")
            game_over = True
            break

        # Computer's move
        print("Computer's move:")
        best_move = find_best_move(board)
        board[best_move[0]][best_move[1]] = 'O'

        # Check if computer wins
        if is_winner(board, 'O'):
            print_board(board)
            print("Computer wins!")
            game_over = True
            break

    print("Game Over")

if __name__ == "__main__":
    play_tic_tac_toe()
