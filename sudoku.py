# Sudoku Solver with and without Backtracking

# Backtracking Approach

def is_valid(board, row, col, num):
    # Check if num is valid in the given row, column, and 3x3 subgrid
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
        # Check 3x3 subgrid
        if board[3 * (row // 3) + i // 3][3 * (col // 3) + i % 3] == num:
            return False
    return True

def solve_sudoku_backtrack(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty cell
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number

                        if solve_sudoku_backtrack(board):  # Recursion!!
                            return True

                        board[row][col] = 0  # Backtrack if needed
                return False  # Trigger backtracking
    return True  # Solved

# Without Backtracking (Constraint Propagation)

def find_possibilities(board):
    # Create a 3D list to store possibilities for each cell
    # Each cell starts with all numbers 1-9 as potential candidates
    possibilities = [[[1, 2, 3, 4, 5, 6, 7, 8, 9] for _ in range(9)] for _ in range(9)]

    # Iterate through each cell in the board
    for row in range(9):
        for col in range(9):
            # If the cell is already filled (not 0), eliminate possibilities
            if board[row][col] != 0:
                num = board[row][col]  # The number already placed in the cell
                possibilities[row][col] = []  # No possibilities left for filled cells

                # Eliminate the number from possibilities in the same row and column
                for i in range(9):
                    if num in possibilities[row][i]:
                        possibilities[row][i].remove(num)  # Remove from the row
                    if num in possibilities[i][col]:
                        possibilities[i][col].remove(num)  # Remove from the column

                # Eliminate the number from possibilities in the 3x3 subgrid
                box_row, box_col = 3 * (row // 3), 3 * (col // 3)  # Top-left corner of the 3x3 grid
                for i in range(3):
                    for j in range(3):
                        if num in possibilities[box_row + i][box_col + j]:
                            possibilities[box_row + i][box_col + j].remove(num)

    # Return the updated possibilities for all cells
    return possibilities

# Solve the Sudoku board without using backtracking
def solve_sudoku_no_backtrack(board):
    while True:
        progress = False  # Track if any progress is made in this iteration

        # Calculate the possibilities for each cell
        possibilities = find_possibilities(board)

        # Iterate through each cell to find cells with only one possible number
        for row in range(9):
            for col in range(9):
                # If the cell is empty (0) and has only one possible value
                if board[row][col] == 0 and len(possibilities[row][col]) == 1:
                    board[row][col] = possibilities[row][col][0]  # Assign the only possible value
                    progress = True  # Mark that progress has been made

        # If no progress is made in this iteration, break the loop
        if not progress:
            break

    # Return the solved or partially solved board
    return board

# Sudoku Solver using Dynamic Programming

# Dynamic Programming Explanation:
# Use a DP table to keep track of possible numbers for each cell.
# As cells are filled, dynamically update the table by eliminating impossible numbers.

# Function to initialize the DP table
# Each cell in the DP table contains a set of possible numbers for that cell
def initialize_dp_table(board):
    dp_table = [[set(range(1, 10)) if board[row][col] == 0 else set() for col in range(9)] for row in range(9)]
    for row in range(9):
        for col in range(9):
            if board[row][col] != 0:
                update_dp_table(dp_table, row, col, board[row][col])
    return dp_table

# Function to update the DP table when a number is placed
# Removes the number from the sets of the corresponding row, column, and 3x3 subgrid
def update_dp_table(dp_table, row, col, num):
    for i in range(9):
        dp_table[row][i].discard(num)  # Remove from the row
        dp_table[i][col].discard(num)  # Remove from the column
    box_row, box_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            dp_table[box_row + i][box_col + j].discard(num)  # Remove from the 3x3 subgrid

# Function to solve Sudoku using DP

def solve_sudoku_dynamic(board):
    dp_table = initialize_dp_table(board)  # Initialize DP table
    while True:
        progress = False

        # Iterate through the board to find cells with only one possible value
        for row in range(9):
            for col in range(9):
                if board[row][col] == 0 and len(dp_table[row][col]) == 1:
                    num = dp_table[row][col].pop()  # Get the only possible number
                    board[row][col] = num  # Place the number on the board
                    update_dp_table(dp_table, row, col, num)  # Update the DP table
                    progress = True

        # If no progress is made, break the loop
        if not progress:
            break

    return board


# Example Sudoku Board (0 represents an empty cell)
example_board = [
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

# Solve using Backtracking
board_backtrack = [row[:] for row in example_board]  # Copy of the board
solve_sudoku_backtrack(board_backtrack)
print("Solved Sudoku (Backtracking):")
for row in board_backtrack:
    print(row)

# Solve using Constraint Propagation (No Backtracking)
board_no_backtrack = [row[:] for row in example_board]  # Copy of the board
solve_sudoku_no_backtrack(board_no_backtrack)
print("\nSolved Sudoku (Without Backtracking):")
for row in board_no_backtrack:
    print(row)
    
    
# Solve the Sudoku using Dynamic Programming
solved_board = solve_sudoku_dynamic(example_board)
print("\nSolved Sudoku (Dynamic Programming):")
for row in solved_board:
    print(row)    
    

# For backtracking approach, time complexity is O(9^n) - for a 9x9 grid & Space complexity is O(n) 

# For non-backtracking approach, constraint propagation, time complexity is O(n * 81 * 27) & Space complexity is O(729)

# For dynamic programming, time complexity is O(n * 81 + 2187) - where 81 is the number of cells and 2187 is for the initialization. 
# & Space complexity is Board = O(81) + DP Table = O(729) totaling to O(810)
