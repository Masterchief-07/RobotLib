from RMatrix import RMatrix
from RobotLib import RobotLib, CCD
import sympy as sp
import numpy as np

"""
rb = RobotLib()
rb.add(alpha=0, r=2, d=0)
rb.add(alpha=0, r=5, d=0)
rb.add(alpha=0, r=2, d=0)
rb.add(alpha=0, r=2, d=0)
rb.add(alpha=0, r=2, d=0)
#sp.pprint(rb.T_0_N)
#sp.pprint(rb.parts)
pos = rb.fk([0.0,0.0,0.0,0.0,0.0])
#pos = rb.fk([1.0,0.0])
#print(pos)
ccd = CCD();
#rb.ik(np.array([[2],[5],[0]]), ccd);
pos = rb.fk([0.0,0.0,0.0,0.0,0.0])
rb.ik(np.array([[5],[5],[0]]),ccd);
"""

rb = RobotLib()
rb.add(alpha=sp.pi/2, r=0, d=5)
rb.add(alpha=0, r=5, d=0)
rb.add(alpha=0, r=5, d=0)
#sp.pprint(rb.T_0_N)
#sp.pprint(rb.parts)
#print(rb.angles)
#pos = rb.fk([np.pi,np.pi/2.0,0.0])
#pos = rb.fk([1.0,0.0])
#print(pos)
ccd = CCD();
rb.ik(np.array([[5],[5],[5]]), ccd);
