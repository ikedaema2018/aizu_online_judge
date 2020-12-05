data = ["46979"]
def input():
  return data.pop(0)

sec = int(input())

h = sec // 3600
sec_h = sec % 3600
m = sec_h // 60
sec_m = sec_h % 60

print(f"{h}:{m}:{sec_m}")