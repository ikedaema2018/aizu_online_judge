data = ["3 8 1"]
def input():
  return data.pop(0)

list = list(map(int, input().split(" ")))
print((" ").join(map(str, sorted(list))))

