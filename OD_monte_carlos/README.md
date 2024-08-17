# Orbital Determination Monte Carlos (OD Monte Carlos)

## Table of Contents
- MoGtestinput_TestCode2.txt
- ODmontecarlos.py
- monte_carlo.py

## Section Breakdown
### [MoGtestinput_TestCode2.txt](https://github.com/diipakshii/SSP/blob/main/OD_monte_carlos/MoGtestinput_TestCode2.txt)
This file contains the input for ODmontecarlos.py. Contains the observational data for Near Earth Asteroid 2015 HH10.

Each observation is given as follows: 

Observation Timestamp (Julian Date): The Julian Date at which the observation was made.

Right Ascension (RA): The right ascension of the object in degrees.

Declination (Dec): The declination of the object in degrees.

Earth-Sun Vector (x, y, z): The position vectors of Earth relative to the Sun in AU (Astronomical Units).

### [ODmontecarlos.py](https://github.com/diipakshii/SSP/blob/main/OD_monte_carlos/ODmontecarlos.py)
This script performs a Monte Carlo simulation to estimate orbital elements by perturbing right ascension (RA) and declination (Dec) values with uncertainties, computing orbital parameters, and comparing the results with actual values to evaluate mean, standard deviation, standard error of the mean, and percentage error for each orbital element.
- ODmontecarlos(): performs a Monte Carlo simulation to estimate the orbital elements of a celestial object based on perturbed observational data

#### Requirements:
- Python 3.x
- math module (standard library)
- numpy library
  
Install required package:
```
pip install numpy
```

### [monte_carlo.py](https://github.com/diipakshii/SSP/blob/main/OD_monte_carlos/monte_carlo.py)
This script performs a Monte Carlo simulation to estimate the value of π. 
- montecarlo(): Performs a monte carlo simulation by randomly generating points within a unit square and calculating the ratio of points within a unit circle, returning the mean estimate, standard deviation, standard error of the mean, and error percentage.

#### Requirements:
- Python 3.x
- math module (standard library)
- numpy library
- matplotlib library
  
Install required package:
```
pip install numpy
```
```
pip install matplotlib
```
