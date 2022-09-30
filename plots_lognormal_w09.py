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



arr = np.loadtxt('data/OMGW09.dat')
krangedirac=[]
OMEGAdirac=[]
for row in arr:
	krangedirac.append(np.float(row[0]))
	OMEGAdirac.append(np.float(row[1])-1*2+np.log10(1.5))

arr = np.loadtxt('data/OMGW09der.dat')
krangediracder=[]
OMEGAdiracder=[]
for row in arr:
	krangediracder.append(np.float(row[0]))
	OMEGAdiracder.append(np.float(row[1]))


data = np.load('data/OmegaGW_of_k_LN_001_w_09_precise.npz')
lst=data.files
krange001nolog=data[lst[0]]
krange001=np.log10(data[lst[0]])
OMEGA001=np.log10(data[lst[1]])
OMEGA001interpol = UnivariateSpline(krange001, OMEGA001,s=0)
OMEGA001interpolder=OMEGA001interpol.derivative()
OMEGA001der=OMEGA001interpolder(krange001)

data = np.load('data/OmegaGW_of_k_LN_005_w_09_precise.npz')
lst=data.files
krange005nolog=data[lst[0]]
krange005=np.log10(data[lst[0]])
OMEGA005=np.log10(data[lst[1]])
OMEGA005interpol = UnivariateSpline(krange005, OMEGA005,s=0)
OMEGA005interpolder=OMEGA005interpol.derivative()
OMEGA005der=OMEGA005interpolder(krange005)

data = np.load('data/OmegaGW_of_k_LN_01_w_09_precise.npz')
lst=data.files
krange01nolog=data[lst[0]]
krange01=np.log10(data[lst[0]])
OMEGA01=np.log10(data[lst[1]])
OMEGA01interpol = UnivariateSpline(krange01, OMEGA01,s=0)
OMEGA01interpolder=OMEGA01interpol.derivative()
OMEGA01der=OMEGA01interpolder(krange01)

############
####################################
############

plt.plot(krange01,OMEGA01,lw=2,color="green",label="$\\Delta=0.1$")
plt.plot(krange005,OMEGA005,lw=2,color="red",label="$\\Delta=0.05$")
plt.plot(krange001,OMEGA001,lw=2,color="blue",label="$\\Delta=0.01$")
plt.plot(krangedirac,OMEGAdirac,lw=2,color="black",label="$\\delta$")



ax=plt.gca()

#ax.set_xscale('log')
#ax.set_yscale('log')


#Axes limit
xmin=-2
xmax=1
ymin=-4
ymax=2

plt.axis([xmin,xmax,ymin,ymax])



#Axes label
plt.xlabel('$\\log_{10}(k/k_p)$',fontsize=18)
plt.ylabel('$\\log_{10}\\Omega_{\\rm GW}(w=0.9)$',fontsize=18)

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

plt.savefig("plots/GW_spectrum_w_09.pdf", format='pdf',transparent=True)

plt.show()

plt.gcf().clear()




plt.plot(krange01nolog,OMEGA01der,lw=2,color="green",label="$\\Delta=0.1$")
plt.plot(krange005nolog,OMEGA005der,lw=2,color="red",label="$\\Delta=0.05$")
plt.plot(krange001nolog,OMEGA001der,lw=2,color="blue",label="$\\Delta=0.01$")
plt.plot(krangediracder,OMEGAdiracder,lw=2,color="black",label="$\\delta$")



ax=plt.gca()

#ax.set_xscale('log')
#ax.set_yscale('log')


#Axes limit
xmin=0.1
xmax=2
ymin=-10
ymax=200

plt.axis([xmin,xmax,ymin,ymax])



#Axes label
plt.xlabel('$k/k_p$',fontsize=18)
plt.ylabel('$d\\log\\Omega_{\\rm GW}(w=0.9)/d\\log k$',fontsize=18)

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

plt.savefig("plots/GW_spectrum_der_w_09.pdf", format='pdf',transparent=True)

plt.show()

plt.gcf().clear()


