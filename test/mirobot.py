from math import pi
from roboticstoolbox import DHRobot, RevoluteMDH, jtraj
from spatialmath import SE3

# robot = DHRobot(
#     [
#         RevoluteMDH(d=127),
#         RevoluteMDH(a=29.69, alpha=-pi/2, offset=-pi/2),
#         RevoluteMDH(a=108),
#         RevoluteMDH(d=168.98, a=20, alpha=-pi/2),
#         RevoluteMDH(alpha=pi/2, offset=pi/2),
#         RevoluteMDH(d=-24.8, alpha=pi/2)
#     ], name="mirobot"
# )

# print(robot)


class Mirobot(DHRobot):
    deg = pi/180
    def __init__(self):
        super().__init__(
            [
                RevoluteMDH(d=127, qlim=[-100*self.deg, 100*self.deg]),
                RevoluteMDH(a=29.69, alpha=-pi/2, offset=-pi/2, qlim=[-60*self.deg, 90*self.deg]),
                RevoluteMDH(a=108, qlim=[-180*self.deg, 50*self.deg]),
                RevoluteMDH(d=168.98, a=20, alpha=-pi/2, qlim=[-180*self.deg, 180*self.deg]),
                RevoluteMDH(alpha=pi/2, offset=pi/2, qlim=[-180*self.deg, 40*self.deg]),
                RevoluteMDH(d=-24.8, alpha=pi/2, qlim=[-180*self.deg, 180*self.deg])
            ], name="mirobot"
        )
mirobot = Mirobot()
print(mirobot)