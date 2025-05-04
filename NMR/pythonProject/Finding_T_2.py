import numpy as np
import pandas as pd
import scipy.optimize as sc
import scipy.signal as signal
import matplotlib.pyplot as plt
#from scipy.interpolate import UnivariateSpline
from scipy.fft import fft, ifft, fftfreq

def exp_model(t,A,T2,B):
    return A*np.exp(-t/T2)+B

path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\distilled_water\\MG\\20250422-0003.txt'
data=pd.read_csv(path, delimiter='\t')
data.replace('∞', np.inf, inplace=True)
data.replace('-∞', -np.inf, inplace=True)
data.replace([np.inf, -np.inf], np.nan, inplace=True)
data=data[1:]
data = data.astype(float)
data['Time'] = pd.to_numeric(data['Time'], errors='coerce')
data['Channel A'] = pd.to_numeric(data['Channel A'], errors='coerce')
# Drop rows again if coercion caused NaNs
data = data.dropna()
Time=data['Time'].to_numpy()
Voltage=data['Channel A'].to_numpy()
y=fft(Voltage)
freq=fftfreq(len(Time), d=(Time[1] - Time[0]))

# Filter: zero out high frequencies
threshold = 30  # remove everything above 20 Hz
Y_filtered = y.copy()
Y_filtered[np.abs(freq) > threshold] = 0

# Inverse FFT
y_filtered = np.real(ifft(Y_filtered))


peaks, properties = signal.find_peaks(y_filtered, height=1,width=500)
p0=np.array([1,2,3])
popt, pcov = sc.curve_fit(exp_model, Time[peaks], y_filtered[peaks],p0=p0,maxfev=5000)
print(popt)
t=np.linspace(Time[peaks[0]],Time[peaks[-1]],100)
y_fit=exp_model(t,popt[0],popt[1],popt[2])

saved_popt=pd.Series(popt)
saved_popt.to_csv(path+"_fit_popt.csv")

fig,ax=plt.subplots(1,1)
ax.plot(Time,y_filtered,label='FFT filtered data')
ax.plot(Time[peaks],y_filtered[peaks],'o',label='peaks')
ax.plot(t,y_fit,label='fit')

ax.grid()
#ax.legend()
ax.set_xlabel('Time[msec]')
ax.set_ylabel('Voltage[V]')

plt.show()