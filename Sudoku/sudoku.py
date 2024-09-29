def find_next_empty(puzzle):
    # finds the next row,col on the puzzle that is not filled --> rep with -1
    # return row,col tuple (or (None, None) if there is none)
    # Keep in mind that we are using 0 to 8 as our indices
    for r in range(9):
        for c in range(9):
            if puzzle[r][c] == -1:
                return r,c
    return None, None


def is_valid(puzzle, guess, row, col):
    # checks whether the guess at that row, col is valid or not
    # returns true if valid and vice versa

    # Check the row
    row_vals = puzzle[row]
    if guess in row_vals:
        return False
    
    # Check the column
    col_vals = [puzzle[i][col] for i in range(9)]
    if guess in col_vals:
        return False
    
    # Check the 3x3 grid
    row_start = (row // 3) * 3
    col_start = (col // 3) * 3
    for r in range(row_start, row_start + 3):
        for c in range(col_start, col_start + 3):
            if puzzle[r][c] == guess:
                return False
                
    # If no conflicts, return True
    return True



def solve_sudoku(puzzle):
    # solve using backtracking
    # our puzzle is a list of lists where each inner list is a row in our sudoku solver
    # return whether a solution exists
    # mutates puzzle to the solution (if solution exists)

    # Choose somewhere on a puzzle to make a guess
    row, col = find_next_empty(puzzle)
    
# step 1: if there is no space left in the puzzle, then we are done because we only
#           allowed valid inputs
    if row is None:
        return True
# step 2: if there is a place to put a number, then make a guess between 1-9
    for guess in range(1,10):
        # step 3: check if this a valid guess or not
        if is_valid(puzzle, guess, row, col):
            # Now if the guess is valid we want to put that guess on the table
            puzzle[row][col] = guess
            # Now recurse using this puzzle
            # step 4: recursively calls our function
            if solve_sudoku(puzzle):
                return True
            
        # step 5: if not valid OR if our guesses does not solve the puzzle, then we need
        #         to backtrack and try a new number
        puzzle[row][col] = -1 # reset the guess


        # step 6: if none of the combination works than given puzzle is not solvable
    return False


if __name__ == '__main__':
    example_board = [
        [4, 9, 6,   -1, 7, -1,      -1, -1, -1],
        [-1, -1, 8,   9, -1, 3,     -1, -1, -1],
        [7, 5, -1,   8, -1, 2,      -1 , 1,  9],

        [-1, -1, -1,  -1, -1, -1,   -1 , 2 , 5],
        [-1, -1, 1,   7, 2, -1,      4 , 9 ,-1],
        [8, -1, 7,   -1, 9, -1,      3 , 6 ,-1],

        [-1, 8, -1,   -1, -1,  7,     9, -1, -1],
        [-1, 6, -1,   -1,  5,  4,     -1,  3, -1],
        [-1, -1, -1,   2,  8,  9,      1,  5,  6]
    ]
    print(solve_sudoku(example_board))
    print(example_board)


 