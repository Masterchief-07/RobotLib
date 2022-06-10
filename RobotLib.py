import sympy as sp
from sympy import symbols, lambdify
import numpy as np
from RMatrix import RMatrix
from itertools import accumulate

class RobotLib:

    def __init__(self):
        self.parts = [];
        self.parts_f = []; #parts function
        self.parts_p = []; #parts parameters
        self.T_0_N = None;

    def add(self, theta=None, alpha=None, r=None, d=None):
        """
            add at DH matrix
        """
        n = len(self.parts)+1
        params = [];
        if(theta==None):
            theta = symbols("theta_{}".format(n))
            params.append(theta)
        if(alpha==None):
            alpha = symbols("alpha_{}".format(n))
            params.append(alpha)
        if(r==None):
            r = symbols("r_{}".format(n))
            params.append(r)
        if(d==None):
            d = symbols("d_{}".format(n))
            params.append(d)
        T = RMatrix.D(theta, alpha, r, d);
        f = lambdify(params, T[:3,3], modules="numpy")
        self.parts_p.append(tuple(params))
        self.parts_f.append(f)
        self.parts.append(T);
        self.T_0_N = T if self.T_0_N ==None else self.T_0_N*T;
        #sp.pprint(T)

    def fk(self,angles:list):
        """
            forward kinematics of every T
        """
        assert(len(self.parts) == len(angles))
        pos = [self.parts_f[i](angles[i]) for i in range(len(self.parts_f))]
        pos = tuple(accumulate(pos))
        return pos;


