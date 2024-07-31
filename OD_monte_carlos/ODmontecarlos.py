import numpy as np
from math import *
from FinalODCode_TestCode2 import odcode

# inputs

# time observations in Julian dates
x = open("MoGtestinput_TestCode2.txt")
components = x.readlines()
time1 = float(components[1])
time2 = float(components[9])
time3 = float(components[17])

# RA and Dec from Observations
RA1_deg = float(components[2])
Dec1_deg = float(components[3])

RA2_deg = float(components[10])
Dec2_deg = float(components[11])

RA3_deg = float(components[18])
Dec3_deg = float(components[19])

# Earth-Sun vectors in equatorial coordinates (x,y,z)

R1 = np.array([float(components[4]), float(components[5]), float(components[6])])
R2 = np.array([float(components[12]), float(components[13]), float(components[14])])
R3 = np.array([float(components[20]), float(components[21]), float(components[22])])

# actual values

act_a = float(components[25])
act_e = float(components[26]) 
act_i = float(components[27])
act_O = float(components[28])
act_w = float(components[29])
act_M = float(components[30])

# monte carlos function

def ODmontecarlos():
    RA_uncertainty = .001
    Dec_uncertainty = .001
    iterations = 50000 # change later

    montecarlovalues = np.zeros((iterations, 6))

    RA1 = np.random.normal(RA1_deg, RA_uncertainty)
    Dec1 = np.random.normal(Dec1_deg, Dec_uncertainty)
    RA2 = np.random.normal(RA2_deg, RA_uncertainty)
    Dec2 = np.random.normal(Dec2_deg, Dec_uncertainty)
    RA3 = np.random.normal(RA3_deg, RA_uncertainty)
    Dec3 = np.random.normal(Dec3_deg, Dec_uncertainty)

    for j in range(iterations): 
        orbitalelements = odcode(time1, time2, time3, RA1, Dec1, RA2, Dec2, RA3, Dec3, R1, R2, R3)
        montecarlovalues[j] = orbitalelements

    mean_a = np.mean(montecarlovalues[:,0])
    SD_a = np.std(montecarlovalues[:,0])
    SDOM_a = SD_a/sqrt(iterations)
    error_a = (abs(mean_a - act_a) / act_a) * 100

    mean_e = np.mean(montecarlovalues[:,1])
    SD_e = np.std(montecarlovalues[:,1])
    SDOM_e = SD_e/sqrt(iterations)
    error_e = (abs(mean_e - act_e) / act_e) * 100

    mean_i = np.mean(montecarlovalues[:,2])
    SD_i = np.std(montecarlovalues[:,2])
    SDOM_i = SD_i/sqrt(iterations)
    error_i = (abs(mean_i - act_i) / act_a) * 100

    mean_O = np.mean(montecarlovalues[:,3])
    SD_O = np.std(montecarlovalues[:,3])
    SDOM_O = SD_O/sqrt(iterations)
    error_O = (abs(mean_O - act_O) / act_O) * 100

    mean_w = np.mean(montecarlovalues[:,4])
    SD_w = np.std(montecarlovalues[:,4])
    SDOM_w = SD_w/sqrt(iterations)
    error_w = (abs(mean_w - act_w) / act_w) * 100

    mean_MA = np.mean(montecarlovalues[:,5])
    SD_MA = np.std(montecarlovalues[:,5])
    SDOM_MA = SD_MA/sqrt(iterations)
    error_MA = (abs(mean_MA - act_M) / act_M) * 100

    print("Semi-major Axis //", "Mean:", mean_a, "/", "Standard Deviation:", SD_a, "/", "Standard Deviation of Mean:", SDOM_a, "/", "Error:", error_a, "%")
    print("Eccentricity //", "Mean:", mean_e, "/", "Standard Deviation:", SD_e, "/", "Standard Deviation of Mean:",  SDOM_e, "/", "Error:", error_e, "%")
    print("Inclination //", "Mean:", mean_i, "/", "Standard Deviation:", SD_i, "/", "Standard Deviation of Mean:", SDOM_i, "/", "Error:", error_i, "%")
    print("Longitude of Ascending Node //", 'Mean:', mean_O,  "/", "Standard Deviation:", SD_O, "/", "Standard Deviation of Mean:", SDOM_O, "/", "Error:", error_a, "%")
    print("Argument of Perihelion //", "Mean:", mean_w,  "/", "Standard Deviation:", SD_w, "/", "Standard Deviation of Mean:", SDOM_w, "/", "Error:", error_w, "%")
    print("Mean Anamoly //", "Mean:", mean_MA, "/", "Standard Deviation:", SD_MA, "/", "Standard Deviation of Mean:", SDOM_MA, "/", "Error:", error_MA, "%")

ODmontecarlos()