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

#Constants 

k_s = 205     #thermal conductivity of Al 6063-T6 (material used to make tank)
k_cf = 10     #thermal conductivity of carbon fiber (in W/m*K)
L_t = 0.0037592    #Thickness of tank (m)
L_rt = 0.03 + L_t  #Distance from raceway to tank shell (m)
h = 300 #heat transfer coefficient (in W/m^2*K)
L_r = 0.04  #Height of Raceway (m) - SUBJECT TO CHANGE
A_1 = 0.1  #Cross-sectional area of raceway (m^2) - SUBJECT TO CHANGE
A_2 = 0.032 #Cross-sectional area of rocket (m^2) 
Tt = 94 #Temp of Rocket Tank (in K)
R_conv = 1/h*A_1  #Resistance between Te and T1 
R_cond = (L_rt/(k_s*A_2) + L_r/(k_cf*A_1)) #Equivalent resistance between T1 and Tt (conduction region)
    
#Defining a function to compute the air temperature at varying altitudes
def Alt2Temp(h):  #h (altitude) is in meters
    Te_C = 15.04 - 0.00649*h #Temp in C
    Te = Te_C + 273.15  #Kelvin Conversion
    return Te
    
#Defining main function to compute the raceway temperatures at a given altitude (only integers between 1 and 11001)
def get_raceway_temps():
    for i in range(1, 10):
        Te = Alt2Temp(i)
        
# Finding T1 (temperature at the side of the raceway hitting the air)
        T1 = (Te*R_cond + Tt*R_conv)/(R_conv + R_cond)
# In this case, we assume Te is the outside air temp and T1 is the exterior of the raceway 

# Modified q_cond considering the rocket isn't at the start (using )
        q_cond = (T1 - Tt)/R_cond

# Finding T2 (temperature at the side of the raceway touching the rocket wall)
        T2 = T1 - (q_cond*L_r)/(k_cf*A_1)

        print("Outer Wall of Raceway:", T1, "Kelvin at altitude i=", i)
        print("Inner Wall of Raceway:", T2, "Kelvin at altitude i=", i)

get_raceway_temps()
