data = [
  "3 4",
  "5 6",
  "2 2",
  "0 0"
]

def input():
  return data.pop(0)

[h, w] = list(map(int, input().split(" ")))

while h != 0 or w != 0:
  for i in range(0, h):
    print("#" * w)
  
  print()
  [h, w] = list(map(int, input().split(" ")))