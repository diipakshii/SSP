# Orbital Determination Method of Gauss (OD MoG)

## Table of Contents
- FinalODCode_TestCode2.py
- MoG_testinput_TestCode2.txt
- f_and_g_functions.py
- odlib_TestCode2.py

## Section Breakdown

### [FinalODCode_TestCode2.py](https://github.com/diipakshii/SSP/blob/main/OD_MoG_submission/FinalODCode_TestCode2.py)
This script is performing orbit determination using observational data. It reads observational data from a file, processes it, and calculates the orbital parameters.
- fg(tau, r2, r2dot, n): Computes the f and g functions
- main(r2xyz_ec, r2dotxyz_ec): Computes the final orbital elements

#### Requirements:
- Python 3.x
- math module (standard library)
- numpy library
  
Install required package:
```
pip install numpy
```

### MoG_testinput_TestCode2.txt
This file contains the input for FinalODCode_TestCode2.py. Contains the observational data for Near Earth Asteroid 2015 HH10.

Each observation is given as follows:
Observation Timestamp (Julian Date): The Julian Date at which the observation was made.
Right Ascension (RA): The right ascension of the object in degrees.
Declination (Dec): The declination of the object in degrees.
Earth-Sun Vector (x, y, z): The position vectors of Earth relative to the Sun in AU (Astronomical Units).

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
This script determines the orbital elements of a celestial object using observational data. It calculates various orbital parameters such as the semi-major axis, eccentricity, inclination, longitude of ascending node, argument of perihelion, and mean anomaly. It also compares computed results with known orbital elements to evaluate the accuracy of the calculations.
- trig_function(cosine, sine): Finds the angle in degrees from cosine and sine values, adjusting for the quadrant based on the sine value.
- ang_momentum(pos_vec, vel_vec): Calculates the angular momentum vector given position and velocity vectors.
- axis(pos_vec, vel_vec): Calculates the semi-major axis of the orbit based on position and velocity vectors.
- eccen(pos_vec, vel_vec, h_scalar): Calculates the orbital eccentricity from position and velocity vectors and the angular momentum scalar.
- inclin(h): Calculates the orbital inclination from the angular momentum vector.
- long_a(h, h_scalar): Calculates the longitude of the ascending node from the angular momentum vector and scalar.
- arg_per(pos_vec, vel_vec, h, h_scalar): Calculates the argument of perihelion from position and velocity vectors and the angular momentum vector and scalar.
- meana(pos_vec, vel_vec, h_scalar): Calculates the mean anomaly from position and velocity vectors and the angular momentum scalar.
- time_per(pos_vec, vel_vec, h_scalar): Calculates the time of last perihelion passage based on the mean anomaly and semi-major axis.
- main(r2xyz_ec, r2dotxyz_ec): Main function that calculates and prints the orbital parameters and their errors by comparing computed results with expected values.
- newton_rap(): Calculates the eccentric anomaly using the Newton-Raphson method.
- ephermeris(): Computes the ephemeris of the celestial object by transforming orbital parameters to equatorial coordinates and calculates right ascension and declination.
- fg(tau, r2, r2dot, flag): Calculates the f and g functions used in orbit determination, with flags to specify the type of function.

#### Requirements:
- Python 3.x
- math module (standard library)
- numpy library
  
Install required package:
```
pip install numpy
```
