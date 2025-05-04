import numpy as np
import pandas as pd
import scipy.optimize as sc
import scipy.signal as signal
import matplotlib.pyplot as plt
#from scipy.interpolate import UnivariateSpline
from scipy.fft import fft, ifft, fftfreq

path='C:\\Users\\X1\\Documents\\MATLAB\\lab\\NMR\\Flourine_FC_70\\A_len_1.76_mu_s\\20250422-0003.txt'
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

fig,ax=plt.subplots(1,1)
ax.plot(freq,y,label="Light mineral oil")
ax.grid()
#ax.legend()
ax.set_xlabel('Time[msec]')
ax.set_ylabel('Voltage[V]')
plt.show()