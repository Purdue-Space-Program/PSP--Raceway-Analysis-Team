#For now we're assuming the setup is 1D (raceway has ~0 thickness)
import numpy as np
import matplotlib.pyplot as plt

#Returns temperature of the air based on altitude (in K)
def getOutsideTemp(altitude):
    return 294;

#https://purdue-space-program.atlassian.net/wiki/spaces/PL/pages/697139206/Copperhead+Vehicle+Parameters
#thermal conductivity of carbon fiber (in W/m*K)
k_cf = 10

#thermal conductivity of Al 6063-T6 (material used to make tank)
k_s = 205

#Thickness of tank (in m)
L_t = 0.0037592

#Height of raceway (in m)
L_r = 0.04 #just an estimate, SUBJECT TO CHANGE based on CAD

#Surface area of raceway (in m)
A = 0.1 #just an estimate, SUBJECT TO CHANGE based on CAD

#heat transfer coefficient (in W/m^2*K)
h = 300 #an estimate, SUBJECT TO CHANGE

#Height above sea level (in m), 187 meters is height of West Lafayette
alt = 187

#Temp of exterior raceway wall (facing outside)
#at the start, assume Te = Outside Air Temp
Te = getOutsideTemp(alt)

#Temp of Rocket Tank (in K)
Tt = 94

#10212
for x in range(1):
    R_cond = (L_t/k_s + L_r/k_cf)/A
    q_cond = (Te - Tt)/R_cond
    
    R_conv = 1/h*A
    q_conv = (abs(getOutsideTemp(alt) - Te))/R_conv
    
    print(q_cond)
    print(q_conv)