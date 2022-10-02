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


arr = np.loadtxt('data/OMGWb2_001.dat')
krangeb2001=[]
OMEGAb2001=[]
krangeb2001nolog=[]
for row in arr:
	krangeb2001.append(np.float(row[0]))
	OMEGAb2001.append(np.float(row[1]))
	krangeb2001nolog.append(10**np.float(row[0]))
OMEGAb2001interpol = UnivariateSpline(krangeb2001, OMEGAb2001,s=0)
OMEGAb2001interpolder=OMEGAb2001interpol.derivative()
OMEGAb2001der=OMEGAb2001interpolder(krangeb2001)

arr = np.loadtxt('data/OMGWb2_005.dat')
krangeb2005=[]
OMEGAb2005=[]
krangeb2005nolog=[]
for row in arr:
	krangeb2005.append(np.float(row[0]))
	OMEGAb2005.append(np.float(row[1]))
	krangeb2005nolog.append(10**np.float(row[0]))
OMEGAb2005interpol = UnivariateSpline(krangeb2005, OMEGAb2005,s=0)
OMEGAb2005interpolder=OMEGAb2005interpol.derivative()
OMEGAb2005der=OMEGAb2005interpolder(krangeb2005)

arr = np.loadtxt('data/OMGWb1_001.dat')
krangeb1001=[]
OMEGAb1001=[]
krangeb1001nolog=[]
for row in arr:
	krangeb1001.append(np.float(row[0]))
	OMEGAb1001.append(np.float(row[1]))
	krangeb1001nolog.append(10**np.float(row[0]))
OMEGAb1001interpol = UnivariateSpline(krangeb1001, OMEGAb1001,s=0)
OMEGAb1001interpolder=OMEGAb1001interpol.derivative()
OMEGAb1001der=OMEGAb1001interpolder(krangeb1001)

arr = np.loadtxt('data/OMGWb1_005.dat')
krangeb1005=[]
OMEGAb1005=[]
krangeb1005nolog=[]
for row in arr:
	krangeb1005.append(np.float(row[0]))
	OMEGAb1005.append(np.float(row[1]))
	krangeb1005nolog.append(10**np.float(row[0]))
OMEGAb1005interpol = UnivariateSpline(krangeb1005, OMEGAb1005,s=0)
OMEGAb1005interpolder=OMEGAb1005interpol.derivative()
OMEGAb1005der=OMEGAb1005interpolder(krangeb1005)

arr = np.loadtxt('data/OMGWb32_001.dat')
krangeb32001=[]
OMEGAb32001=[]
krangeb32001nolog=[]
for row in arr:
	krangeb32001.append(np.float(row[0]))
	OMEGAb32001.append(np.float(row[1]))
	krangeb32001nolog.append(10**np.float(row[0]))
OMEGAb32001interpol = UnivariateSpline(krangeb32001, OMEGAb32001,s=0)
OMEGAb32001interpolder=OMEGAb2001interpol.derivative()
OMEGAb32001der=OMEGAb32001interpolder(krangeb32001)

arr = np.loadtxt('data/OMGWb32_005.dat')
krangeb32005=[]
OMEGAb32005=[]
krangeb32005nolog=[]
for row in arr:
	krangeb32005.append(np.float(row[0]))
	OMEGAb32005.append(np.float(row[1]))
	krangeb32005nolog.append(10**np.float(row[0]))
OMEGAb32005interpol = UnivariateSpline(krangeb32005, OMEGAb32005,s=0)
OMEGAb32005interpolder=OMEGAb32005interpol.derivative()
OMEGAb32005der=OMEGAb2005interpolder(krangeb32005)
############
####################################
############

plt.plot(krangeb2001,OMEGAb2001,lw=2,color="green",label="$b=2$")
plt.plot(krangeb2005,OMEGAb2005,lw=2,color="green",ls="--")
plt.plot(krangeb32001,OMEGAb32001,lw=2,color="blue",label="$b=3/2$")
plt.plot(krangeb32005,OMEGAb32005,lw=2,color="blue",ls="--")
plt.plot(krangeb1001,OMEGAb1001,lw=2,color="red",label="$b=1$")
plt.plot(krangeb1005,OMEGAb1005,lw=2,color="red",ls="--")

ax=plt.gca()

#ax.set_xscale('log')
#ax.set_yscale('log')


#Axes limit
xmin=-4
xmax=1
ymin=-4
ymax=3

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

first_legend = plt.legend(loc=2,frameon=True,fontsize=16,ncol=3,handlelength=1)

plt.tight_layout()

plt.savefig("plots/GW_spectrum_w<0.pdf", format='pdf',transparent=True)

plt.show()

plt.gcf().clear()




plt.plot(krangeb2001nolog,OMEGAb2001der,lw=2,color="green",label="$b=2$")
plt.plot(krangeb2005nolog,OMEGAb2005der,lw=2,color="green",ls="--")
plt.plot(krangeb32001nolog,OMEGAb32001der,lw=2,color="blue",label="$b=3/2$")
plt.plot(krangeb32005nolog,OMEGAb32005der,lw=2,color="blue",ls="--")
plt.plot(krangeb1001nolog,OMEGAb1001der,lw=2,color="red",label="$b=1$")
plt.plot(krangeb1005nolog,OMEGAb1005der,lw=2,color="red",ls="--")


ax=plt.gca()

#ax.set_xscale('log')
#ax.set_yscale('log')


#Axes limit
xmin=0.001
xmax=0.1
ymin=-5
ymax=5

plt.axis([xmin,xmax,ymin,ymax])



#Axes label
plt.xlabel('$k/k_p$',fontsize=18)
plt.ylabel('$d\\log\\Omega_{\\rm GW}(w=1/9)/d\\log k$',fontsize=18)

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

first_legend = plt.legend(loc=1,frameon=True,fontsize=16,ncol=3,handlelength=1)

plt.tight_layout()

plt.savefig("plots/GW_spectrum_der_w<0.pdf", format='pdf',transparent=True)

plt.show()

plt.gcf().clear()


