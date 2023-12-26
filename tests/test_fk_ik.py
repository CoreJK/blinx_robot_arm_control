import timeit

fk_setup = """
import sys
sys.path.append("..")
from common.blinx_robot_module import Mirobot
from math import radians
import numpy as np
import timeit
mirobot = Mirobot()
q1 = radians(-15)
q2 = radians(-10)
q3 = radians(15)
q4 = radians(10)
q5 = radians(-5)
q6 = radians(-5)
"""

fk_code = """
translation_vector = mirobot.fkine(np.array([q1, q2, q3, q4, q5, q6]))
"""

ik_setup = """
import sys
sys.path.append("..")
from common.blinx_robot_module import Mirobot
from math import radians
from spatialmath import SE3
from spatialmath.base import rpy2tr
import numpy as np
import timeit
import shelve
fk_data = shelve.open('fk_data')
fk_xyz = fk_data['fk_res']
fk_data.close()
mirobot = Mirobot()
q1 = radians(-15)
q2 = radians(-10)
q3 = radians(15)
q4 = radians(10)
q5 = radians(-5)
q6 = radians(-5)
x, y, z = fk_xyz.t  # 平移向量，坐标
Rx, Ry, Rz = fk_xyz.rpy()
"""

ik_code = """
R_T = SE3([x, y, z]) * rpy2tr([Rz, Ry, Rx], unit='deg')
sol = mirobot.ikine_LM(R_T, joint_limits=True)
"""

# timeit.timeit 测试代码执行耗时
# 正解函数耗时测试，单位 s
fk_taking_time = timeit.timeit(stmt=fk_code, setup=fk_setup, number=1)
print("正解函数耗时: {} ms".format(fk_taking_time * 1000) )

# 逆解函数耗时测试, 单位 s
ik_taking_time = timeit.timeit(stmt=ik_code, setup=ik_setup, number=1)
print("逆解函数耗时: {} ms".format(ik_taking_time * 1000))

# timeit.repeat 测试代码执行耗时
# 正解函数耗时测试
fk_taking_time_re = timeit.repeat(setup=fk_setup, stmt=fk_code, number=1)
print(fk_taking_time_re)
print("正解函数最小耗时: {} ms, 最大耗时: {} ms".format(min(fk_taking_time_re) * 1000, max(fk_taking_time_re) * 1000))

# 逆解函数耗时测试
ik_taking_time_re = timeit.repeat(setup=ik_setup, stmt=ik_code, number=1)
print(ik_taking_time_re)
print("逆解函数最小耗时: {} ms, 最大耗时: {} ms".format(min(ik_taking_time_re) * 1000, max(ik_taking_time_re) * 1000))