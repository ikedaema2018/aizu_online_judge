data = [
  "3",
  "1 1 3 8",
  "3 2 2 7",
  "4 3 8 1"
]

def input():
  return data.pop(0)

appart = []
for i in range(0, 4):
  appart.append([[], [], []])

for i in range(0, len(appart)):
  for j in range(0, len(appart[i])):
    appart[i][j] = [0] * 10
    
leng = int(input())

for i in range(0, leng):
  info = list(map(int, input().split(" ")))
  appart[info[0] - 1][info[1] - 1][info[2] - 1] += info[3]  
  
for i in range(0, len(appart)):
  for floor in appart[i]:
    print(" " + " ".join(map(str, floor)))
  if i != len(appart) - 1:
    print("####################")
  
