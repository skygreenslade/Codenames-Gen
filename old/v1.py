
import random



def generateGrid(redFirst):
    grid = [[]]

    squares = squaresList(redFirst)

    pos = 00 #left digit = row, right digit = col
    row = 0
    while(len(squares) != 0):
        nextIndex = random.randint(0,len(squares)-1)
        if ((pos%10) //5 == 1):
            pos += 5 #if pos ends in 5, add 5 to get to next value
            grid.append([])
        row = pos//10
        grid[row].append(squares.pop(nextIndex))
        pos += 1

    return grid


def squaresList(redFirst):
    red = 8
    blue = 8
    black = 1
    brown = 7

    if redFirst:
        red += 1
    else:
        blue += 1
    
    squares = []
    for val in range(red):
        squares.append("red")
    for val in range(blue):
        squares.append("blue")
    for val in range(brown):
        squares.append("burlywood1")
    squares.append("gray14")

    return squares
#squaresList

def main():
    redFirst = bool(random.getrandbits(1)) #decide who goes first
    finalGrid = generateGrid(redFirst)

    return finalGrid, redFirst
    
main()

