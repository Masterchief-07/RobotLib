import sympy as sp
import numpy as np

class RMatrix:
    #robot Matrix 4x4
    def __init__(self):
        self.matrix = np.array(4,4)

    def get(self, x, y):
        assert(x<4 && y<4)
        return self.matrix[x][y];
