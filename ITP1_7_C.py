data = [
  "4 5",
  "1 1 3 4 5",
  "2 2 2 4 5",
  "3 3 0 1 1",
  "2 3 4 4 6"
]

def input():
  return data.pop(0)

[h, w] = list(map(int, input().split(" ")))
result = []
for _ in range(0, h):
  r = list(map(int, input().split(" ")))
  s = sum(r)
  result.append(r + [s])

bottom = []
for i in range(0, w + 1):
  sum = 0
  for j in range(0, h):
    sum += result[j][i]
  bottom.append(sum)
result.append(bottom)

for i in range(0, len(result)):
  print((" ").join(map(str, result[i])))
