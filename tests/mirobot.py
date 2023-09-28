from math import pi, radians
import numpy as np
from roboticstoolbox import DHRobot, RevoluteMDH
import spatialmath.base as smb


class Mirobot(DHRobot):
    """比邻星机械臂建模"""
    def __init__(self):
        super().__init__(
            [
                RevoluteMDH(d=127, qlim=[radians(-100), radians(100)]),
                RevoluteMDH(a=29.69, alpha=-pi/2, offset=-pi/2, qlim=[radians(-60), radians(90)]),
                RevoluteMDH(a=108, qlim=[radians(-180), radians(50)]),
                RevoluteMDH(d=168.98, a=20, alpha=-pi/2, qlim=[radians(-180), radians(180)]),
                RevoluteMDH(alpha=pi/2, offset=pi/2, qlim=[radians(-180), radians(40)]),
                RevoluteMDH(d=-24.8, alpha=pi/2, qlim=[radians(-180), radians(180)])
            ], 
            name = "mirobot",
            manufacturer = "BLinx"
        )
        self.qr = np.array([0, radians(90), radians(90), 0, 0, 0])
        self.qz = np.zeros(6)
        self.addconfiguration("qr", self.qr)
        self.addconfiguration("qz", self.qz)

    
if __name__ == "__main__":    
    mirobot = Mirobot()
    print(mirobot)
    
    q1 = radians(20)
    q2 = radians(10)
    q3 = radians(-15)
    q4 = radians(-10)
    q5 = radians(10)
    q6 = radians(10)
    # fig = mirobot.plot(mirobot.qz)
    T = mirobot.fkine(np.array([q1, q2, q3, q4, q5, q6]))
    
    # T = sm.SE3.Trans(0.6, 0.1, 0) * sm.SE3(smb.rpy2tr(0, 180, 0, 'deg'))
    print(T, '\n')
    
    # print(q.q)
    # qt = tools.trajectory.jtraj(mirobot.qz, mirobot.qr, 50)
    # fig = mirobot.plot(qt.q)
    # fig.hold()
    