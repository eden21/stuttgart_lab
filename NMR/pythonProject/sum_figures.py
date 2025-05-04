import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def exp_model(t,A,T1,B):
    return A*np.exp(-t/T1)+B

t=np.linspace(0,1,100)
fig,ax=plt.subplots(1,1)
path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\FID_mineral_oil\\heavy_mineral_oil\\scope.txt_fit_popt.csv'
popt=pd.read_csv(path)
y_fit=exp_model(t,popt.iloc[0,1],popt.iloc[1,1],popt.iloc[2,1])
ax.plot(t,y_fit,label="Heavy mineral oil")
path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\FID_mineral_oil\\light_mineral_oil\\scope.txt_fit_popt.csv'
popt=pd.read_csv(path)
y_fit=exp_model(t,popt.iloc[0,1],popt.iloc[1,1],popt.iloc[2,1])
ax.plot(t,y_fit,label="Light mineral oil")


ax.grid()
ax.legend()
ax.set_xlabel('Time[msec]')
ax.set_ylabel('Voltage[V]')
plt.show()