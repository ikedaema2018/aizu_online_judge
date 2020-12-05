data = [
  "3 2",
  "2 2",
  "5 3",
  "0 0"
]

def input():
  return data.pop(0)

[a, b] = list(map(int, input().split(" ")))
while a != 0 and b != 0:
  if a > b:
    print(f"{b} {a}")
  else:
    print(f"{a} {b}")
  [a, b] = list(map(int, input().split(" ")))

