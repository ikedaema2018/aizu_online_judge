data = ["2 100000009"]

def input():
  return data.pop(0)

[a, b] = list(map(int, input().split(" ")))

print(f"{a // b} {a % b} {a / b}")