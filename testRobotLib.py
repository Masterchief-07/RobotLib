from RMatrix import RMatrix
from RobotLib import RobotLib
import sympy as sp
import numpy as np

rb = RobotLib()
rb.add(alpha=0, r=2, d=0)
rb.add(alpha=0, r=2, d=0)
rb.add(alpha=0, r=2, d=0)
rb.add(alpha=0, r=2, d=0)
rb.add(alpha=0, r=2, d=0)
#sp.pprint(rb.T_0_N)

pos = rb.fk([0.0,0.0,0.0,0.0,0.0])
print(pos)
