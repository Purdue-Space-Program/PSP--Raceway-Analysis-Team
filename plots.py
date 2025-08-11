import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
import pandas as pd

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