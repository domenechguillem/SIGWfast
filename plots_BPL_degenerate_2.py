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




data = np.load('data/OmegaGW_of_k_BPL_w1_nuv_32.npz')
lst=data.files
krange1nolog=data[lst[0]]
krange1=np.log10(data[lst[0]])
OMEGA1=np.log10(data[lst[1]])
OMEGA1interpol = UnivariateSpline(krange1, OMEGA1,s=0)
OMEGA1interpolder=OMEGA1interpol.derivative()
OMEGA1der=OMEGA1interpolder(krange1)


data = np.load('data/OmegaGW_of_k_BPL_w1_nIR_0_nuv_32.npz')
lst=data.files
krange001nolog=data[lst[0]]
krange001=np.log10(data[lst[0]])
OMEGA001=np.log10(data[lst[1]])
OMEGA001interpol = UnivariateSpline(krange001, OMEGA001,s=0)
OMEGA001interpolder=OMEGA001interpol.derivative()
OMEGA001der=OMEGA001interpolder(krange001)

data = np.load('data/OmegaGW_of_k_BPL_w1_nuv_3.npz')
lst=data.files
krange005nolog=data[lst[0]]
krange005=np.log10(data[lst[0]])
OMEGA005=np.log10(data[lst[1]])
OMEGA005interpol = UnivariateSpline(krange005, OMEGA005,s=0)
OMEGA005interpolder=OMEGA005interpol.derivative()
OMEGA005der=OMEGA005interpolder(krange005)

data = np.load('data/OmegaGW_of_k_BPL_w19_nuv_12.npz')
lst=data.files
krange01nolog=data[lst[0]]
krange01=np.log10(data[lst[0]])
OMEGA01=np.log10(data[lst[1]])
OMEGA01interpol = UnivariateSpline(krange01, OMEGA01,s=0)
OMEGA01interpolder=OMEGA01interpol.derivative()
OMEGA01der=OMEGA01interpolder(krange01)

data = np.load('data/OmegaGW_of_k_BPL_w19_nuv_1.npz')
lst=data.files
krange012nolog=data[lst[0]]
krange012=np.log10(data[lst[0]])
OMEGA012=np.log10(data[lst[1]])
OMEGA012interpol = UnivariateSpline(krange012, OMEGA012,s=0)
OMEGA012interpolder=OMEGA012interpol.derivative()
OMEGA012der=OMEGA012interpolder(krange01)

data = np.load('data/OmegaGW_of_k_BPL_w19_nuv_32.npz')
lst=data.files
krange013nolog=data[lst[0]]
krange013=np.log10(data[lst[0]])
OMEGA013=np.log10(data[lst[1]])
OMEGA013interpol = UnivariateSpline(krange013, OMEGA013,s=0)
OMEGA013interpolder=OMEGA013interpol.derivative()
OMEGA013der=OMEGA013interpolder(krange013)

data = np.load('data/OmegaGW_of_k_BPL_w19_nIR_1_nuv_12.npz')
lst=data.files
krange014nolog=data[lst[0]]
krange014=np.log10(data[lst[0]])
OMEGA014=np.log10(data[lst[1]])
OMEGA014interpol = UnivariateSpline(krange014, OMEGA014,s=0)
OMEGA014interpolder=OMEGA014interpol.derivative()
OMEGA014der=OMEGA014interpolder(krange014)


############
####################################
############

plt.plot(krange005,OMEGA005,lw=2,color="red",label="$w=1 (n_{UV}=3)$")
plt.plot(krange001,OMEGA001,lw=2,color="blue",label="$w=1 (n_{IR}=0)$")
plt.plot(krange1,OMEGA1,lw=2,color="orange",label="$w=1 (n_{UV}=3/2)$")
plt.plot(krange01,OMEGA01,lw=2,color="green",label="$w=1/9 (n_{UV}=1/2)$")
#plt.plot(krange012,OMEGA012,lw=2,color="purple",label="$w=1/9 (n_{UV}=1)$")
plt.plot(krange013,OMEGA013,lw=2,color="magenta",label="$w=1/9 (n_{UV}=3/2)$")
plt.plot(krange014,OMEGA014,lw=2,color="cyan",label="$w=1/9 (n_{IR}=1/2)$")


ax=plt.gca()

#ax.set_xscale('log')
#ax.set_yscale('log')


#Axes limit
xmin=-2
xmax=2
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

plt.savefig("plots/GW_spectrum_BPL_degenerate_2.pdf", format='pdf',transparent=True)

plt.show()

plt.gcf().clear()




plt.plot(krange005nolog,OMEGA005der,lw=2,color="red",label="$w=1 (n_{UV}=3)$")
plt.plot(krange001nolog,OMEGA001der,lw=2,color="blue",label="$w=1 (n_{IR}=0)$")
plt.plot(krange1nolog,OMEGA1der,lw=2,color="orange",label="$w=1 (n_{UV}=3/2)$")
plt.plot(krange01nolog,OMEGA01der,lw=2,color="green",label="$w=1/9 (n_{UV}=1/2)$")
#plt.plot(krange012nolog,OMEGA012der,lw=2,color="purple",label="$w=1/9 (n_{UV}=1)$")
plt.plot(krange013nolog,OMEGA013der,lw=2,color="magenta",label="$w=1/9 (n_{UV}=3/2)$")
plt.plot(krange014nolog,OMEGA014der,lw=2,color="cyan",label="$w=1/9 (n_{IR}=1)$")


ax=plt.gca()

ax.set_xscale('log')
#ax.set_yscale('log')


#Axes limit
xmin=0.01
xmax=100
ymin=-10
ymax=5

plt.axis([xmin,xmax,ymin,ymax])



#Axes label
plt.xlabel('$k/k_p$',fontsize=18)
plt.ylabel('$d\\log\\Omega_{\\rm GW}/d\\log k$',fontsize=18)

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

first_legend = plt.legend(loc=3,frameon=True,fontsize=16,ncol=1,handlelength=1)

plt.tight_layout()

plt.savefig("plots/GW_spectrum_der_BPL_degenerate_2.pdf", format='pdf',transparent=True)

plt.show()

plt.gcf().clear()


