import sympy as sp
from sympy import symbols, Matrix, cos , sin, tanh, pprint
import numpy as np

class RMatrix:
    #robot Matrix 4x4
    def __init__(self):
        self.matrix = sp.zeros(4,4)

    def get(self, x, y):
        assert(x<4 and x>=0 and y<4 and y>=0)
        return self.matrix[x,y]

    def print(self):
        pprint(self.matrix)

    def add_T(theta=symbols("theta"), alpha=symbols("alpha"), r=symbols("r"), d=symbols("d")):
        pass

    @staticmethod
    def D(theta=symbols("theta"), alpha=symbols("alpha"), r=symbols("r"), d=symbols("d")):
        """
            Denavite hartenberg Matrix
        """
        return Matrix([
            [cos(theta), -sin(theta)*cos(alpha), sin(theta)*sin(alpha), r*cos(theta)],
            [sin(theta), cos(theta)*cos(alpha), -cos(theta)*sin(alpha), r*sin(theta)],
            [0, sin(alpha), cos(alpha), d],
            [0, 0, 0, 1],
            ])

    @staticmethod
    def I(theta=symbols("theta")):
        """
           Identity homogenous matrix 
        """
        return Matrix([
            [1,0,0,0],
            [0,1,0,0],
            [0,0,1,0],
            [0,0,0,1]])

    @staticmethod
    def Rx(theta=symbols("theta")):
        """
            Homogenous rotation Matrix around X axis
        """
        return Matrix([
            [1,0,0,0],
            [0,cos(theta),-sin(theta), 0],
            [0,sin(theta), cos(theta), 0],
            [0,0,0,1]])

    @staticmethod
    def Ry(theta=symbols("theta")):
        """
            Homogenous rotation Matrix around Y axis
        """
        return Matrix([
            [cos(theta),0,sin(theta),0],
            [0,1,0, 0],
            [-sin(theta),0, cos(theta), 0],
            [0,0,0,1]])


    @staticmethod
    def Rz(theta=symbols("theta")):
        """
            Homogenous rotation Matrix around Z axis
        """
        return Matrix([
            [cos(theta),-sin(theta),0,0],
            [sin(theta),cos(theta),0, 0],
            [0,0, 1, 0],
            [0,0,0,1]])



    @staticmethod
    def Tx(x = symbols("x")):
        """
            Homogenous Translation Matrix on X axis
        """
        a = sp.eye(4)
        a[0,3] = x
        return a
    @staticmethod
    def Ty(y = symbols("y")):
        """
            Homogenous Translation Matrix on Y axis
        """
        a = sp.eye(4)
        a[1,3] = y
        return a

    @staticmethod
    def Tz(z = symbols("z")):
        """
            Homogenous Translation Matrix on Z axis
        """
        a = sp.eye(4)
        a[2,3] = z
        return a
