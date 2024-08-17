# Orbital Determination 2 (OD 2)
Second submission on the progress to my final OD code for the Near Earth Asteroid. Adds to [odlib.py](https://github.com/diipakshii/SSP/blob/main/OD1_submission/odlib.py) from OD1.

## Table of Contents
- Pal_OD2.py
- Pal_input.txt
- odlib.py

## Section Breakdown
### [Pal_OD2.py](https://github.com/diipakshii/SSP/blob/main/OD2_submission/Pal_OD2.py)
This script uses the odlib module to calculate and print angular momentum and orbital elements.

#### Requirements: 
- Python 3.x
- odlib.py (installed or available in the same directory as your script)

### [Pal_input.txt](https://github.com/diipakshii/SSP/blob/main/OD2_submission/Pal_input.txt)
This file contains input data used in OD calculations. 
- Lines 1-6: Positional and velocity components (x, y, z, vx, vy, vz) in kilometers and kilometers per second.
- Lines 7-12: Actual values for orbital parameters (eccentricity, inclination, longitude of ascending node, argument of perihelion, mean anomaly, true anomaly, and semi-major axis).

### [odlib.py](https://github.com/diipakshii/SSP/blob/main/OD2_submission/odlib.py)
This script performs calculations related to trigonometry, angular momentum, and orbital elements for celestial objects. It reads input data from a file and calculates various orbital parameters.
- add(a, b): takes two arguments, a and b, and returns their sum
- trig_function(cosine, sine): determines the angle (in degrees) based on given cosine and sine values
- ang_momentum(): calculates the angular momentum vector based on positional and velocity data provided in a file named Pal_input.txt'.
- orbitalelements(): reads additional orbital parameters from Pal_input.txt and calculates key orbital elements including semi-major axis, eccentricity, inclination, longitude of ascending node, and argument of perihelion

#### Requirements:
- Python 3.x
- cmath, math, numpy modules (standard and external libraries)

Install required package
```
pip install numpy
```

  
