import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def exp_model(t,A,T1,B):
    return A*np.exp(-t/T1)+B

t=np.linspace(0,75,100)
fig,ax=plt.subplots(1,1)
path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\multi_pulses\\meiboom_gill\\20250415-0012.txt_fit_popt.csv'
popt=pd.read_csv(path)
y_fit=exp_model(t,popt.iloc[0,1],popt.iloc[1,1],popt.iloc[2,1])
min=np.min(y_fit)
ax.plot(t,y_fit-min,label="Heavy mineral oil")


path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\water_glycerine\\10_glycerine_90_water\\MG\\20250422-0003.txt_fit_popt.csv'
popt=pd.read_csv(path)
y_fit=exp_model(t,popt.iloc[0,1],popt.iloc[1,1],popt.iloc[2,1])
min=np.min(y_fit)
ax.plot(t,y_fit-min,label="10% glycerine 90% water")


path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\water_glycerine\\20_glycerine_80_water\\MG\\20250422-0003.txt_fit_popt.csv'
popt=pd.read_csv(path)
y_fit=exp_model(t,popt.iloc[0,1],popt.iloc[1,1],popt.iloc[2,1])
min=np.min(y_fit)
ax.plot(t,y_fit-min,label="20% glycerine 80% water")


path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\water_glycerine\\50_water_50_glycerine\\MG\\20250422-0003.txt_fit_popt.csv'
popt=pd.read_csv(path)
y_fit=exp_model(t,popt.iloc[0,1],popt.iloc[1,1],popt.iloc[2,1])
min=np.min(y_fit)
ax.plot(t,y_fit-min,label="50% glycerine 50% water")


path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\water_glycerine\\100_glycerine\\MG\\20250422-0003.txt_fit_popt.csv'
popt=pd.read_csv(path)
y_fit=exp_model(t,popt.iloc[0,1],popt.iloc[1,1],popt.iloc[2,1])
min=np.min(y_fit)
ax.plot(t,y_fit-min,label="100% glycerine")

ax.grid()
ax.legend()
ax.set_xlabel('Time[msec]')
ax.set_ylabel('Voltage[V]')
plt.show()