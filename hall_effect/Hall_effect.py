import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
from scipy import stats, optimize
from scipy.optimize import curve_fit
from sklearn.linear_model import LinearRegression
import math


dataB50 = pd.read_csv('B50mT.txt', sep=" ", header = None)
dataB100 = pd.read_csv('B100mT.txt', sep=" ", header = None)
dataB200 = pd.read_csv('B200mT.txt', sep=" ", header = None)
d = 0.001
l = 0.02 #y0
w = 0.01 

plt.scatter(dataB50[0],dataB50[1]*1000, label='B = 50 mT')
plt.scatter(dataB100[0],dataB100[1]*1000,label= 'B = 100 mT')
plt.scatter(dataB200[0],dataB200[1]*1000, label='B = 200 mT')
plt.legend()

model50 = stats.linregress(dataB50[0], dataB50[1]*1000)
print(f"slope: {model50.slope}" f"+/- {model50.stderr}")
model100 = stats.linregress(dataB100[0],dataB100[1]*1000)
print(f"slope: {model100.slope}" f"+/- {model100.stderr}")
model200 = stats.linregress(dataB200[0],dataB200[1]*1000)
print(f"slope: {model200.slope}" f"+/- {model200.stderr}")

#print('ps=',0.05/(model50.slope*d*1.602*10**(-19)))
#print('ps=',0.1/(model100.slope*d*1.602*10**(-19)))
#print('ps=',0.2/(model200.slope*d*1.602*10**(-19)))

#print(50(model50.slope*d/0.01)
#print(model100.slope*d/0.02)
#print(model200.slope*d/0.03)

plt.plot(dataB50[0], model50.intercept + model50.slope*dataB50[0])
plt.plot(dataB100[0],model100.intercept + model100.slope*dataB100[0])
plt.plot(dataB200[0],model200.intercept + model200.slope*dataB200[0])
plt.ylabel('$U_H$ [mV]')
plt.xlabel('I [mA]')
plt.show()

#VOLTAGE VS MAGNETIC FIELD
I10 = pd.read_csv('I10mA.txt', sep=" ", header = None)
I20 = pd.read_csv('I20mA.txt', sep=" ", header = None)
I30 = pd.read_csv('I30mA.txt', sep=" ", header = None)

plt.scatter(I10[0],I10[1]*1000, label='I = 10 mA')
plt.scatter(I20[0],I20[1]*1000, label='I = 20 mA')
plt.scatter(I30[0],I30[1]*1000, label='I = 30 mA')
plt.legend ()

model10 = stats.linregress(I10[0],I10[1]*1000)
print(f"slope: {model10.slope}" f"+/- {model10.stderr}")
model20 = stats.linregress(I20[0],I20[1]*1000)
print(f"slope: {model20.slope}" f"+/- {model20.stderr}")
model30 = stats.linregress(I30[0],I30[1]*1000)
print(f"slope: {model30.slope}" f"+/- {model30.stderr}")

print(model10.slope*d/0.01)
print(model20.slope*d/0.02)
print(model30.slope*d/0.03)

print('ps=',1/((model10.slope*d/0.01)*(1.602*10**(-19))))
print('ps=',1/((model20.slope*d/0.02)*(1.602*10**(-19))))
print('ps=',1/((model30.slope*d/0.03)*(1.602*10**(-19))))

print('v=',model10.slope/w)
print('v=',model20.slope/w)
print('v=',model30.slope/w)

print('mob=',(model10.slope/w)*l/1.5)
print('mob=',(model20.slope/w)*l/1.5)
print('mob=',(model30.slope/w)*l/1.5)


plt.plot(I10[0],model10.intercept + model10.slope*I10[0])
plt.plot(I20[0],model20.intercept + model20.slope*I20[0])
plt.plot(I30[0],model30.intercept + model30.slope*I30[0])
plt.ylabel('$U_H$ [mV]')
plt.xlabel('B [mT]')
plt.show()

#BANDGAP UNDOPED GERMANIUM
UnGe = pd.read_csv('Section5_NoB_2mA_undopped.csv')
UnGe["Temperature [K]"] = (UnGe["Voltage U_A1 / V"] * 100) + 273.15

# UnGe.plot.scatter(x="Temperature [K]", y="Voltage U_B1 / V")
# plt.xlabel('T [K]')
# plt.ylabel('$U_{B1}$ [V]')
# plt.show()

UnGe["1/T [1/K]"] = 1/UnGe["Temperature [K]"]
UnGe["log $\sigma$"] = np.log(l*0.002/(w*d*UnGe["Voltage U_B1 / V"]))
#UnGe.plot.scatter(x="1/T [1/K]", y="log $\sigma$")

