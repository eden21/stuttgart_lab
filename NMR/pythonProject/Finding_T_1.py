import numpy as np
import pandas as pd
import scipy.optimize as sc
import scipy.signal
import matplotlib.pyplot as plt


def exp_model(t,A,T1,B):
    return A*np.exp(-t/T1)+B

path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\water_glycerine\\100_glycerine\FID\\20250422-0003.txt'
data=pd.read_csv(path, delimiter='\t')
data.replace('∞', np.inf, inplace=True)
data=data[1:]
data = data.astype(float)


low_lim=0.05
high_lim=0.5
relevant_data = data[(data['Time'] >= low_lim) & (data['Time'] <= high_lim)]
p0=np.array([1,2,3])
popt, pcov = sc.curve_fit(exp_model, relevant_data['Time'], relevant_data['Channel A'],p0=p0,maxfev=5000)
print(popt)
t=np.linspace(low_lim,high_lim,100)
y_fit=exp_model(t,popt[0],popt[1],popt[2])

saved_data=pd.DataFrame({"time":t,"y_fit":y_fit})
saved_data.to_csv(path+"_fit.csv")
saved_popt=pd.Series(popt)
saved_popt.to_csv(path+"_fit_popt.csv")
fig,ax=plt.subplots(1,1)
ax.plot(data['Time'],data['Channel A'],label='all data')
ax.plot(relevant_data['Time'],relevant_data['Channel A'],label='fit region')
ax.plot(t,y_fit,label='fit')


ax.grid()
ax.legend()
ax.set_xlabel('Time[msec]')
ax.set_ylabel('Voltage[V]')
plt.show()