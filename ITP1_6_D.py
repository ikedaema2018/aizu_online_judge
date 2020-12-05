data = [
  "40 42 -1",
  "20 30 -1",
  "0 2 -1",
  "-1 -1 -1"
]

def input():
  return data.pop(0)

[m, f, r] = list(map(int, input().split(" ")))

while m != -1 or f != -1 or r != -1:
  if m == -1 or f == -1:
    print("F")
  elif m + f >= 80:
    print("A")
  elif m + f >= 65:
    print("B")
  elif m + f >= 50:
    print("C")
  elif m + f >= 30:
    if r >= 50:
      print("C")
    else:
      print("D")
  elif m + f < 30:
    print("F")
    
  [m, f, r] = list(map(int, input().split(" ")))
  
  