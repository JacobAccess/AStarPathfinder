from Board import *
import turtle

class TurtlePrinter:

    def __init__(self, board, start, goal, grid=16):
        self.board = Board(board)

        px, py = self.board.find_player()
        self.board.state[py][px] = 0

        self.grid = grid

        self.w = grid * len(self.board.state[0])
        self.h = grid * len(self.board.state)
        turtle.setup(self.w + grid, self.h + grid)
        turtle.colormode(255)
        self.turtle = turtle.Turtle()
        self.turtle.speed(1)
        self.turtle.shape("circle")
        self.turtle.hideturtle()

        self.tracer = turtle.tracer()
        turtle.tracer(0,0)

        self.start = start
        self.goal = goal
        
        self.DrawSquare(start[0], start[1], (255,0,0))
        self.DrawSquare(goal[0], goal[1], (0,255,0))


    def DrawBoard(self):
        for i in range(0, len(self.board.state)):
            for j in range(0, len(self.board.state[i])):
                if self.board.state[i][j] == BLANK:
                    self.DrawSquare(j, i)
        turtle.update()

    def DrawSquare(self, x, y, colour=(0,0,0)):
        t = self.turtle
        t.color(colour)
        t.up()
        t.goto((self.grid*x) - (self.w/2), (self.h/2) - (self.grid*y))
        t.begin_fill()
        for k in range(0, 4):
            t.forward(self.grid)
            t.right(90)
        t.end_fill()
        t.color((0,0,0))


    def Move(self, x, y):
        t = self.turtle
        t.goto((self.grid*x) - (self.w/2) + (self.grid/2), (self.h/2) - (self.grid*y) - (self.grid/2))

    def Solve(self, route):
        t = self.turtle
        turtle.tracer(self.tracer)
        t.color((0,0,255))
        route.pop(0)
        t.up()
        self.Move(self.start[0], self.start[1])
        t.down()
        turtle.update()
        for i in route:
            x, y = i.board.find_player()
            self.Move(x, y)
            turtle.update()

