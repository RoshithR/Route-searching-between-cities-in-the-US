import sys
import heapq
import copy

#designing a goal board
def goal_board():
    board = (range (1,16))
    board.append(0)
    goal_board = []
    for i in range(0, len(board), 4):
        goal_board.append(board[i:i+4])
    return goal_board

# to get the row and column of 0 in a board
def get_rowandcol(element,current_board):
    col = 0
    row = 0
    for i in current_board:
        if (element in i):
            col = i.index(element)
            return row,col
        row += 1

# Checking if the board is solvable
def is_board_solvable(current_board):
    row,col = get_rowandcol(0,current_board)
    new_list = []
    inv_count = 0
    parity = 0
    for i in current_board:
        for j in i:
            new_list.append(j)
    for i in range(len(new_list)):
        #print "i = %s " % i
        for j in range(i+1,len(new_list)):
            #print "j = %s " % j
            if (new_list[j] < new_list[i] and new_list[j] != 0):
                #print "val at j = %s " % new_list[j]
                #print "val at i = %s " % new_list[i]
                inv_count += 1
    #print inv_count
    #print row
    if (inv_count % 2 == 0):
        parity = 1
    else:
        parity = 2
    if ((row == 0 or row == 2) and parity == 2):
        return True
        #print "solvable"
    elif ((row == 1 or row == 3) and parity == 1):
        return True
    else:
        return False
        #print "Not solvable"

# calculating the heuristic_evaluation
def heuristic_evaluation(current_board):
    goalboard = goal_board()
    new_list = []
    for i in goalboard:
        for j in i:
            new_list.append(j)
    heuristic_value = 0
    for i in current_board:
        for j in i:
            if j != 0:
                #print "row and col for %s:" % j
                row_current,col_current = get_rowandcol(j, current_board)
                #print "r1: %s" % row_current
                #print "c1: %s" % col_current
                for x in range(16):
                    if (j == new_list[x]):
                        row_goal,col_goal = get_rowandcol(j, goalboard)
                        #print "r2: %s" % row_goal
                        #print "c2: %s" % col_goal
                        man_distance = abs(row_goal - row_current) + abs(col_goal - col_current)
                        #print "man: %s" % man_distance
                heuristic_value += man_distance
                #print "heuristic value of %s is:" % current_board
                #print heuristic_value/3
    return float(heuristic_value)/3

# to get all the left successors of current state
def left_successors(row,col,current_board):
    succ_fringe = []
    successor = copy.deepcopy(current_board)
    for i in range (col,0,-1):
        #print zerorow
        successor[row][i],successor[row][i-1] = successor[row][i-1],successor[row][i]
        print "left : ", successor
        left_successor = copy.deepcopy(successor)
        if left_successor not in visited_states:
            succ_fringe.append(left_successor)
    return succ_fringe

# to get all the right successors of current state
def right_successors(row,col,current_board):
    succ_fringe = []
    successor = copy.deepcopy(current_board)
    for i in range (col,3):
        #print zerorow
        successor[row][i],successor[row][i+1] = successor[row][i+1],successor[row][i]
        print "right : ",successor
        right_successor = copy.deepcopy(successor)
        if right_successor not in visited_states:
            succ_fringe.append(right_successor)
    return succ_fringe

# to get all the up successors of current state
def up_successors(row,col,current_board):
    succ_fringe = []
    successor = copy.deepcopy(current_board)
    for i in range (row,0,-1):
        #print zerorow
        successor[i][col],successor[i-1][col] = successor[i-1][col],successor[i][col]
        print "up : ",successor
        up_successor = copy.deepcopy(successor)
        if up_successor not in visited_states:
            succ_fringe.append(up_successor)
    return succ_fringe

# to get all the down successors of current state
def down_successors(row,col,current_board):
    succ_fringe = []
    successor = copy.deepcopy(current_board)
    for i in range (row,3):
        #print zerorow
        successor[i][col],successor[i+1][col] = successor[i+1][col],successor[i][col]
        print "down : ",successor
        down_successor = copy.deepcopy(successor)
        if down_successor not in visited_states:
            succ_fringe.append(down_successor)
    return succ_fringe

#succesor function
def successor(row,col,current_board):
    succ_fringe = []
    # successors from left fringe
    left_fringe = left_successors(row,col,current_board)
    for element in left_fringe:
        heapq.heappush(succ_fringe,(heuristic_evaluation(element),element))

    # successors from right fringe
    right_fringe = right_successors(row,col,current_board)
    for element in right_fringe:
        heapq.heappush(succ_fringe,(heuristic_evaluation(element),element))

    # successors from up fringe
    up_fringe = up_successors(row,col,current_board)
    for element in up_fringe:
        heapq.heappush(succ_fringe,(heuristic_evaluation(element),element))

    # successors from down fringe
    down_fringe = down_successors(row,col,current_board)
    for element in down_fringe:
        heapq.heappush(succ_fringe,(heuristic_evaluation(element),element))
    return succ_fringe

# checking if goal is reached
def is_goal(current_board):
    current_list = []
    goal_list = (range (1,16))
    goal_list.append(0)
    count = 0
    for i in current_board:
        for j in i:
            current_list.append(j)
    for i in range(len(goal_list)):
        if (goal_list[i] != current_list[i]):
            #print "not goal"
            return False
            #print "val at j = %s " % new_list[j]
            #print "val at i = %s " % new_list[i]
    return True


def solve(initial_board):
    row,col =  get_rowandcol(0, initial_board)
    #cost = 0
    fringe = []
    heapq.heappush(fringe,(heuristic_evaluation(initial_board),initial_board,0))
    while len(fringe) > 0:
        #print "fringe before pop: %s" % fringe
        popping_s = heapq.heappop(fringe)
        s = popping_s[1]
        visited_states.append(s)
        print "Current state:"
        print s
        #print "fringe after pop: %s" % fringe
        if is_goal(s):
            return True
        row_s,col_s = get_rowandcol(0, s)
        returned_heap = successor(row_s,col_s,s)
        for i in range(len(returned_heap)):
            successors = heapq.heappop(returned_heap)
            heapq.heappush(fringe,(successors))
    return False


# accepting the input file from the user and getting our initial_board.
def get_initial(input_filename):
    b = open(input_filename, 'r')
    input_board = b.readlines()
    temp_board = []
    for i in input_board:
        for j in i.split():
            temp_board.append(int(j))
            intial_board = [temp_board[i:i+4] for i in range(0, len(temp_board), 4)]
    return intial_board


input_filename = sys.argv[1]
visited_states = []
current_board = get_initial(input_filename)
print "initial Board:",current_board
if (is_board_solvable(current_board)):
    if(solve(current_board)):
        print "reached"
else:
    print "Input board is not solvable"
