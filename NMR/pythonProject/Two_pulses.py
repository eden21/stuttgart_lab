import numpy as np
import pandas as pd
import scipy.optimize as sc
import scipy.signal as signal
import matplotlib.pyplot as plt
#from scipy.interpolate import UnivariateSpline
from scipy.fft import fft, ifft, fftfreq

def exp_model(t,A,T2):
    return A*np.exp(-t/T2)

path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\2_pulse\\20250415-0003.txt'
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
y_filtered=y_filtered-y_filtered[1]

peaks, properties = signal.find_peaks(y_filtered, height=1,width=1600)

# Two data points
x1, y1 = Time[peaks[0]], y_filtered[peaks[0]]
x2, y2 = Time[peaks[1]], y_filtered[peaks[1]]

# Compute B
T2 = 1/(-np.log(y2 / y1) / (x2 - x1))

# Compute A
A = y1 / np.exp(-T2 * x1)

print(f"A = {A}, T2 = {T2}")
t=np.linspace(Time[peaks[0]],Time[peaks[-1]],100)
y_fit=exp_model(t,A,T2)
diff=y_fit[-1]-y_filtered[peaks[-1]]
y_fit=y_fit-diff

fig,ax=plt.subplots(1,1)
ax.plot(Time,y_filtered,label='FFT filtered data')
ax.plot(Time[peaks],y_filtered[peaks],'o',label='peaks')
ax.plot(t,y_fit,label='fit')

ax.grid()
#ax.legend()
ax.set_xlabel('Time[msec]')
ax.set_ylabel('Voltage[V]')

plt.show()