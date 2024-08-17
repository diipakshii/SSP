# Orbital Determination 4 (OD 4)
Fourth submission on the progress to my final OD code for the Near Earth Asteroid. 

## Table of Contents
- Newton_Raphson_Method.py
- f_and_g_functions.py

## Section Breakdown
### [Newton_Raphson_Method.py](https://github.com/diipakshii/SSP/blob/main/OD4_submission/Newton_Raphson_Method.py)
This script demonstrates two methods for finding the intersection of functions and solving equations:

Graphing: Provides a brief overview of the intersection of two functions.
Implementation of the Newton-Raphson Method: Uses an iterative method to find an approximate solution to a given equation.

#### Requirements:
- Python 3.x
- math module (standard library)

### [f_and_g_functions.py](https://github.com/diipakshii/SSP/blob/main/OD4_submission/f_and_g_functions.py)
This script provides an implementation of the fg function used in orbital mechanics. The fg function computes position and velocity functions (f and g) used for determining the state of a celestial body in orbit.
- fg(tau, r2, r2dot, flag): computes the functions f and g based on time parameter tau, position vector r2, velocity vector r2dot, and flag

#### Requirements:
- Python 3.x
- math module (standard library)
- numpy library
  
Install required package:
```
pip install numpy
```
