data = [
  "5",
  "10 1 5 4 17"
]

def input():
  return data.pop(0)

input()
list = list(map(int, input().split(" ")))

print(f"{min(list)} {max(list)} {sum(list)}")
