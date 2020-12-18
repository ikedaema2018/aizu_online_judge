# 三角関数がわからないのでネットで回答を見た
# Radian = pi * 度数 / 180
# 面積 = sin * a * b / 2
# 周の長さ = a + b + aの2乗 + bの2乗 - 2 * a * b * cos
# aを底辺にしたときの三角形の高さ = b * sin

data = [
  "100 80 54"
]

def input():
  return data.pop(0)

import math

def to_radian(d):
  return math.pi * c / 180


s = input()
a,b,c = map(int, s.split(" "))

r = to_radian(c)
S = math.sin(r) * a * b / 2
L = a + b + math.sqrt(a**2 + b**2 - 2*a*b*math.cos(r))
h = b*math.sin(r)

print("{0:.8f}".format(S))
print("{0:.8f}".format(L))
print("{0:.8f}".format(h))