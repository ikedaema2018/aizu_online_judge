data = ["3"]

def input():
  return data.pop(0)

import math

r = int(input())

menseki = r * r * math.pi
ennshuu = 2 * r * math.pi

print(f"{menseki} {ennshuu}")