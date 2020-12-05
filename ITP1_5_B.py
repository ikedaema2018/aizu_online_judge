data = [
  "2 2",
  "3 3",
  "0 0"
]

def input():
  return data.pop(0)

[h, w] = list(map(int, input().split(" ")))

while h is not 0 or w is not 0:
  h_flag = True
  for i in range(0, h):
    w_flag = False
    if h_flag:
      w_flag = True
    else:
      w_flag = False
    str = ""
    for j in range(0,w):
      if w_flag:
        str += "#"
      else:
        str += "."
      w_flag = not w_flag
    print(str)
    h_flag = not h_flag
  print()
  [h, w] = list(map(int, input().split(" ")))
  