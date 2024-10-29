def solve_maze(maze, x, y, solution, n):
    
    #base case:is destination reached?
    if x == n - 1 and y == n - 1 and maze[x][y] == 0:
        solution[x][y] = 1
        return True

    #is current position safe?
    if isSafe(maze, x, y, n) and solution[x][y] == 0:
        
        #cell marking
        solution[x][y] = 1

        #moving
        if solve_maze(maze, x + 1, y, solution, n):  #move_down
            return True
        if solve_maze(maze, x, y + 1, solution, n):  #move_right
            return True
        if solve_maze(maze, x - 1, y, solution, n):  #move_up
            return True
        if solve_maze(maze, x, y - 1, solution, n):  #move_left
            return True

        #backtrack: unmark this cell in the solution path
        solution[x][y] = 0

    return False

def isSafe(maze, x, y, n):
    #a cell is safe if it is within bounds and not blocked (if it has value 0)
    return 0 <= x < n and 0 <= y < n and maze[x][y] == 0

#example maze
maze = [
    [0, 0, 0, 0, 0],
    [1, 1, 1, 1, 0],
    [0, 0, 0, 0, 0],
    [0, 1, 1, 1, 1],
    [0, 0, 0, 0, 0]
]

solution = [[0 for j in range(len(maze))] for i in range(len(maze))]
n = len(maze)

if solve_maze(maze, 0, 0, solution, n):
    for row in solution:
        print(row)
else:
    print("No solution")
