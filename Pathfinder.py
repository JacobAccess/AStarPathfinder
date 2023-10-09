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

s, g = ReadMaze("mediummaze.png")

final = None

goal = Board(g)
start = Board(s)

begin = Node(start, goal, cost=0)
t = TurtlePrinter(begin.board, start.find_player(), goal.find_player(), 8)


expanded = []
unexpanded = [begin.find_player()]
nodes = [begin]
#h = begin.heuristic()

timer = time.time()

while len(nodes) > 0:
    nodes.sort(key=sorter)
    focus = nodes.pop(0)
    nname = focus.find_player()

    if focus.complete():
        final = focus
        break

    nm = focus.find_moves()
    for i in nm:
        iname = i.find_player()
        if (not iname in expanded) and (not iname in unexpanded):
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
#print(f"Took {totaltimer} seconds. Displaying path in 5 seconds.")
#time.sleep(5)

#for i in route:
    #print(i)
    #print(i.board)
print(f"Took {totaltimer} seconds, and {len(route)} moves.")

t.DrawBoard()
t.Solve(route)
