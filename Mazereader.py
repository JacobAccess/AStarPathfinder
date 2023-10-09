from PIL import Image

RED = (237, 28, 36)

def Approximate(colour, comparison, margin=55):
    r = abs(comparison[0] - colour[0])
    g = abs(comparison[1] - colour[1])
    b = abs(comparison[2] - colour[2])

    return r < margin and g < margin and b < margin

def CloneList(l):
    o = l[:]
    for i in range(0, len(o)):
        o[i] = o[i][:]
    return o

def ReadMaze(image):
    im = Image.open(image, "r")
    pixels = im.getdata()

    data = []

    for i in range(0, im.height):
        row = []
        for j in range(0, im.width):
            p = j + (i*im.width)

            x = pixels[p]
            y = 0
            if x == (0,0,0) or x == (0,0,0,255):
                y = 1
            elif x == (255,255,255) or x == (255,255,255,255):
                y = 0
            elif Approximate(x, RED):
                y = 2
            else:
                y = 3
                
            row.append(y)
        data.append(row)
        
    start = CloneList(data)
    end = CloneList(data)
           
    for i in range(0, len(end)):
        for j in range(0, len(end[i])):
            if end[i][j] == 2:
                end[i][j] = 0
                break
        else:
            continue

        break
                

    for i in range(0, len(start)):
        for j in range(0, len(start[i])):
            if start[i][j] == 3:
                start[i][j] = 0
                end[i][j] = 2
                break
        else:
            continue
        
        break
            

    return [start, end]

if __name__ == "__main__":
    start, finish = ReadMaze("maze.png")
    #print(start)
    #print(finish)
    print(Approximate((0,255,0), RED))
