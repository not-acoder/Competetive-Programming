import math
import numpy as np

ab=float(input())
bc=float(input())
ac= math.hypot(ab,bc)
#print(ac)
angle_a = bc/ac
angle_a=math.degrees(math.asin(angle_a))
#print(angle_a)
mbc = 90-angle_a
angle_a=round(angle_a)
print(angle_a)