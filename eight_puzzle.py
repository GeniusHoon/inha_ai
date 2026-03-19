import queue
import copy

class Puzzle :
    # up down left right
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    def __init__(self, board, goal, depth) :
        self.board = board
        self.goal = goal
        self.depth = depth

    def get_dist_to_goal(self) :
        dist = 0
        for i in range(3) :
            for j in range(3) :
                if self.board[i][j] != self.goal[i][j] :
                    dist += 1
        return dist

    def get_total_dist_to_goal(self) :
        return self.depth + self.get_dist_to_goal()
    
    def get_next_puzzles(self) :
        next_puzzles = []
        # find 0 index first.
        for i in range(3) :
            for j in range(3) :
                if self.board[i][j] == 0 :
                    zero_y = i
                    zero_x = j
                    break

        # directions to go
        for i in range(4) :
            next_x = zero_x + self.dx[i]
            next_y = zero_y + self.dy[i]

            if 0 <= next_x < 3 and 0 <= next_y < 3 :
                # swap
                new_puzzle = Puzzle(copy.deepcopy(self.board), self.goal, self.depth + 1)
                new_puzzle.board[zero_y][zero_x] = new_puzzle.board[next_y][next_x]
                new_puzzle.board[next_y][next_x] = 0
                next_puzzles.append(new_puzzle)

        return next_puzzles
    
    def __lt__(self, other) :
        return self.get_total_dist_to_goal() < other.get_total_dist_to_goal()
    
    def __gt__(self, other) :
        return self.get_total_dist_to_goal() > other.get_total_dist_to_goal()
    
    def __eq__(self, other) :
        return self.board == other.board

    def __ne__(self, other) :
        return self.board != other.board
        
    def __str__(self) :
        res = "-------------------\n"
        for i in range(3) :
            for j in range(3) :
                res += str(self.board[i][j]) + " "
            res += "\n"
        res += "Depth: " + str(self.depth) + " Dist : " + str(self.get_total_dist_to_goal()) + "\n"
        res += "-------------------"
        return res

open = queue.PriorityQueue()
closed = []

initial_board = [[1, 2, 3], 
                 [8, 0, 5],
                 [7, 4, 6]]

goal_board = [[1, 2, 3],
              [8, 0, 4],
              [7, 6, 5]]

open.put(Puzzle(initial_board,
                goal_board, 0))

count = 0
while not open.empty() :
    count += 1
    current = open.get()
    print(count, "**********************")
    print(current)
    print("**********************")
    closed.append(current)

    if current.board == current.goal :
        print("Goal reached!")
        break
    
    # make child node.
    next_puzzles = current.get_next_puzzles()

    # condition check. shoudn't be in closed list.
    for next_puzzle in next_puzzles :
        if next_puzzle not in closed :
            print("Put in open list")
            print(next_puzzle)
            open.put(next_puzzle)