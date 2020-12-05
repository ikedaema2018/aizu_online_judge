data = ["5 4 2 4 1"]
def input():
  return data.pop(0)

[w, h, x, y, r] = list(map(int, input().split()))

if x + r <= w and x - r >=0 and y + r <= h and y - r >= 0:
  print("Yes")
else:
  print("No") 