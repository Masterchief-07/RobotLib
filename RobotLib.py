import sympy as sp
from sympy import symbols, lambdify
import numpy as np
from numpy import ndarray
from RMatrix import RMatrix
from itertools import accumulate

class RobotLib:

    def __init__(self):
        self.parts = [];
        self.parts_f = []; #parts function
        self.parts_p = []; #parts parameters
        self.angles = [];
        self.pos = [];
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
        self.angles = angles;
        pos = [self.parts_f[i](angles[i]) for i in range(len(self.parts_f))]
        pos = tuple(accumulate(pos))
        self.pos = pos;
        return pos;
    
    def ik(self, target:ndarray, algo:object):
        """
            inverse kinematics using a algo
        """
        algo.ik(self.angles, self.pos, self.parts_f, target); 
        pass



class CCD(object):
    """
        CCD algo class
    """
    def __init__(self, err_threshold = 0.001):
        self.angles=[];
        self.pos = [];
        self.errors = 0;
        self.err_threshold = err_threshold

    def comput(self,v_t:ndarray, v_e:ndarray, v_i:ndarray):
        """
            comput ccd 
        """
        v_e_i = v_e - v_i;
        v_t_i = v_t - v_i;

        a = v_t_i / np.linalg.norm(v_t_i);
        b = v_e_i / np.linalg.norm(v_i_i);

        r = a.T.dot(b)[0].item();
        angle = np.arccos(r);
        return angle

    def ik(self,angles:list, pos:list, funct:list, target:ndarray):
        self.errors = 0;
        self.angles = list(angles)
        self.pos = list(pos)
        while self.errors>self.err_threshold:
            for i in reversed(range(len(funct)-1)):
                pass
                

                



