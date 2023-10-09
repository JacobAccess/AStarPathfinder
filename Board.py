BLANK = "█"

class Board:
    def __init__(self, basis, playertile="0"):
        self.tile = playertile
        
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
                col = self.state[i].index("P")
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
            if self.state[row-1][col] != BLANK:
                ov = self.state[row-1][col]
                a = Board(self, ov)
                a.change(col, row, self.tile)
                a.change(col, row-1, "P")
                moves.append(a)
                
        if row + 1 < len(self.state):
            if self.state[row+1][col] != BLANK:
                ov = self.state[row+1][col]
                b = Board(self, ov)
                b.change(col, row, self.tile)
                b.change(col, row+1, "P")
                moves.append(b)

        if col - 1 >= 0:
            if self.state[row][col-1] != BLANK:
                ov = self.state[row][col-1]
                c = Board(self, ov)
                c.change(col, row, self.tile)
                c.change(col-1, row, "P")
                moves.append(c)

        if col + 1 < len(self.state[row]):
            if self.state[row][col+1] != BLANK:
                ov = self.state[row][col+1]
                d = Board(self, ov)
                d.change(col, row, self.tile)
                d.change(col+1, row, "P")
                moves.append(d)
        
        return moves

    def __str__(self):
        o = ""
        for i in self.state:
            for j in i:
                o = o + j
            o = o + "\n"
        return o
        
        
if __name__ == "__main__":
    s = [["0","0","0"],
         [BLANK,BLANK,"0"],
         ["0","P","0"]]
    b = Board(s)
    c = b.calculate_moves()
    for i in c:
        print(i)
        
