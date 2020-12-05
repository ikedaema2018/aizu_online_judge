data = [
  "1 + 2",
  "1 * 2",
  "1 - 2",
  "1 / 2",
  "0 ? 0"
]

def input():
  return data.pop(0)

[s_o1, operator, s_o2] = list(input().split(" "))

while operator != "?":
  if operator == "+":
    print(int(s_o1) + int(s_o2))
  elif operator == "*":
    print(int(s_o1) * int(s_o2))
  elif operator == "-":
    print(int(s_o1) - int(s_o2))
  elif operator == "/":
    print(int(s_o1) // int(s_o2))
  [s_o1, operator, s_o2] = list(input().split(" "))
