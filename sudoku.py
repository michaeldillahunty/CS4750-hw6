import time

start_time = time.process_time()

def number_of_squares(number): # function to check correct dimensions of board 
    if number == 9: # 3x3 squares in board
        return 3
    elif number == 4: # 2x2 squares in board
        return 2

def printboard(board):  # helper function to format solved boards for printing
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end=" ")
        print("")

def find_empty(board):  # find the empty positions in the board and return an array of these found positions
    empty_values = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty_values.append((i,j)) # (row,col)
    return empty_values


def check_validation(board, pos, value):  # checks if a value is in a valid position
    for i in range(len(board)): # check rows
        if board[pos[0]][i] == value:
            return False

    for i in range(len(board)): # check columns 
        if board[i][pos[1]] == value:
            return False
    
    starting_row = (pos[0] // squares) * squares
    starting_col = (pos[1] // squares) * squares

    for i in range(starting_row, starting_row + squares):
        for j in range(starting_col, starting_col + squares): 
            if board[i][j] == value:
                return False
    return True

def forward_checking(board):                    # find the domins of a position
    empty_values = find_empty(board) ##
    domains = {}  
    for pos in empty_values:
        domains[pos] = []
        for i in range(1, len(board) + 1):
            if check_validation(board, pos, i):
                domains[pos].append(i)

        if domains[pos] == []:
            domains[pos].pop
    return domains

# function gets an array of positions, returns position with the most relevant relation
def degree(posns, board): # i.e. [(x1,y1), (x2,y2)]           
    sum = {}
    count = 0
    for pos in posns: # check rows
        for a in range(len(board)):
            if board[pos[0]][a] == 0:
                count += 1
        sum[pos] = count
        count = 0

    for pos in posns: # check columns
        for j in range(len(board)):
            if board[j][pos[1]] == 0:
                sum[pos] += 1
    
    for pos in posns: # check squares
        starting_row = (pos[0] // squares) * squares
        starting_col = (pos[1] // squares) * squares

        for i in range(starting_row,starting_row + squares):
            for j in range(starting_col,starting_col + squares): 
                if board[i][j] == 0:
                    sum[pos] += 1

    result = ()
    for pos in sum:          
        if sum[pos] > count:
            count = sum[pos]
            result = pos
    return result

def mrv(domains, board):  # find position that has the smallest domain value
    positions = []
    temp = size_Of_board + 1  # in the given board size cases, temp = 9x9 == 9
    for d in domains:
        if len(domains[d]) == temp:
            positions.append(d)
        elif len(domains[d]) < temp:
            positions.clear()
            positions.append(d)
            temp = len(domains[d])
    
    if len(positions) > 1 :
        return degree(positions,board)
    return positions.pop()

algo_start = time.process_time()
print("Algorithm Start: ", algo_start)
def solve(board): # solve with mrv degree backtracking
    domains = forward_checking(board)
    if not domains:
        return True
    start = mrv(domains, board)
    for i in domains[start]:
            board[start[0]][start[1]] = i
            if solve(board):
                return True
            board[start[0]][start[1]] = 0    
    return False  # this board cannot be solved
algo_finish = time.process_time()
print("Algorithm Finish: ", algo_finish)    

test_board_a = [
    [0, 0, 1, 0, 0, 2, 0, 0, 0],
    [0, 0, 5, 0, 0, 6, 0, 3, 0],
    [4, 6, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 1, 0, 4, 0, 0, 0],
    [6, 0, 0, 8, 0, 0, 1, 4, 3],
    [0, 0, 0, 0, 9, 0, 5, 0, 8],
    [8, 0, 0, 0, 4, 9, 0, 5, 0],
    [1, 0, 0, 3, 2, 0, 0, 0, 0],
    [0, 0, 9, 0, 0, 0, 3, 0, 0]
]

test_board_b = [
   [0, 0, 5, 0, 1, 0, 0, 0, 0],
   [0, 0, 2, 0, 0, 4, 0, 3, 0],
   [1, 0, 9, 0, 0, 0, 2, 0, 6],
   [2, 0, 0, 0, 3, 0, 0, 0, 0],
   [0, 4, 0, 0, 0, 0, 7, 0, 0],
   [5, 0, 0, 0, 0, 7, 0, 0, 1],
   [0, 0, 0, 6, 0, 3, 0, 0, 0],
   [0, 6, 0, 1, 0, 0, 0, 0, 0],
   [0, 0, 0, 0, 7, 0, 0, 5, 0]
]

test_board_c = [
   [6, 7, 0, 0, 0, 0, 0, 0, 0],
   [0, 2, 5, 0, 0, 0, 0, 0, 0],
   [0, 9, 0, 5, 6, 0, 2, 0, 0],
   [3, 0, 0, 0, 8, 0, 9, 0, 0],
   [0, 0, 0, 0, 0, 0, 8, 0, 1],
   [0, 0, 0, 4, 7, 0, 0, 0, 0],
   [0, 0, 8, 6, 0, 0, 0, 9, 0],
   [0, 0, 0, 0, 0, 0, 0, 1, 0],
   [1, 0, 6, 0, 5, 0, 3, 7, 0]
]


solve_board_a = test_board_a
size_Of_board =  len(solve_board_a)
squers = number_of_squares(size_Of_board)

solve_board_b = test_board_b
board_size = len(solve_board_b)
squares = number_of_squares(board_size)

solve_board_c = test_board_c
board_size = len(solve_board_c)
squares = number_of_squares(board_size)

print("----- Original Board A -----")
printboard(solve_board_a)
print("----- Original Board B -----")
printboard(solve_board_b)
print("----- Original Board C -----")
printboard(solve_board_c)
print("----------------------------")
print("----- Solved Board A -----")
solve(solve_board_a)
printboard(solve_board_a)
print("----- Solved Board B -----")
solve(solve_board_b)
printboard(solve_board_b)
print("----- Solved Board C -----")
solve(solve_board_c)
printboard(solve_board_c)

end_time = time.process_time()
print("Start Time: ", start_time)
print("End Time: ", end_time)
print("Time Elapsed: ", end_time-start_time)