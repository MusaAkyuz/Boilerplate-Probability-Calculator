import copy
import random
# Consider using the modules imported above.

class Hat:
  def __init__(self, **balls):
    self.contents = []
    self.balls = balls
    for key, value in self.balls.items():
        for count in range(int(value)):
            self.contents.append(key)

  def draw(self, count):
    if count <= len(self.contents):
        balls_drawn = []
        for i in range(count):
            rand_int = random.randrange(len(self.contents))
            balls_drawn.append(self.contents[rand_int])
            self.contents.pop(rand_int)  
        return balls_drawn
    else:
      return self.contents
    
def experiment(hat, expected_balls, num_balls_drawn, num_experiments):  
  
  expected = []

  for key, value in expected_balls.items():
    for count in range(int(value)):
      expected.append(key)
      
  M = 0
  for count in range(num_experiments):
    hat_content = copy.deepcopy(hat)
    balls_drawn = hat_content.draw(num_balls_drawn)
    count = 0
    for item in expected:
      if balls_drawn.count(item) >= expected.count(item):
        count += 1
    if count == len(expected):
      M += 1
      
  return M / num_experiments