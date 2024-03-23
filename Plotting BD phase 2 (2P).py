##2parameters plotting without a colorbar##

import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from matplotlib.ticker import LogLocator
from astropy import constants as scp

#Stevenson's Dataset
BD_stev=pd.read_csv(r'BD_catalogue_20-11-23.csv')
BD_met=BD_stev['FeH']
BD_met_log=np.log(BD_met)
BD_mass=BD_stev['mass']
BD_mass_log=np.log(BD_mass)
BD_min_mass=BD_stev['msini']
BD_min_mass_log=np.log(BD_min_mass)

BD_orbt=BD_stev['period']
BD_orbt_log=np.log(BD_orbt)
BD_ecc=BD_stev['ecc']
BD_ecc_log=np.log(BD_ecc)

#Semimajor axis from Mass and Orbital period
import pandas as pd
import numpy as np

G = 6.67430**11  

def calculate_smaxis(mass, period):
    #mass=(mass*1.898*10^27)
    #period=period*24*3600
    d_day = (((G * mass*1.898*10**27) / 4) ** (1/3)) * (((period*24*3600) / np.pi) ** (2/3))
    d= d_day*6.68459*10**(-12)
    return d

BD_stev['sm_axis'] = calculate_smaxis(BD_stev['mass'], BD_stev['period'])

BD_stev.to_csv("BD_catalogue_20-11-23.csv", index=False)
#print(BD_stev['sm_axis'])
BD_smaxis=BD_stev['sm_axis']

#Small Planets
SP=pd.read_csv(r'Small_Planets.csv')
sp_met=SP['[Fe/H]']
sp_met_log=np.log(sp_met)
sp_mass=SP['pl_mass (Mj)']
sp_mass_log=np.log(sp_mass)
sp_orbt=SP['pl_orb_period']
sp_orbt_log=np.log(sp_orbt)
sp_smaxis=SP['pl_semImjr_axis']
sp_smaxis_log=np.log(sp_smaxis)
#sp_ecc=SP['ecc']
#sp_ecc_log=np.log(sp_ecc) {Eccentricity not available}
#print(sp_met, sp_mass)

#Giant Planets
GP=pd.read_csv(r'Giant_Planets.csv')
gp_met=GP['[Fe/H]']
gp_met_log=np.log(gp_met)
gp_mass=GP['pl_mass (Mj)']
gp_mass_log=np.log(gp_mass)
gp_orbt=GP['pl_orb_period']
gp_orbt_log=np.log(gp_orbt)
gp_smaxis=GP['pl_semImjr_axis']
gp_smaxis_log=np.log(gp_smaxis)
#print(gp_mass, gp_met)
#plt.scatter(gp_met, gp_mass)

#Directly Imaged Planets
DIP=pd.read_csv(r'BDDATA_DIP.csv')
dip_met=DIP['Fe/H']
dip_met_log=np.log(dip_met)
dip_mass=DIP['Planetmass']
dip_mass_log=np.log(dip_mass)
dip_orbt=DIP['Orbital_period']
dip_orbt_log=np.log(dip_orbt)
dip_smaxis=DIP['semimajor_axis']
dip_smaxis_log=np.log(dip_smaxis)

#Directly Imaged Brown Dwarfs
DIBD=pd.read_csv(r'BDDATA_DIBD.csv')
dibd_met=DIBD['Fe_H']
dibd_met_log=np.log(dibd_met)
dibd_mass=DIBD['Planetmass']
dibd_mass_log=np.log(dibd_mass)
dibd_orbt=DIBD['Orbital_period']
dibd_orbt_log=np.log(dibd_orbt)
dibd_smaxis=DIBD['semimajor_axis']
dibd_smaxis_log=np.log(dibd_smaxis)

##Mass vs Fe##

from matplotlib.cm import get_cmap
from matplotlib.colors import LinearSegmentedColormap
plt.figure(figsize=(21,7))
sc=plt.scatter(BD_mass, BD_met, label="Stevenson's", c='blue', alpha=0.6, marker="o")
sc=plt.scatter(BD_min_mass,BD_met, c='blue', alpha=0.6, marker="o")
sc=plt.scatter(sp_mass,sp_met, label="Small Planets", c='orange', alpha=0.6, marker="d")
plt.xscale('log')
plt.xlim(xmin=0.005, xmax=100)
sc=plt.scatter(gp_mass,gp_met, label="Giant Planets", c='y', alpha=0.6, marker="X")
sc=plt.scatter(dip_mass,dip_met, label="DIP", c='r', alpha=1, marker="^")
sc=plt.scatter(dibd_mass,dibd_met, label="DIBD", c='black', alpha=1, marker="*", s=400)
plt.xticks([0.005,0.01,0.02,0.05, 0.1, 0.2, 0.5,1,2,5,10,20,50,100,200,500,1000])
locator = LogLocator(base=10)  # Specify base-10 logarithm for ticks
plt.gca().xaxis.set_major_locator(locator)
plt.legend()
plt.grid()
#ax.set_axisbelow(True)
#plt.colorbar(sc)
#plt.colorbar.label('Orbital Period (days)')
#cmap = get_cmap('brg')
#colors = plt.cm.viridis.colors[::-1]
#inverted_cmap = LinearSegmentedColormap.from_list('my_inverted_colormap', colors)
#plt.colorbar(cmap=inverted_cmap, label='Log of Orbital Period (d)')
#plt.colorbar(cmap='colors', label='Log of Orbital Period (d)')
plt.axvline(x=13,linestyle='--')
plt.axvline(x=80,linestyle='--')
plt.xlabel('Mass/Msini (Mj)')
plt.ylabel('[Fe/H]')
plt.title('Exoplanets Fe/H at different mass')
plt.legend()


