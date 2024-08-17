# Orbital Determination Method of Gauss (OD MoG)

## Table of Contents
- FinalODCode_TestCode2.py
- MoG_testinput_TestCode2.txt
- f_and_g_functions.py
- odlib_TestCode2.py

## Section Breakdown

### FinalODCode_TestCode2.py

### MoG_testinput_TestCode2.txt

### [f_and_g_functions.py](https://github.com/diipakshii/SSP/blob/main/OD_MoG_submission/f_and_g_functions.py)
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

### odlib_TestCode2.py
