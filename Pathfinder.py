from Board import *
from Node import *
from Mazereader import *
from Turtleprinter import *
import time



def sorter(e):
    return e.cost + e.hcost

def printer():
    for i in nodes:
        print(i)

s, g = ReadMaze("maze.png")

final = None

goal = Board(g)
start = Board(s)

begin = Node(start, goal, cost=0)
t = TurtlePrinter(begin.board, start.find_player(), goal.find_player(), 32)


expanded = []
unexpanded = [begin.name()]

nodes = [begin]
#h = begin.heuristic()

timer = time.time()

while len(nodes) > 0:
    nodes.sort(key=sorter)
    focus = nodes.pop(0)
    nname = focus.name()
    if focus.complete():
        final = focus
        break

    nm = focus.find_moves()
    for i in nm:
        iname = i.name()
        if i.find_player() == [14, 2]:
                print("Junction")
                print(i.parent.board)
                print(i.cost + i.hcost)
        if (not iname in expanded):# and (not iname in unexpanded):

            if not focus.in_journey(i): 
                nodes.append(i)
                unexpanded.append(iname)

    expanded.append(nname)
    unexpanded.remove(nname)


route = []
child = final
while child is not None:
    route.append(child)
    child = child.parent
route.reverse()

totaltimer = time.time() - timer

verbose = False
if verbose:
    for i in route:
        print(i)
        print(i.board)
print(f"Took {totaltimer} seconds, and {len(route)} moves.")

t.DrawBoard()
t.Solve(route)
