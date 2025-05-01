import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

d=np.array([4.000000,4.000349,4.001304,4.004402,4.006291,4.009008,4.011556,4.013564,4.013564])
E=np.array([-12622.742427734975,-12622.742427734982,-12622.742469385119,-12622.74253910218,-12622.742676741611,-12622.74273765984,-12622.742814292258,-12622.742883843233,-12622.742936837436])
d1=np.array([4.000000,3.999850,3.999486,3.998974])
E1=np.array([-12623.457407743479,-12623.457503144986,-12623.45760930948,-12623.457666994997])
fig,(ax1,ax2)=plt.subplots(1,2,figsize=(12,6))
ax1.plot(d,E,'-o')
#ax.plot(d1,E1,label='DFT+bj')
ax1.set_xlabel(r"d[$\AA$]")
ax1.set_ylabel(r'E[eV]')
ax1.set_title(r"Energy Vs. distance of the dimer in DFT")
ax1.grid()
ax2.plot(d1,E1,'-o')
ax2.set_xlabel(r"d[$\AA$]")
ax2.set_ylabel(r'E[eV]')
ax2.set_title(r"Energy Vs. distance of the dimer in DFT+bj")
ax2.grid()
plt.tight_layout()
plt.show()
