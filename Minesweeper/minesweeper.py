import random
import re


class Board:
    def __init__(self, dim_size, num_bombs):
        self.dim_size = dim_size
        self.num_bombs = num_bombs

        # lets create a board
        self.board = self.make_new_board()
        self.assign_values_to_board()
          
        # initialize a set to keep track of which locations we have uncovered
        # we'll have (row,col) tuples into this set 
        self.dug = set()

    def make_new_board(self):
        
        board = [[None for _ in range(self.dim_size)] for _ in range(self.dim_size)] #it makes a new board depending on the size of board 

        # plant the bombs
        bombs_planted = 0
        while bombs_planted < self.num_bombs:
            loc = random.randint(0, self.dim_size**2 - 1)
            row = loc // self.dim_size # we want the number of times dim_size goes into loc to tell us what row to look at
            col = loc % self.dim_size # we want the remainder to tell us what index in that row to look at

            if board[row][col] == "*":
                # This we have actually planted the bomb there
                continue

            board[row][col] = "*"
            bombs_planted += 1
        return board
    
    def assign_values_to_board(self):
        # now that we have the bombs planted, let's assign a number 0-8 for all the empty spaces, which
        # represents how many neighboring bombs there are. we can precompute these and it'll save us some
        # effort checking what's around the board later on :)
        for r in range(self.dim_size):
            for c in range(self.dim_size):
                if self.board[r][c]:
                    continue
                self.board[r][c] = self.get_num_neighbouring_bombs(r,c)


    def get_num_neighbouring_bombs(self,row,col):
        # let's iterate through each of the neighboring positions and sum number of bombs
        # top left: (row-1, col-1)
        # top middle: (row-1, col)
        # top right: (row-1, col+1)
        # left: (row, col-1)
        # right: (row, col+1)
        # bottom left: (row+1, col-1)
        # bottom middle: (row+1, col)
        # bottom right: (row+1, col+1)

        # make sure to not go out of bounds!  

        num_neighbouring_bombs = 0 
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if r == row and c == col:
                    # our original location
                    continue
                if self.board[r][c] == "*":
                    num_neighbouring_bombs += 1

        return num_neighbouring_bombs

    def dig(self,row, col):
        # dig at that location
        # return true if successful and if bomb is there return false


        # a few scenarios 
        # hit a bomb --> game over
        # dig at location with neighboring bombs --> finish dig
        # dig at location with no neighbouring bombs --> recursively dig neighbours
        
        self.dug.add((row, col)) # Keep track of where we dug
        if self.board[row][col] == "*":
            return False
        elif self.board[row][col] > 0:
            return True

        # self.board[row][col] == 0
        for r in range(max(0, row-1), min(self.dim_size-1, row+1)+1):
            for c in range(max(0, col-1), min(self.dim_size-1, col+1)+1):
                if (r,c) in self.dug:
                    continue # don't dig where you've already dug
                self.dig(r,c)
        return True
    def __str__(self):
        # this is a magic function where if you call print on this object, 
        # it will print out what this function returns
        # return a string that shows the board to the player

        # lets create a new array that represents what the user should see
        visible_board = [[None for i in range(self.dim_size)] for i in range(self.dim_size)]
        for row in range(self.dim_size):
            for col in range(self.dim_size):
                if (row,col) in self.dug:
                    visible_board[row][col] = str(self.board[row][col])
                else:
                    visible_board[row][col] = " "
        
        # put this together in a string
        string_rep = ''
        # get max column widths for printing
        widths = []
        for idx in range(self.dim_size):
            columns = map(lambda x: x[idx], visible_board)
            widths.append(
                len(
                    max(columns, key = len)
                )
            )

        # print the csv strings
        indices = [i for i in range(self.dim_size)]
        indices_row = '   '
        cells = []
        for idx, col in enumerate(indices):
            format = '%-' + str(widths[idx]) + "s"
            cells.append(format % (col))
        indices_row += '  '.join(cells)
        indices_row += '  \n'
        
        for i in range(len(visible_board)):
            row = visible_board[i]
            string_rep += f'{i} |'
            cells = []
            for idx, col in enumerate(row):
                format = '%-' + str(widths[idx]) + "s"
                cells.append(format % (col))
            string_rep += ' |'.join(cells)
            string_rep += ' |\n'

        str_len = int(len(string_rep) / self.dim_size)
        string_rep = indices_row + '-'*str_len + '\n' + string_rep + '-'*str_len

        return string_rep
         

        
                


#play the game
def play(dim_size = 10, num_bombs = 10):
    # Step1: Create the boards and plant the bombs
    board = Board(dim_size, num_bombs)
    # Step2: Show the user the board and ask for where they want to dig

    # Step3a : If location is a bomb, show game over message
    # Step3b : If location is a not a bomb, then dig recursively until each square is a
    #           next to a bomb
    # Step4: Repeat step 2 and 3a/b until there are no more places to dig
    safe = True
    while len(board.dug) < board.dim_size ** 2 - num_bombs:
        print(board)
        user_input = re.split(',(\\s)*',input("Where would you like to dig? Input as row,col: "))
        row, col = int(user_input[0]), int(user_input[-1])
        if row < 0 or row >= board.dim_size or col < 0 or col >= board.dim_size:
            print("Invalid location. Try Again")
            continue

        # if it is valid
        safe = board.dig(row,col)
        if not safe: #means we have dug the bomb. Game Over
             break
        
    # There are two ways to end this loop
    if safe:
        print("Congratulation You Won!!!!!! Hurrah! You are Victorious")
    else:
        print("Sorry Game Over. You lost. You are loser!!!!!")

    # Now we can reveal the whole board
    board.dug = [(r,c) for r in range(board.dim_size) for c in range(board.dim_size)]
    print(board)



if __name__ == "__main__":
    play()