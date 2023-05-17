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

# How it works



# Notes

## Exercise 1

In this exercise, the gradient of F is stored in the code.

With `LEARN_RATE` set to `0.00001`, the final guess ends with something close to `(-0.8962922428213529, 0.14270553189951954)`. Plotted on a graph:

<img width="1024" alt="Math3D scene with given function and point" src="https://github.com/brendan-ch/gradient-descent/assets/34608561/db12af79-8ccd-4408-962f-2fb9de4c7f05">

[See full Math3D scene](https://www.math3d.org/qrkeSXBDy)

## Exercise 2

Same as exercise 1, but approximates the gradient of F using a difference quotient. Original function F is stored in the code.

With `LEARN_RATE` and `H` both set to `0.00001`, the final guess ends with something close to `(-0.8962922428272383, 0.14270553184258455)`.
