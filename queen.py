import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def queen(t):
  Board = np.add.outer(range(8), range(8)) %2
  turn = 0
  while turn < t:
    turn += 1
    row = int(input("row:"))
    col = int(input("column:"))
    for idx, i in np.ndenumerate(Board):
      x = idx[0]
      y = idx[1]
      idxList = []
      if (x + y == col+ row) or  (x - y == abs(col-row))  or (x == row) or (y==col ):
        idxList.append(idx)
        for a in idxList:
          Board[a] =  -1          
    plt.imshow(Board)
    plt.show()
queen(5)
plt.show()
