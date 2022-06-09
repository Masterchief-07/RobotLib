from RMatrix import RMatrix
from sympy import pprint, symbols, Eq, Matrix, solveset,linsolve, nonlinsolve, solve

theta_1, theta_2, l_1, l_2, x, y = symbols("theta_1 theta_2 l_1 l_2 x y");

T_0_1 = RMatrix.D(theta_1, 0, l_1, 0);
T_1_2 = RMatrix.D(theta_2, 0, l_2, 0);
T_0_2 = T_0_1 * T_1_2
equations = T_0_2[:2,3]
a = Eq(equations[0]-x,0)
b = Eq(equations[1]-y,0)
pprint(T_0_1)
pprint(T_1_2)
pprint(T_0_2)
pprint(T_0_2.rref())
pprint(a)
pprint(b)
#pprint(solveset(Eq(a,x), theta_1))
#pprint(linsolve([a,b], theta_1, theta_2))
pprint(nonlinsolve([a,b], theta_1, theta_2))
