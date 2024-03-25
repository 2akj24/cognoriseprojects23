def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))

def find_empty_location(board, empty_spot):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                empty_spot[0], empty_spot[1] = row, col
                return True
    return False

def is_valid_move(board, row, col, num):
    return (not used_in_row(board, row, num) and
            not used_in_col(board, col, num) and
            not used_in_box(board, row - row % 3, col - col % 3, num))

def used_in_row(board, row, num):
    return num in board[row]

def used_in_col(board, col, num):
    return any(row[col] == num for row in board)

def used_in_box(board, start_row, start_col, num):
    for row in range(3):
        for col in range(3):
            if board[row + start_row][col + start_col] == num:
                return True
    return False

def solve_sudoku(board):
    empty_spot = [0, 0]

    if not find_empty_location(board, empty_spot):
        return True
    
    row, col = empty_spot

    for num in range(1, 10):
        if is_valid_move(board, row, col, num):
            board[row][col] = num

            if solve_sudoku(board):
                return True
            
            board[row][col] = 0
    
    return False

if __name__ == "__main__":
    # Example Sudoku board (0 represents empty cells)
    board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    print("Sudoku puzzle:")
    print_board(board)
    print("\nSolving...\n")

    if solve_sudoku(board):
        print("Sudoku solution:")
        print_board(board)
    else:
        print("No solution exists.")
