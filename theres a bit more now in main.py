#mostly pseucode
# import _____ 
#insert with the import the stuff from structural and thermal analysis
#if else statements regarding the imports of files
#else  
#  print out channel numbers with areas of conversion
#also run another if else for structural analysis conversion
#generate the plots with html for all of the data
#save to file


import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd
#import subplot - we need to create that 
#local import 
#stuff thats hard to understand pt.1
if instance():
  print("file available")
  #that was very bs-ed im so sorry
  #cea output and file idk what those mean at all??? like i dont understand what the variables do aaaaa
else:
  print("file is not available")
  file_name = input("enter name for file requested")
  #wait when was input created ;w;
  file_name = file_name + ".txt"
  #another round of cea output that i cant understand for the love of god im so sorry for anyone trying to clean this up prayers to you

#dimensions of the raceway will all of code around here
import structural_analysis
import thermal_analysis
import raceway_temps.xlsx

chanl_num = 0
print ("Channel Number: ", chanl_num)
#avgheight = horizontal displacement 
#surface_roughness = avgheight, avg roughness, and maxheight
print ("Surface Roughness:  ", surface_roughness)
#stuff thats hard to understand pt.2 :(

#weird thing with non convergence function thing
print("channels/stations did not converge")
print ("Channel Number:  ", chanl_num)
#lists/arrays in here idk how to interpert that with our own stuff

i = 0
radius_check = r_arr[i]
#WHEN DID THE r-arr LIST GET MADE WHAT
radius_new = r_arr[i + 1]
#ok lots of stuff get more complicated from here sdfsdfsf

#if boolean with stuff thats hard to understand pt. 3
#axes and phases 
phase_colors = {"liquid": "blue", "gas": "yellow", "super_crit_gas": "red"}

#plot code if someone wants to add some that stuff

# THERMAL ANALYSIS PLOTS ONLY BELOW

from thermal_analysis import get_raceway_temps  # ensure that this function is called at all
import seaborn as sns

df = get_raceway_temps() # Call the functionm to get Altitiude vs T1, T2 dataframe and store in df

# Scatterplot for Altitude vs T1
sns.set()
plt.figure(figsize=(12, 9))
plt.title('Altitude vs Outer Raceway Temperature (T1)')

sns.scatterplot(x=df['Altitude (m)'], y=df['Outer Wall Temp (T1, K)'],
                  size=df['Inner Wall Temp (T2, K)'], 
                  sizes=(60, 600),
                  hue=df['Inner Wall Temp (T2, K)'],
                  palette='Blues',
                  alpha=0.85,
                  edgecolor='none',
                  linewidth=0.3,
                  data=df)

  #Trend line 
x = df['Altitude (m)']
y = df['Outer Wall Temp (T1, K)']
w = np.polyfit(x,y,1)
z = np.poly1d(w)
plt.plot(x,z(x),'r--')

plt.show()

# Scatterplot for Altitude vs T2
sns.set()
plt.figure(figsize=(12, 9))
plt.title('Altitude vs Inner Raceway Temperature (T2)')

sns.scatterplot(x=df['Altitude (m)'], y=df['Inner Wall Temp (T2, K)'],
                  size=df['Outer Wall Temp (T1, K)'], 
                  sizes=(60, 600),
                  hue=df['Outer Wall Temp (T1, K)'],
                  palette='Blues',
                  alpha=0.85,
                  edgecolor='none',
                  linewidth=0.3,
                  data=df)

  #Trend line 
x = df['Altitude (m)']
y = df['Inner Wall Temp (T2, K)']
w = np.polyfit(x,y,1)
z = np.poly1d(w)
plt.plot(x,z(x),'r--')

plt.show()

#Heatmap (for correlation between all variables)
corr = df.select_dtypes('number').corr() # Select only numeric columns for correlation

sns.heatmap(corr, cmap='inferno',
            annot=True, #show correlation values
            fmt='.2f', # two decimal places
            vmin=-1, vmax=1, #correlation range
            center=0, #center heatmap to 0 so that negative correlations aren't overestimated
            square=True, #square cells
            cbar_kws={"shrink": 0.8}
            )
plt.title('Correlation Heatmap of Raceway Temperatures and Altitude')
plt.xticks(rotation=45, ha='right')
plt.yticks(rotation=0)
plt.tight_layout()
plt.show()

# Density plot for Altitude vs T1
plt.figure(figsize=(12, 9))
plt.title('Density Plot of Altitude vs Outer Raceway Temperature (T1)')

sns.kdeplot(data = df, x = 'Altitude (m)', y = 'Outer Wall Temp (T1, K)',cmap='RdBu_r', fill=True, alpha=0.75)
plt.show()

# Density plot for Altitude vs T2
plt.figure(figsize=(12, 9))
plt.title('Density Plot of Altitude vs Inner Raceway Temperature (T2)')

sns.kdeplot(data = df, x = 'Altitude (m)', y = 'Inner Wall Temp (T2, K)',cmap='RdBu_r', fill=True, alpha=0.75)
plt.show()

#^ anybody who has worked on plots i really do reccomend that yall work on this part specifically
#make them for: heatmap, axial positions to ____ (ref the og code), nozzle contour, 
#idk how to explain literally the last 200 lines of code SJNDFDFDFJNF


