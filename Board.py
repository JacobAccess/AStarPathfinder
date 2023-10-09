class Board:
    def __init__(self, basis):
        if type(basis) == list:
            self.state = basis[:]
        else:
            self.state = basis.state[:]

        for i in range(0,len(self.state)):
            self.state[i] = self.state[i][:]

    def find_player(self):
        row = -1
        col = -1
        for i in range(0, len(self.state)):
            try:
                col = self.state[i].index(2)
                row = i
            except:
                pass
        return [col, row]

    def change(self, column, row, value):
        self.state[row][column] = value

    def calculate_moves(self):
        moves = []
        
        col, row = self.find_player()
        #return [col, row]

        if row - 1 >= 0:
            if self.state[row-1][col] == 0:
                b = Board(self)
                b.change(col, row, 0)
                b.change(col, row-1, 2)
                moves.append(b)
                
        if row + 1 < len(self.state):
            if self.state[row+1][col] == 0:
                b = Board(self)
                b.change(col, row, 0)
                b.change(col, row+1, 2)
                moves.append(b)

        if col - 1 >= 0:
            if self.state[row][col-1] == 0:
                b = Board(self)
                b.change(col, row, 0)
                b.change(col-1, row, 2)
                moves.append(b)

        if col + 1 < len(self.state[row]):
            if self.state[row][col+1] == 0:
                b = Board(self)
                b.change(col, row, 0)
                b.change(col+1, row, 2)
                moves.append(b)
        
        return moves

    def __str__(self):
        o = ""
        for i in self.state:
            o = o + "\n" + str(i)
        return o
        
        
if __name__ == "__main__":
    s = [[0,0,0],
         [1,1,0],
         [0,2,0]]
    b = Board(s)
    c = b.calculate_moves()
    for i in c:
        print(i)
        
