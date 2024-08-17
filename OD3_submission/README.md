# Orbital Determination 3 (OD 3)
Third submission on the progress to my final OD code for the Near Earth Asteroid. Adds to [odlib.py](https://github.com/diipakshii/SSP/blob/main/OD2_submission/odlib.py) from OD2.

## Table of Contents
- Pal_OD3.py
- Pal_input.txt
- odlib.py

## Section Breakdown
### [Pal_OD3.py](https://github.com/diipakshii/SSP/blob/main/OD3_submission/Pal_OD3.py)
This script that uses the odlib module to compute and print various results.

#### Requirements:
- Python 3.x
- odlib.py (installed or available in the same directory as your script)

### [Pal_input.txt](https://github.com/diipakshii/SSP/blob/main/OD3_submission/Pal_input.txt)
This file contains input data used in OD calculations. 

- Lines 1-6: Positional and velocity components (x, y, z, vx, vy, vz) in kilometers and kilometers per second.
- Lines 7-12: Actual values for orbital parameters (eccentricity, inclination, longitude of ascending node, argument of perihelion, mean anomaly, true anomaly, and semi-major axis).
- Line 13: Semi-major Axis (a) in Astronomical Units (AU)
- Line 14: Time of Last Perihelion Passage (T) in Julian Date (JD)

### [odlib.py](https://github.com/diipakshii/SSP/blob/main/OD3_submission/odlib.py)
The script calculates and prints various orbital parameters and elements for a celestial object using positional and velocity data from a file. The calculations include angular momentum, orbital elements, mean anomaly, and the time of last perihelion passage.
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
