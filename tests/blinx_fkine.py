from math import pi, atan2, sqrt, cos, fabs, degrees


def blinx_fkine(R):
    """比邻星机械臂正运动解"""
    ry = atan2(-R[2][0], sqrt(R[0][0]*R[0][0] + R[1][0]*R[1][0]))

    if (fabs(ry - pi*0.5) <= 0.0001):
        ry = pi*0.5
        rz = 0.0
        rx = atan2(R[1][1], R[0][1])
    else:
        if (fabs(ry + pi*0.5) <= 0.0001):
            ry = -pi*0.5
            rz = 0.0
            rx = -atan2(R[1][1], R[0][1])
        else:
            rx = atan2(R[2][1]/cos(ry), R[2][2]/cos(ry))
        rz = atan2(R[1][0]/cos(ry), R[0][0]/cos(ry))
        
    return [degrees(rx) , degrees(ry), degrees(rz)]
