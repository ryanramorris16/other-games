# Generate a sudoku board

import copy
import random
import numpy as np

def is_valid(row, col, num):
    global grid
    # Check if row has this number in it already
    for i in range(9):
        if grid[row][i] == num:
            return False

    # Check if col has this number in it already
    for i in range(9):
        if grid[i][col] == num:
            return False

    # Check if 3x3 square has this number in it already
    square_row = (row // 3) * 3
    square_col = (col // 3) * 3
    for i in range(square_row, square_row + 3):
        for j in range(square_col, square_col + 3):
            if grid[i][j] == num:
                return False

    return True     # If row, col, square are all valid, returns True

def solve_sudoku():
    count = 0
    global grid
    for row in range(9):
        for col in range(9):
            if grid[row][col] == 0:
                for num in random.sample(range(1, 10), 9):  # Shuffle numbers
                    if is_valid(row, col, num):   # If the number CAN go there, PUT it there
                        grid[row][col] = num
                        if solve_sudoku()[0]:  # Recursion to fill in grid
                            return True, count
                        else:   # Else grid can't be filled in, i.e. not valid solution
                            grid[row][col] = 0  # Backtrack
                return False, count
    count += 1
    return True, count

def generate_sudoku():
    global grid
    grid = [[0 for _ in range(9)] for _ in range(9)]    # Start with 9 x 9 grid of 0s
    solve_sudoku()  # "Solve" empty grid by populating with valid full grid
    return grid

grid = generate_sudoku()
solution = grid
#print(np.matrix(new_sudoku))

# Hiding numbers to create actual puzzle
def generate_index_list():
    rows = [x for x in range(9)]
    cols = [x for x in range(9)]
    indices = [(row, col) for row in rows for col in cols]
    random.shuffle(indices)
    return indices

idx_list = generate_index_list()
difficulty = {"Easy": 20, "Medium": 40, "Hard": 60}

def remove_num(index):
    global grid
    row, col = index
    temp = grid[row][col]   # Store solution value as temp variable in case clue cannot be removed for unique solution
    grid[row][col] = 0
    new_grid = copy.deepcopy(grid)

    if solve_sudoku()[1] > 1:
        print("replacing")
        new_grid[row][col] = temp
    else:
        #print("not replacing")
        new_grid[row][col] = 0

    grid = new_grid

    return grid

print("Solution: \n",np.matrix(grid))

i = 0
while i < 5:#difficulty['Easy']:
    new_sudoku = remove_num(idx_list[i])
    #print(i, idx_list[i], "\n", np.matrix(new_sudoku))
    i += 1

print(np.matrix(new_sudoku))

#print("Removed index {}: \n".format(idx_list[0]), np.matrix(remove_num(new_sudoku, idx_list[0])))

#sudoku_test = [[0,0,0,2,6,0,7,0,1],[6,8,0,0,7,0,0,9,0],[1,9,0,0,0,4,5,0,0,],[8,2,0,1,0,0,0,4,0],[0,0,4,6,0,2,9,0,0],[0,5,0,0,0,3,0,2,8],[0,0,9,3,0,0,0,7,4],[0,4,0,0,5,0,0,3,6],[7,0,3,0,1,8,0,0,0]]
#print(np.matrix(sudoku_test))
#print(np.matrix(solve_sudoku(sudoku_test)[1]))
