data = ["1 3 8"]
def input():
  return data.pop(0)

[a, b, c] = list(map(int, input().split(" ")))

if a < b and b < c:
  print("Yes")
else:
  print("No")