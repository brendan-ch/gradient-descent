import numpy as np

# Constants, change these as needed
INITIAL_GUESS = (2, 3)  # initial guess as stated by the exercise
CYCLES = 10000  # maximum computational cycles
LEARN_RATE = 0.00001  # the learning rate, indicated by epsilon in problem
H = 0.00001
RANGE = 2

# Original function
# Change as needed
F = lambda x, y : np.square(x) + np.square(y) + (x * np.sin(10 * y)) + np.cos(4 * x)

# Obtain an approximation of the derivative
# Keep these as is
F_X = lambda x, y : (F(x + H, y) - F(x - H, y)) / (2 * H)
F_Y = lambda x, y : (F(x, y + H) - F(x, y - H)) / (2 * H)
min_F = lambda x, y : (F_X(x, y) * -LEARN_RATE, F_Y(x, y) * -LEARN_RATE)
max_F = lambda x, y : (F_X(x, y) * LEARN_RATE, F_Y(x, y) * LEARN_RATE)

def descend(initial_guess):
  # Approximate
  guess = initial_guess

  i = 0
  step_sizes = (float('inf'), float('inf'))
  while i < CYCLES and np.abs(step_sizes[0]) >= LEARN_RATE and np.abs(step_sizes[1]) >= LEARN_RATE:
    step_sizes = min_F(guess[0], guess[1])
    # print(step_sizes)

    guess = (guess[0] + step_sizes[0], guess[1] + step_sizes[1])
    i += 1

  return guess

min_point = descend(INITIAL_GUESS)
min_value = F(min_point[0], min_point[1])

# Get the neighboring points
for x in range(int(np.round(min_point[0] - RANGE)), int(np.round(min_point[0] + RANGE))):
  for y in range(int(np.round(min_point[1] - RANGE)), int(np.round(min_point[1] + RANGE))):
    guess = descend((x, y))
    if F(guess[0], guess[1]) < min_value:
      min_point = guess
      min_value = F(guess[0], guess[1])

print(min_point)