from RMatrix import RMatrix
from sympy import pprint, symbols, Eq, lambdify
import numpy as np

"""
    simple implementation of CDD on a 2dof arm robot
"""

theta_1, theta_2, l_1, l_2= symbols("theta_1, theta_2, l_1, l_2")

T_0_1 = RMatrix.D(theta_1, 0, l_1, 0);
T_1_2 = RMatrix.D(theta_2, 0, l_2, 0);
T_0_2 = T_0_1*T_1_2

#DH matrix of differents joint
#pprint(T_0_1)
#pprint(T_1_2)
#pprint(T_0_2)

#joint position equation
v_0 = np.array([0,0]).astype(np.float32).reshape(2,1)
f_1 = lambdify((theta_1, l_1),T_0_1[:2,3],modules="numpy")
f_e = lambdify((theta_1, theta_2, l_1, l_2),T_0_2[:2,3],modules="numpy")

#print(v_0)
#print(f_1(0,2))
#print(f_e(0,0,2,2))

#ccd algo
def computccd(v_t:np.ndarray, v_e:np.ndarray, v_i:np.ndarray):
    v_t_i = v_t - v_i
    v_e_i = v_e - v_i
    print(v_t_i)
    a = v_t_i/(np.sqrt(np.sum(np.square(v_t_i))))
    b = v_e_i/(np.sqrt(np.sum(np.square(v_e_i))))
    return a.T.dot(b);

#simulation
v_t = np.array([[2.0],[2.0]]).astype(np.float32)
theta0, theta1 = 0.0, 0.0
l1, l2 = 2, 2

error = 1.0
while(error>0.5):
    #forward kinematics
    v_1 = f_1(theta0, l1)
    v_e = f_e(theta0, theta1, l1, l2)
    #ccd algo
    theta1 += computccd(v_t, v_e, v_1);
    v_e = f_e(theta0, theta1, l1, l2)
    theta0 += computccd(v_t, v_e, v_0);

    v_e = f_e(theta0, theta1, l1, l2)
    error = np.sum(np.square(v_t - v_e))
    print(f"error: {error}")
