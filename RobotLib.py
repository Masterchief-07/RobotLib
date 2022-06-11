import sympy as sp
from sympy import symbols, lambdify
import numpy as np
from numpy import ndarray
from RMatrix import RMatrix
from itertools import accumulate

class RobotLib:

    def __init__(self):
        self.parts = [];
        self.parts_f = [];  #parts function
        self.parts_p = [];  #parts parameters
        self.angles = [];   #angles
        self.pos = [];      #pos of every articulations
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
        pos = (self.parts_f[i](angles[i]) for i in range(len(self.parts_f)))
        pos = tuple(accumulate(pos))
        self.pos = pos;
        return pos;
    
    def ik(self, target:ndarray, algo:object):
        """
            inverse kinematics using a algo
        """
        self.angles = algo.ik(self.angles, self.parts_f, target); 
        return self.angles


class CCD(object):
    """
        CCD algo class
    """
    def __init__(self, err_threshold = 0.0001):
        self.angles=None;
        self.pos = None;
        self.errors = 0;
        self.err_threshold = err_threshold

    def comput(self,v_t:ndarray, v_e:ndarray, v_i:ndarray):
        """
            comput ccd 
        """
        v_e_i = v_e - v_i;
        v_t_i = v_t - v_i;

        a = v_t_i / np.linalg.norm(v_t_i);
        b = v_e_i / np.linalg.norm(v_e_i);

        r = a.T.dot(b)[0].item();
        angle = np.arccos(r).item();
        return angle

    def fk(self, angles, functs, start_at=0):
        """
            forward kinematics at any angles
            to speed the calculation of the endefactor after each angle update
        """
        assert(start_at >= 0 and start_at < len(functs) and len(angles) == len(functs))
        if(start_at == 0 or self.pos==None):
            self.pos=tuple(accumulate(functs[i](angles[i])for i in range(len(functs))))
            return self.pos
        pos = tuple(accumulate((functs[i](angles[i])for i in range(start_at, len(functs))), initial=self.pos[start_at-1]))[1:]
        return pos

    def cerror(self, v_t:ndarray, v_e:ndarray):
        """
            comput the error betwean the endefactor and the target
        """
        return np.linalg.norm(v_t-v_e)
        


    def ik(self,angles:list, functs:list, target:ndarray):
        self.errors = 0;
        self.angles = list(angles)
        pos = self.fk(angles, functs)
        v_t = target;
        error = 1;
        iteration = 0
        while error>self.err_threshold:
            for i in reversed(range(len(angles))):
                #print("------------------------------")
                pos = self.fk(self.angles, functs, i-1 if i-1>=0 else 0);
                #print(f"{i} : {pos}")
                #print(f"v_e: {pos[-1]}")
                theta = self.comput(v_t, pos[-1], pos[0]) if i>0 else self.comput(v_t, pos[-1], np.array([[0],[0],[0]]))
                #print(f"thetat: {theta}")
                self.angles[i] += theta
                #print(f"angles: {self.angles}")
                error = self.cerror(v_t, pos[-1])
                #print(f"error = {error}")
            iteration+=1
            #print(f"------------------------------{iteration}------------------------------")
        print(f"n{iteration}\n error:{error}\n v_e:{pos[-1]}\n angles:{self.angles}\n")
        return self.angles
                    



