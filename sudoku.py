from itertools import product
from printer import pretty_print
import time


def possible(n, x, y, grid):
    x0 = (x // 3) * 3 # x start of current 3X3 cube
    y0 = (y // 3) * 3 # y start of  current 3X3 cube

    # got 3 arms - k for iterating over rows and columns (0-8), i & j for iterating over the cube (0-2)
    for k, (i, j) in enumerate(product(range(3), repeat = 2)): 
        rcc = {grid[k][y], grid[x][k], grid[x0 + i][y0 + j]} # current spots on row, colums and cube
        
        if n in rcc: return False

    return True


def solutions(grid): # yields solved grids
    for i, j in product(range(9), repeat = 2): 
        if grid[i][j] == 0:
            for n in range(1, 10):
                if possible(n, i, j, grid):
                    grid[i][j] = n
                    yield from solutions(grid)
                    grid[i][j] = 0
                    
            return

    yield grid



def main():
    grid = [[5, 3, 0, 0, 7, 0, 0, 0, 0],
            [6, 0, 0, 1, 9, 5, 0, 0, 0],
            [0, 9, 8, 0, 0, 0, 0, 6, 0],
            [8, 0, 0, 0, 6, 0, 0, 0, 3],
            [4, 0, 0, 8, 0, 3, 0, 0, 1],
            [7, 0, 0, 0, 2, 0, 0, 0, 6],
            [0, 6, 0, 0, 0, 0, 2, 8, 0],
            [0, 0, 0, 4, 1, 9, 0, 0, 5],
            [0, 0, 0, 0, 8, 0, 0, 0, 0]]

    pretty_print(grid)
    #input('press entr for a solution>')

    for i in solutions(grid):
        pretty_print(i)
        #input('enter again to look for more solutions>')

    print('sorry, that\'s all folks')


if __name__ == "__main__":
    start = time.time()
    main()
    end = time.time()
    print(end - start)
    
