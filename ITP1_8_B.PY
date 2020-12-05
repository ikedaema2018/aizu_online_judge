data = [
  "This is a pen."
]

def input():
  return data.pop(0)

import string

d = {}

for s in list(string.ascii_lowercase):
  d[s] = 0
  
s = ""
while True:
  try:
    s += input().lower()
  except:
    break
  
s_exclude_br = (" ").join(s.splitlines())
sr = list(s_exclude_br)

for s in sr:
  s = s.lower()
  if not s in d:
    continue
  d[s] = d[s] + 1

for k, v in d.items():
  print(f"{k} : {v}")
  
