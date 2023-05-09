# coding: utf-8
import matplotlib
#matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import numpy as np
from matplotlib import cm
from scipy import optimize
import scipy.special as special
import scipy.integrate as integrate
from scipy.optimize import fsolve
import csv
from matplotlib import rc
from scipy.interpolate import UnivariateSpline

matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
plt.rcParams['font.family'] = 'serif'
rc('axes', linewidth=2)
#prop = fm.FontProperties(fname='system/anaconda2/lib/python2.7/site-packages/matplotlib/mpl-data/fonts/ttf/Palatino.ttf')

#import plot_defaults
#rc('font',**{'family':'serif','serif':['Palatino']})
#rc('text', usetex=True)




data = np.load('s_lognor_w_0_cs_1.npz')
lst=data.files
krange0nolog=data[lst[0]]
krange0=np.log10(data[lst[0]])
OMEGA0=np.log10(data[lst[1]])


data = np.load('s_lognor_w_1_cs_1.npz')
lst=data.files
krange1nolog=data[lst[0]]
krange1=np.log10(data[lst[0]])
OMEGA1=np.log10(data[lst[1]])

data = np.load('s_lognor_w_03_cs_1.npz')
lst=data.files
krange03nolog=data[lst[0]]
krange03=np.log10(data[lst[0]])
OMEGA03=np.log10(data[lst[1]])

data = np.load('s_lognor_w_05_cs_1.npz')
lst=data.files
krange05nolog=data[lst[0]]
krange05=np.log10(data[lst[0]])
OMEGA05=np.log10(data[lst[1]])

data = np.load('s_lognor_w_016_cs_1.npz')
lst=data.files
krange016nolog=data[lst[0]]
krange016=np.log10(data[lst[0]])
OMEGA016=np.log10(data[lst[1]])

data = np.load('s_lognor_w_m01_cs_1.npz')
lst=data.files
krangem01nolog=data[lst[0]]
krangem01=np.log10(data[lst[0]])
OMEGAm01=np.log10(data[lst[1]])


############
####################################
############

plt.plot(krange1,OMEGA1,lw=2,color="green",label="$w=1$")
plt.plot(krange05,OMEGA05,lw=2,color="red",label="$w=1/2$")
plt.plot(krange03,OMEGA03,lw=2,color="blue",label="$w=1/3$")
plt.plot(krange016,OMEGA016,lw=2,color="magenta",label="$w=1/6$")
plt.plot(krange0,OMEGA0,lw=2,color="black",label="$w=0$")
plt.plot(krangem01,OMEGAm01,lw=2,color="orange",label="$w=-1/9$")



ax=plt.gca()

#ax.set_xscale('log')
#ax.set_yscale('log')


#Axes limit
xmin=-3
xmax=np.log10(2.1)
ymin=-4
ymax=2

plt.axis([xmin,xmax,ymin,ymax])



#Axes label
plt.xlabel('$\\log_{10}(k/k_p)$',fontsize=18)
plt.ylabel('$\\log_{10}\\Omega_{\\rm GW}$',fontsize=18)

#ax.text(0.2, 0.25, '$0.2$', color='black', fontsize=18)
#ax.text(10**5, 10**(-2), '$k_{\\rm rh}/k_p=10^{-2}$', color='black', fontsize=18,
#        bbox=dict(facecolor='white', edgecolor='black', boxstyle='round',alpha=0.6))

#Ticks size
plt.xticks(fontsize=16)
plt.yticks(fontsize=16)
plt.minorticks_on()
ax.tick_params(axis = 'both',  direction="in",width=1,length=10 , which = 'major', labelsize = 16)
ax.tick_params(axis = 'both',  direction="in",width=1,length=5 , which = 'minor', labelsize = 16)

#More features
plt.grid(True,which="both",alpha=0.5)

# Legend

first_legend = plt.legend(loc=2,frameon=True,fontsize=16,ncol=2,handlelength=1)

plt.tight_layout()

plt.savefig("GW_spectrum_s_cs_1.pdf", format='pdf',transparent=True)

plt.show()

plt.gcf().clear()




