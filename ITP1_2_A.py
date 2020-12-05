data = ["100 1"]
def input():
  return data.pop(0)

[a, b] = list(map(int, input().split(" ")))

if a == b:
  print("a == b")
elif a > b:
  print("a > b")
elif a < b:
  print("a < b")