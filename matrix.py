import matplotlib.pyplot as plt
import numpy as np

cols = np.arange(10,90,10)
rows = np.arange(1, 9)
Board = cols[:, np.newaxis] + rows

plt.imshow(Board)

plt.show()
print(Board)
