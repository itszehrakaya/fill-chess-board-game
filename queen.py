import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x, y = np.ogrid[:8, :8]
def queen(i):
    turn = 0
    indexList = []
    while turn < i:
        turn += 1
        location = int(input())
        row = location//10 - 1 
        col = location%10 - 1

        findIndex = np.where((x + y == col+ row) | 
                     (x - y == abs(col-row)) |
                     (x == row)  | (y==col ), x, -1 )
        
        getIndex  = np.where(findIndex != -1)
        indexList.append(list(zip(getIndex[0], getIndex[1])))

        plt.imshow(findIndex)
        print(indexList)

queen(5)
plt.show()
