import numpy as np

# Constants, change these as needed
INITIAL_GUESS = (-1, 0)  # initial guess as stated by the exercise
CYCLES = 10000  # maximum computational cycles
LEARN_RATE = 0.00001  # the learning rate, indicated by epsilon in problem

# Gradient functions
# Change these as needed
F_X = lambda x, y : (2 * x) + np.sin(10 * y) - (4 * np.sin(4 * x))
F_Y = lambda x, y : (2 * y) + (10 * x) * np.cos(10 * y)

# Minimise the gradient
min_F = lambda x, y, e : (F_X(x, y) * -e, F_Y(x, y) * -e)

# Maximise the gradient
max_F = lambda x, y, e : (F_X(x, y) * e, F_Y(x, y) * e)

# Approximate
guess = INITIAL_GUESS

i = 0
step_size = (float('inf'), float('inf'))
while i < CYCLES and np.abs(step_size[0]) >= LEARN_RATE and np.abs(step_size[1]) >= LEARN_RATE:
  step_size = min_F(guess[0], guess[1], LEARN_RATE)
  # print(step_size)

  guess = (guess[0] + step_size[0], guess[1] + step_size[1])
  i += 1
  
print(guess)
