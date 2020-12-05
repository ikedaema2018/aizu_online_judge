data = ["3 5"]
def input():
  return data.pop(0)

[h, w] = list(map(lambda x: int(x), input().split(" ")))
print(h * w, (h + w) * 2)