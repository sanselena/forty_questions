# Pseudo code for N-Queens Problem
#
# 1. Initialize Function:
#    - Define a function 'solveNQueens(n)' which will call a helper function to place queens.
#
# 2. Backtracking:
#    - Define a recursive function 'placeQueens(row, queens)' where:
#      - 'row' is the current row we are trying to place a queen in.
#      - 'queens' is a list that keeps track of the column index of the queens placed in previous rows.
#
# 3. Base Case:
#    - If 'row == n', this means all queens are successfully placed. Store the solution and return.
#
# 4. Recursive Case:
#    - For each column 'col' in range '0' to 'n-1':
#      - Check if placing a queen at '(row, col)' is safe by verifying:
#        - No other queen is in the same column.
#        - No other queen is on the same diagonal.
#      - If it is safe, place the queen by adding 'col' to 'queens' and recursively call 'placeQueens(row + 1, queens)'.
#
# 5. Remove Queen (Backtrack):
#    - After returning from the recursive call, remove the last queen placed to try other configurations.
#
# 6. Return All Solutions:
#    - Return the stored solutions.

def solveNQueens(n):
    def placeQueens(row, queens):
        if row == n:
            #all queens are placed, convert queens' positions to board format and add to solutions
            solution = []
            for queen_column in queens:
                row_representation = ' .' * queen_column + ' Q' + ' .' * (n - queen_column - 1)
                solution.append(row_representation)
            solutions.append(solution)
            return

        for col in range(n):
            #check if placing queen at (row, col) is safe
            if col not in queens and all(
                abs(col - queens[r]) != row - r for r in range(row)
            ):
                #place the queen and recurse for the next row
                placeQueens(row + 1, queens + [col])

    solutions = []
    placeQueens(0, [])
    return solutions

#example usage
n = 5
solutions = solveNQueens(n)
for i, solution in enumerate(solutions, 1):
    print(f"Solution {i}:")
    for row in solution:
        print(row)
    print()
