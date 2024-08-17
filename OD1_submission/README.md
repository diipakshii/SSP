# Orbital Determination 1 (OD 1)
First submission on the progress to my final OD code for the Near Earth Asteroid.

## Table of Contents
- Pal_OD1.py
- Pal_input.txt
- odlib.py
- quadrant_finding_function.py

## Section Breakdown
### [Pal_OD1.py](https://github.com/diipakshii/SSP/blob/main/OD1_submission/Pal_OD1.py)
This script utilizes the odlib module to calculate and print angular momentum.

#### Requirements:
- Python 3.x
- odlib.py (installed or available in the same directory as your script)

### [Pal_input.txt](https://github.com/diipakshii/SSP/blob/main/OD1_submission/Pal_input.txt)
 Input file containing the positional and velocity components for odlib.py. 

### [odlib.py](https://github.com/diipakshii/SSP/blob/main/OD1_submission/odlib.py)
This script provides functions for basic arithmetic, trigonometric calculations, and the computation of angular momentum using celestial mechanics principles.
- add(a, b): takes two arguments, a and b, and returns their sum
- trig_function(cosine, sine): determines the angle (in degrees) based on given cosine and sine values
- ang_momentum(): calculates the angular momentum vector based on positional and velocity data provided in a file named Pal_input.txt'.

#### Requirements:
- Python 3.x
- math module (standard library)
- numpy library
  
Install required package
```
pip install numpy
```

### [quadrant_finding_function.py](https://github.com/diipakshii/SSP/blob/main/OD1_submission/quadrant_finding_function.py)
This script uses the trig_function to calculate angles based on cosine and sine values.
