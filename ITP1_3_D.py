data = ["5 14 80"]

def input():
  return data.pop(0)

[a, b, c] = list(map(int, input().split(" ")))

count = 0
for i in range(a, b+1):
  if c % i == 0:
    count += 1
    
print(count)