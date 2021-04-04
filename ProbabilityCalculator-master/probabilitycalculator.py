import random
import copy

class Hat:
    def __init__(self, **balls):
        self.contents = []
        for key, value in balls.items():
            self.contents = self.contents + [key] * value

    def draw(self, number_to_be_drawn):
        length_contents = len(self.contents)
        if number_to_be_drawn >= length_contents:
            return self.contents
        drawn = []
        for i in range(number_to_be_drawn):
            x = random.randint(1, length_contents - i) - 1
            drawn.append(self.contents.pop(x))
        return drawn

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    count = 0
    for _ in range(num_experiments):
        new_hat = copy.deepcopy(hat)
        drawn = new_hat.draw(num_balls_drawn)
        for key, value in expected_balls.items():
            if drawn.count(key) < value:
                count += 1
                break
    return 1 - count / num_experiments
    
    
# TEST CASES
# my_hat = Hat(blue=3,red=2,green=6)
# print(experiment(hat=my_hat, expected_balls={"blue":2, "green":1}, num_balls_drawn=4, num_experiments=100000))

# hat2 = Hat(yellow=5, red=1, green=3, blue=9, test=1)
# print(experiment(hat = hat2, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn = 20, num_experiments = 100))
            
    
            