modelUnGe = stats.linregress(UnGe["1/T [1/K]"], UnGe["log $\sigma$"])
# print(f"slope: {modelUnGe.slope}" f"+/- {modelUnGe.stderr}")
# print('Eg=', -modelUnGe.slope*2*1.3807*10**(-23))
# plt.plot(UnGe["1/T [1/K]"],modelUnGe.intercept + modelUnGe.slope*UnGe["1/T [1/K]"], "-r", label='log $\sigma=E_g / 2K_B T$')
# plt.legend ()
# plt.show()

#BANDGAP P-DOPED GERMANIUM
pGe = pd.read_csv('Section_4_no_magnetic_field_I30mA.csv')
pGe["Temperature"] = (pGe["Voltage U_A1 / V"] * 100) + 273.15
# pGe.plot.scatter(x="Temperature", y="Voltage U_B1 / V")
# plt.xlabel('T [K]')
# plt.ylabel('$U_{B1}$ [V]')
# plt.show()

above370 = pGe[pGe["Temperature"] > 360.00]
#print(above370)
above370["1/T [1/K]"] = 1/ above370["Temperature"]
above370["log $\sigma$"] = np.log(l*0.03/(w*d*above370["Voltage U_B1 / V"]))
#above370.plot.scatter(x="1/T [1/K]", y="log $\sigma$")

modelpGe = stats.linregress(above370["1/T [1/K]"], above370["log $\sigma$"])
# print(f"slope: {modelpGe.slope}" f"+/- {modelpGe.stderr}")
# print('Eg=', modelpGe.slope*2*1.3807*10**(-23))
# plt.plot(above370["1/T [1/K]"],modelpGe.intercept + modelpGe.slope*above370["1/T [1/K]"], "-r", label='log $\sigma=E_g / 2K_B T$')
# plt.legend ()
# plt.show()

#VH vs Temperature
def func(x, a, b):
        e = 1.602*10**(-19)
        B = 0.2 
        I = 30
        y0 = 0.01
        ps = 9.1690*10**(20) 
        kb = 8.61733*10**-5
        Eg = 0.6506
        #return ((1-b)/(ps + ((np.sqrt(ps**(2)/4 + a*np.exp(-Eg/(kb*x))) - ps/2)*(1+b))))
        return ((I*B/y0)*(ps + ((np.sqrt(ps**(2)/4 + a**(2)*np.exp(-Eg/(kb*x))) - ps/2)*(1-b**2)))/
                (ps + (np.sqrt(ps**(2)/4 + a**(2)*np.exp(-Eg/(kb*x))) - ps/2)*(1+b)))#*(1/(e))

#        return ((1-b)/(ps + (np.sqrt(ps**(2)/4 + a*np.exp(-Eg/(k*x))) - ps/2)*(1+b)))*(I*B/(y0*e))        

#        return ((ps + (np.sqrt(ps**(2)/4 + a*np.exp(-Eg/(kb*x))) - ps/2)*(1-b**2))/
#                ((ps + (np.sqrt(ps**(2)/4 + a*np.exp(-Eg/(kb*x))) - ps/2)*(1+b))**2))*(I*B/(y0*e))
    
e = 1.602*10**(-19)
B = 0.2
I = 0.03
y0 = 0.01
ps = 9.1690*10**(20) 
kb = 8.61733*10**-5
Eg = 0.6506 #1.130816*10**(-19)

Hall_T = pd.read_csv('Section3_B200mT_I30mA.csv')
Hall_T["Temperature"] = (Hall_T["Voltage U_A1 / V"] * 100) + 273.15
Hall_T["V mV"] = Hall_T["Voltage U_B1 / V"] * 1000
Hall_T1 = Hall_T[Hall_T["Time t / s"] < 287.4] #Temperature before t=287.4
Hall_T1.plot.scatter(x="Temperature", y="V mV")
Hall_T2 = Hall_T1[Hall_T1["Temperature"] > 360.0]
guess = np.array([1*10**26 , 2])
guess = guess.astype(float)
popt, pcov = curve_fit(func,Hall_T2["Temperature"] , Hall_T2["V mV"], guess)
a,b = popt
print('a=',a,'b=',b)
print (np.sqrt(np.diag(pcov)))

#Hall_T1["y"] = ((ps + ((np.sqrt(ps**(2)/4 + 1.99*10**(26)*np.exp(-Eg*13025.9/(Hall_T1["Temperature"]))) - ps/2)*(1-1.81**2)))/
#     (((ps + (np.sqrt(ps**(2)/4 + 1.99*10**(26)*np.exp(-Eg*13025.9/(Hall_T1["Temperature"]))) - ps/2)*(1+1.81))**2 )*7.49*10**22)) 

plt.plot(Hall_T2["Temperature"], func(Hall_T2["Temperature"],a,b), 'r-')
#plt.plot(Hall_T1["Temperature"], Hall_T1["y"])
plt.xlabel('T [K]')
#plt.ylim(-0.01,0.01)
plt.ylabel('$U_{H}$ [mV]')
plt.figure()