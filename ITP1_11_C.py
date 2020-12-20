data = [
  "10 20 30 40 50 60",
  "10 20 30 40 50 60"
]

def input():
  return data.pop(0)

class Dice:
  def __init__(self, squares):    
    self.top = squares[0]
    self.front = squares[1]
    self.right = squares[2]
    self.left = squares[3]
    self.rear = squares[4]
    self.bottom = squares[5]

  def shake_the_top(self, direction):
    tmp_top = self.top
    if direction == "S":
      self.top = self.rear
      self.rear = self.bottom
      self.bottom = self.front
      self.front = tmp_top
    if direction == "N":
      self.top = self.front
      self.front = self.bottom
      self.bottom = self.rear
      self.rear = tmp_top
    if direction == "E":
      self.top = self.left
      self.left = self.bottom
      self.bottom = self.right
      self.right = tmp_top
    if direction == "W":
      self.top = self.right
      self.right = self.bottom
      self.bottom = self.left
      self.left = tmp_top
    
  def right_value_by_after_shake_the_top(self, top, front):
    if top == self.rear and front == self.top:
      print(self.right)
      return True
    elif top == self.front and front == self.bottom:
      print(self.right)
      return True
    elif top == self.left and front == self.front:
      print(self.top)
      return True
    elif top == self.right and front == self.front:
      print(self.bottom)
      return True
    
  def get_label(self):
    return [self.top, self.front, self.right, self.left, self.rear, self.bottom]
        
dice = Dice(list(map(int,input().split(" "))))

d2_label = list(map(int, input().split(" ")))
for s in 'EEENEEENEEESEEESEEENEEEN':
  if dice.get_label() == d2_label:
    print("Yes")
    break
  dice.shake_the_top(s)
else:
  print("No")
    
  
  
  
