# Gradient Descent Algorithm

This project is an extra credit assignment for MATH 210, section 02 (spring 2023) at Chapman University.

# Running the code

Start by creating and activating the Python virtual environment:

```
python -m venv .env
source .env/bin/activate
```

Install `numpy` and other dependencies:

```
pip install -r requirements.txt
```

Then, run each exercise like so:

```
python exercise1.py
python exercise2.py
python exercise3.py
```

# Notes

## Exercise 1

In this exercise, the gradient of F is stored in the code.

```python
# Gradient functions
F_X = lambda x, y : (2 * x) + np.sin(10 * y) - (4 * np.sin(4 * x))
F_Y = lambda x, y : (2 * y) + (10 * x) * np.cos(10 * y)
```

With `LEARN_RATE` set to `0.00001`, the final guess ends with something close to `(-0.8962922428213529, 0.14270553189951954)`. Plotted on a graph:

<img width="974" alt="Math3D scene with a local minimum" src="https://github.com/brendan-ch/gradient-descent/assets/34608561/fca3fdda-293f-45d0-95cd-daf39a12b447">

[See full Math3D scene](https://www.math3d.org/qrkeSXBDy)

## Exercise 2

Same as exercise 1, but approximates the gradient of F using a difference quotient. The original function F is stored in the code.

```python
# Original function
# Change as needed
F = lambda x, y : np.square(x) + np.square(y) + (x * np.sin(10 * y)) + np.cos(4 * x)

# Obtain an approximation of the derivative
# Keep these as is
F_X = lambda x, y : (F(x + H, y) - F(x - H, y)) / (2 * H)
F_Y = lambda x, y : (F(x, y + H) - F(x, y - H)) / (2 * H)
```

With `LEARN_RATE` and `H` both set to `0.00001`, the final guess ends with something close to `(-0.8962922428272383, 0.14270553184258455)`.

## Exercise 3

This exercise changes the starting point to (2, 3). Running the above code with this point will cause it to stop at a saddle point `(2.0000094546460945, 2.9999091497100734)` after just 1 descent cycle.

To make the code more likely to find the global minimum, I changed the algorithm to check the points around the initial guess. Then, I calculated the actual minimum for each of these points and returned the lowest point. I continued to do this until the minimum point stopped changing.

```python
# Moved gradient descent logic into a function
def descend(initial_guess):
  # Approximate
  guess = initial_guess

  i = 0
  step_sizes = (float('inf'), float('inf'))
  while i < DESCENT_CYCLES and np.abs(step_sizes[0]) >= LEARN_RATE and np.abs(step_sizes[1]) >= LEARN_RATE:
    step_sizes = min_F(guess[0], guess[1])
    # print(step_sizes)

    # Move guess towards the step size
    guess = (guess[0] + step_sizes[0], guess[1] + step_sizes[1])
    i += 1

  # Return final guess
  return guess

# Compute the initial min point
min_point = descend(INITIAL_GUESS)
prev_min_point = (0, 0)  # This is used to check if min_point has changed
min_value = F(min_point[0], min_point[1])  # Calculate the minimum value at the point

# "Sweep" and check the neighboring points
i = 0
while i < SWEEP_CYCLES and min_point != prev_min_point:
  prev_min_point = min_point
  # Round to nearest whole number to make it work with range
  for x in range(int(np.round(min_point[0] - RANGE)), int(np.round(min_point[0] + RANGE))):
    for y in range(int(np.round(min_point[1] - RANGE)), int(np.round(min_point[1] + RANGE))):
      # Update the guess
      guess = descend((x, y))

      # Replace the minimum point if minimum value is less
      if F(guess[0], guess[1]) < min_value:
        min_point = guess
        min_value = F(guess[0], guess[1])

  i += 1
```

Doing this resulted in the point `(0.8962922428272383, -0.14270553184258455)`, which is the global minimum:

<img width="974" alt="Math3D scene with the global minimum" src="https://github.com/brendan-ch/gradient-descent/assets/34608561/4c5ff29c-a2e2-4f1a-8b53-88792c4a7ff7">

[See full Math3D scene](https://www.math3d.org/2Y6t1kpA8)
