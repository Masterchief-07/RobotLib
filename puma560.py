from RMatrix import RMatrix
from sympy import symbols, pi, pprint
theta_1, theta_2, theta_3, theta_4, theta_5, theta_6 = symbols("theta_1 theta_2 theta_3 theta_4 theta_5 theta_6")

T_0_1 = RMatrix.D(theta_1, -pi/2, 0, 671.83)
T_1_2 = RMatrix.D(theta_2, 0, 431.80, 139.70)
T_2_3 = RMatrix.D(theta_3, pi/2, -20.32, 0)
T_3_4 = RMatrix.D(theta_4, -pi/2, 0, 431.80)
T_4_5 = RMatrix.D(theta_5, pi/2, 0, 0)
T_5_6 = RMatrix.D(theta_6, 0, 0, 56.5)
pprint(T_0_1)
pprint(T_1_2)
pprint(T_2_3)
pprint(T_3_4)
pprint(T_4_5)
pprint(T_5_6)
