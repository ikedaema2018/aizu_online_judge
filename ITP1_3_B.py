data = [
  "3",
  "5",
  "11",
  "7",
  "8",
  "19",
  "0"
]
def input():
  return data.pop(0)

count = 1
it = int(input())
while it != 0:
  print(f"Case {count}: {it}")
  count += 1
  it = int(input())