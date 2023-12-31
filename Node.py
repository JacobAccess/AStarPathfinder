class Node:
    def __init__(self, board, goal, parent=None, cost=0):
        self.board = board
        self.goal = goal
        self.parent = parent
        self.cost = cost
        self.hcost = self.heuristic()

    def name(self):
        return str(self.find_player())# + " ~ " + str(self.cost + self.hcost)

    def heuristic(self):
        ccol, crow = self.board.find_player()
        gcol, grow = self.goal.find_player()

        hrow = abs(grow - crow)
        hcol = abs(gcol - ccol)

        return hcol+hrow

    def find_player(self):
        return self.board.find_player()

    def cell_cost(self, x, y):
        return int(self.board.state[y][x])

    def find_moves(self):
        moves = []
        boards = self.board.calculate_moves()
        for i in boards:
            px, py = i.find_player()
            n = Node(i, self.goal, self, self.cost+1+self.cell_cost(px, py))
            moves.append(n)
        return moves

    def complete(self):
        if self.board.state == self.goal.state:
            return True
        return False

    def in_journey(self, node):
        p = self.parent
        while p is not None:
            if node.board.state == p.board.state:
                return True
            else:
                p = p.parent
        return False

    def __str__(self):
        c = self.cost
        h = self.heuristic()
        return f"Node with Cost {c} + Heuristic {h} = Total {c+h}"
