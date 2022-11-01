import time
"""
references:
    - https://github.com/aimacode/aima-python

"""
start_time = time.process_time()

def check_board(number): # check valid board size
    if number == 9:
        return 3
    else:
        return

def printboard(board): # print sudoku board
    for i in range(len(board)):
        for j in range(len(board)):
            print(board[i][j], end = " ")
        print("")
        
# find the empty positions in board(the positions that are 0),and return an arry of positions
def find_empty(board): 
    empty_pos = []
    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == 0:
                empty_pos.append((i,j)) # (row,col)
    return empty_pos

 # checks if a number is valid in position
def check_validation(board, pos, val):          
    #checking rows
    for i in range(len(board)):
        if board[pos[0]][i] == val:
            return False

    #checking col
    for i in range(len(board)):
        if board[i][pos[1]] == val:
            return False
    
    #checking Squers
    starting_row = (pos[0] // squares) * squares
    starting_col = (pos[1] // squares) * squares

    for i in range(starting_row,starting_row + squares):
        for j in range(starting_col,starting_col + squares): 
            if board[i][j] == val:
                return False
    return True

def forward_checking(board):                    # find the domins of a position
    empty_valus = find_empty(board) ##
    domins = {}  ##
    for pos in empty_valus:
        domins[pos] = []
        # empty_valus.remove(pos)
        for i in range(1, len(board) + 1):
            if check_validation(board, pos, i):
                domins[pos].append(i)

        if domins[pos] == []:
            domins[pos].pop
    return domins

def degree(poses,board):  # [(2,1),(3,0)]           # gets an array of positions and return the position that has most relation
    sum = {}
    count = 0
    #checking row
    for pos in poses:
        for a in range(len(board)):
            if board[pos[0]][a] == 0:
                count += 1
        sum[pos] = count
        count = 0

    #checking col
    for pos in poses:
        for j in range(len(board)):
            if board[j][pos[1]] == 0:
                sum[pos] += 1
    
    #checking Squers
    for pos in poses:
        starting_row = (pos[0] // squares) * squares
        starting_col = (pos[1] // squares) * squares

        for i in range(starting_row,starting_row + squares):
            for j in range(starting_col,starting_col + squares): 
                if board[i][j] == 0:
                    sum[pos] += 1

    result = ()
    for pos in sum:             # sum = {(0,0) : 5, (1,2) : 8}
        if sum[pos] > count:
            count = sum[pos]
            result = pos
    
    return result


def mrv_domains(domains,board): # finds the position that has less domin
    poses = []
    temp = sizeof_board + 1 # for a 9x9 board, temp = 9, so everything is < temp in this case
    for domain in domains:
        if len(domains[domain]) == temp:
            poses.append(domain)
        elif len(domains[domain]) < temp:
            poses.clear()
            poses.append(domain)
            temp = len(domains[domain])
    
    if len(poses) > 1 :
        return degree(poses,board)
    
    return poses.pop()


def backtrack(board):               # solve the problem by backtracking

    domins = forward_checking(board)
    if not domins:
        return True
    start = mrv_domains(domins,board)
    for i in domins[start]:
            board[start[0]][start[1]] = i
            if backtrack(board):
                return True
            board[start[0]][start[1]] = 0
         

    return False  # this sudoku cant be solved



print("----- Test Board A -----")
test_board_a = [
               [0, 0, 1,   0, 0, 2,   0, 0, 0],
               [0, 0, 5,   0, 0, 6,   0, 3, 0],
               [4, 6, 0,   0, 0, 5,   0, 0, 0],

               [0, 0, 0,   1, 0, 4,   0, 0, 0],
               [6, 0, 0,   8, 0, 0,   1, 4, 3],
               [0, 0, 0,   0, 9, 0,   5, 0, 8],

               [8, 0, 0,   0, 4, 9,   0, 5, 0],
               [1, 0, 0,   3, 2, 0,   0, 0, 0],
               [0, 0, 9,   0, 0, 0,   3, 0, 0]
]

print("----- Test Board B -----")
test_board_b = [
               [0, 0, 1,   0, 0, 2,   0, 0, 0],
               [0, 0, 5,   0, 0, 6,   0, 3, 0],
               [4, 6, 0,   0, 0, 5,   0, 0, 0],

               [0, 0, 0,   1, 0, 4,   0, 0, 0],
               [6, 0, 0,   8, 0, 0,   1, 4, 3],
               [0, 0, 0,   0, 9, 0,   5, 0, 8],

               [8, 0, 0,   0, 4, 9,   0, 5, 0],
               [1, 0, 0,   3, 2, 0,   0, 0, 0],
               [0, 0, 9,   0, 0, 0,   3, 0, 0]
]

print("----- Test Board C -----")
test_board_c = [
               [0, 0, 1,   0, 0, 2,   0, 0, 0],
               [0, 0, 5,   0, 0, 6,   0, 3, 0],
               [4, 6, 0,   0, 0, 5,   0, 0, 0],

               [0, 0, 0,   1, 0, 4,   0, 0, 0],
               [6, 0, 0,   8, 0, 0,   1, 4, 3],
               [0, 0, 0,   0, 9, 0,   5, 0, 8],

               [8, 0, 0,   0, 4, 9,   0, 5, 0],
               [1, 0, 0,   3, 2, 0,   0, 0, 0],
               [0, 0, 9,   0, 0, 0,   3, 0, 0]
]

solve_board_a = test_board_a
sizeof_board =  len(solve_board_a)
printboard(solve_board_a)

solve_board_b = test_board_b
sizeof_board =  len(solve_board_b)
printboard(solve_board_b)

solve_board_c = test_board_c
sizeof_board =  len(solve_board_c)
printboard(solve_board_c)

squares = check_board(sizeof_board)


if backtrack(solve_board_a) and backtrack(solve_board_b) and backtrack(solve_board_c):
    print("----- Solved Test Board A -----")
    printboard(solve_board_a)
    end_time = time.process_time()
    print("(A) CPU time:  ", end_time - start_time)
    
    print("----- Solved Test Board B -----")
    printboard(solve_board_b)
    end_time = time.process_time()
    print("(A) CPU time:  ", end_time - start_time)
    
    print("----- Solved Test Board C -----")
    printboard(solve_board_c)
    end_time = time.process_time()
    print("(A) CPU time:  ", end_time - start_time)
else:
    print("ERROR: invalid board - cannot be solved")
