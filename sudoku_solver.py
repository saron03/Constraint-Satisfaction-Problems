# sudoku_solver.py
# Solves a 9x9 Sudoku puzzle using Constraint Satisfaction Problem (CSP) concepts
# and a backtracking algorithm. Variables are empty cells, domains are values 1-9,
# and constraints ensure each value is unique in its row, column, and 3x3 box.
# Written by: 
#       Saron Yitbareck 
#       UGR/3774/15


from typing import List, Tuple

# Define the initial 9x9 Sudoku grid (0 represents empty cells)
sudoku_board = [
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

# Find the next empty cell (variable) to assign a value
def find_empty_cell(board: List[List[int]]) -> Tuple[int, int] | None:
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                return (row, col)
    return None  # No empty cells remain

# Check if a value satisfies Sudoku constraints (unique in row, column, and 3x3 box)
def is_valid_choice(board: List[List[int]], row: int, col: int, guess: int) -> bool:
    # Check row for duplicates
    if guess in board[row]:
        return False

    # Check column for duplicates
    if guess in [board[r][col] for r in range(9)]:
        return False

    # Check 3x3 box for duplicates
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for r in range(start_row, start_row + 3):
        for c in range(start_col, start_col + 3):
            if board[r][c] == guess:
                return False

    return True

# Solve the Sudoku puzzle using recursive backtracking
def solve_sudoku(board: List[List[int]]) -> bool:
    # Base case: If no empty cells remain, the puzzle is solved
    next_cell = find_empty_cell(board)
    if not next_cell:
        return True

    row, col = next_cell

    # Try each value in the domain (1-9)
    for digit in range(1, 10):
        if is_valid_choice(board, row, col, digit):
            board[row][col] = digit  # Assign the value
            if solve_sudoku(board):  # Recursively solve the rest
                return True
            board[row][col] = 0  # Backtrack if solution fails

    return False  # No valid value found, trigger backtracking

# Print the Sudoku board in a formatted grid with 3x3 box separators
def print_board(board: List[List[int]]) -> None:
    print("Solved Sudoku Puzzle:")
    for i, row in enumerate(board):
        if i > 0 and i % 3 == 0:
            print("-" * 21)  # Horizontal separator for 3x3 boxes
        row_str = ""
        for j, val in enumerate(row):
            if j > 0 and j % 3 == 0:
                row_str += "| "  # Vertical separator for 3x3 boxes
            row_str += f"{val} "
        print(row_str.rstrip())

# Solve the puzzle and display the result
if solve_sudoku(sudoku_board):
    print_board(sudoku_board)
else:
    print("No solution found.")