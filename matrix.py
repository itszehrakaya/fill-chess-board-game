import numpy as np

cols = np.arange(10,90,10)
rows = np.arange(1, 9)
cols[:, np.newaxis] + rows
