import math

# Initialize the board
def initialize_board():
    return [['-' for _ in range(3)] for _ in range(3)]

# Check for a win
def check_win(board, player):
    win_conditions = [
        # Horizontal
        [board[0][0], board[0][1], board[0][2]],
        [board[1][0], board[1][1], board[1][2]],
        [board[2][0], board[2][1], board[2][2]],
        # Vertical
        [board[0][0], board[1][0], board[2][0]],
        [board[0][1], board[1][1], board[2][1]],
        [board[0][2], board[1][2], board[2][2]],
        # Diagonal
        [board[0][0], board[1][1], board[2][2]],
        [board[0][2], board[1][1], board[2][0]],
    ]
    return [player, player, player] in win_conditions

# Check for a draw
def check_draw(board):
    return all(cell != '-' for row in board for cell in row)

# Minimax algorithm
def minimax(board, depth, is_maximizing):
    if check_win(board, 'X'):
        return -10
    if check_win(board, 'O'):
        return 10
    if check_draw(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = '-'
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == '-':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = '-'
                    best_score = min(score, best_score)
        return best_score

# Find the best move
def find_best_move(board):
    best_move = None
    best_score = -math.inf
    for row in range(3):
        for col in range(3):
            if board[row][col] == '-':
                board[row][col] = 'O'
                move_score = minimax(board, 0, False)
                board[row][col] = '-'
                if move_score > best_score:
                    best_score = move_score
                    best_move = (row, col)
    return best_move

# Display the board
def print_board(board):
    for row in board:
        print(' '.join(row))
    print()

# Play the game
def play_game():
    board = initialize_board()
    while True:
        # Human player move
        print_board(board)
        row = int(input("Enter row (0, 1, 2): "))
        col = int(input("Enter column (0, 1, 2): "))
        if board[row][col] == '-':
            board[row][col] = 'X'
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, 'X'):
            print_board(board)
            print("You win!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

        # AI move
        print("AI is making a move...")
        move = find_best_move(board)
        if move:
            board[move[0]][move[1]] = 'O'
        if check_win(board, 'O'):
            print_board(board)
            print("AI wins!")
            break
        if check_draw(board):
            print_board(board)
            print("It's a draw!")
            break

# Run the game
play_game()
