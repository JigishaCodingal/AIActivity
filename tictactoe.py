def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board, player):
    for row in board:
        if all(s == player for s in row):
            return True
    for col in zip(*board):
        if all(s == player for s in col):
            return True
    if all(board[i][i] == player for i in range(3)):
        return True
    if all(board[i][2 - i] == player for i in range(3)):
        return True
    return False

def is_full(board):
    return all(cell != " " for row in board for cell in row)

def main():
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Player {current_player}, enter row and column (0-2): ").split())
            if board[row][col] != " ":
                print("Cell already taken, try again.")
                continue
            board[row][col] = current_player
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            if is_full(board):
                print_board(board)
                print("It's a tie!")
                break
            current_player = "O" if current_player == "X" else "X"
        except (ValueError, IndexError):
            print("Invalid input, please enter row and column as two numbers between 0 and 2.")

if __name__ == "__main__":
    main()
