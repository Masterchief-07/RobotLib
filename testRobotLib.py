from RMatrix import RMatrix
from RobotLib import RobotLib, CCD
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
algo = CCD();
rb.ik(np.array([[2],[2],[0]]), algo);