##Mass vs FOrbital Period#
plt.figure(figsize=(30,10))
sc=plt.scatter(BD_mass, BD_orbt, label="Stevenson's", c='blue', alpha=1, marker="o")
sc=plt.scatter(BD_min_mass,BD_orbt, c='blue', alpha=1, marker="o")
sc=plt.scatter(sp_mass,sp_orbt, label="Small Planets", c='orange', alpha=0.6, marker="d")
plt.xscale('log')
plt.yscale('log')
plt.xlim(xmin=0.005, xmax=100)
plt.ylim(ymin=0.005, ymax=1000000)
sc=plt.scatter(gp_mass,gp_orbt, label="Giant Planets", c='green', alpha=1, marker="d")
sc=plt.scatter(dip_mass,dip_orbt, label="DIP", c='red', marker="^")
sc=plt.scatter(dibd_mass,dibd_orbt, label="DIBD", c='black', marker="*", s=300)
plt.xticks([0.005,0.01,0.02,0.05, 0.1, 0.2, 0.5,1,2,5,10,20,50,100,200,500,1000])
locator = LogLocator(base=10)  # Specify base-10 logarithm for ticks
plt.gca().xaxis.set_major_locator(locator)
plt.grid()
#plot_color_gradients('Cyclic'['hsv'])
#ax.set_axisbelow(True)
#plt.colorbar(sc)
#plt.colorbar.label('Orbital Period (days)')
#plt.colorbar(label='Fe/H')
plt.axvline(x=13,linestyle='--')
plt.axvline(x=80,linestyle='--')
plt.xlabel('Mass/Msini (Mj)')
plt.ylabel('Orbital Period')
plt.title('Exoplanets Period at different mass')
plt.legend()
plt.show()


## SM axis vs Fe##
plt.figure(figsize=(24,8))
sc=plt.scatter(BD_met, BD_smaxis, label="Stevenson's", c='blue', alpha=0.6, marker="o")
sc=plt.scatter(BD_met,BD_smaxis, c='blue', marker="o")
sc=plt.scatter(sp_met,sp_smaxis, label="Small Planets", c='orange', alpha=0.6, marker="v")
#plt.xscale('log')
plt.yscale('log')
#plt.xlim(xmin=0.005, xmax=100)
plt.ylim(ymin=0.005, ymax=150000)
sc=plt.scatter(gp_met,gp_smaxis, label="Giant Planets", c='green', alpha=1, marker="^")
sc=plt.scatter(dip_met,dip_smaxis, label="DIP", c='red', marker="d")
sc=plt.scatter(dibd_met,dibd_smaxis, label="DIBD", c='black', marker="*", s=300)
plt.grid()

#plt.colorbar(label='Log Mass/Mcsini (Mj)', cmap='viridis_r')
#plt.axvline(x=13,linestyle='--',label='13')
#plt.axvline(x=80,linestyle='--',label='80')
plt.xlabel('Fe/H')
plt.ylabel('Semimajor axis')
plt.title('Exoplanets Fe/H at different Orbital Period')
plt.legend()
plt.show()


##smaxis vs mass##
plt.figure(figsize=(24,8))
sc=plt.scatter(BD_mass, BD_smaxis, label="Stevenson's", c='blue', alpha=0.6, marker="o")
sc=plt.scatter(BD_min_mass,BD_smaxis, c='blue', marker="o")
sc=plt.scatter(sp_mass,sp_smaxis, label="Small Planets", c='orange', vmax=3, alpha=0.6, marker="v")
#plt.xscale('log')
#plt.yscale('log')
plt.xlim(xmin=0.005, xmax=150)
plt.ylim(ymin=0.001, ymax=15000)
sc=plt.scatter(gp_mass,gp_smaxis, label="Giant Planets", c='green', alpha=0.6, marker="^")
sc=plt.scatter(dip_mass,dip_smaxis, label="DIP", c='red', marker="d")
sc=plt.scatter(dibd_mass,dibd_smaxis, label="DIBD", c='black', marker="*", s=500)
#plt.xticks([0.005,0.01,0.02,0.05, 0.1, 0.2, 0.5,1,2,5,10,20,50,100,200,500,1000])
plt.xscale('log')
plt.yscale('log')
plt.grid()
#plt.set_xlim()
#plt.ylim(ymin=-1,ymax=120000)
#plt.colorbar(sc).pad(0.2)
#plt.colorbar(label='Log Mass/Mcsini (Mj)')
plt.axvline(x=13,linestyle='--')
plt.axvline(x=80,linestyle='--')
plt.xlabel('Mass (Mj)')
plt.ylabel('Semimajor axis')
plt.title('Exoplanets Fe/H at different Orbital Period')
plt.legend()
plt.show()


