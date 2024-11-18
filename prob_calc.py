import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self,**objects):
    self.contents=[]
    for color, amount in objects.items():
      for x in range(amount):
        self.contents.append(color)

  def draw(self,draws):
    nothing=[]
    if(draws>len(self.contents)):
      return self.contents
    for x in range(draws):
      remove=self.contents.pop(int(random.random()*len(self.contents)))
      nothing.append(remove)
    return nothing

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  count=0
  for x in range(num_experiments):
    copy_balls=copy.deepcopy(expected_balls)
    hat_copy=copy.deepcopy(hat)
    colors_amount=hat_copy.draw(num_balls_drawn)
    
    for color in colors_amount:
      if(color is copy_balls):
        copy_balls[color]-=1

  
    if(x <=0 for x in copy_balls.values()):
      count+=1
  probability=count/num_experiments
  return probability
