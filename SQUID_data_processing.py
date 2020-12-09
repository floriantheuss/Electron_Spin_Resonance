import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import math
import os.path

#filename= input('Enter the filename of the raw SQUID data (e.g, C:\\Users\\F25_1.307_b\\Nextcloud\\Klingeler_Masterarbeit\\howardevansite\\NaCuFe2(VO4)3 powder\\NaCuFe2(VO4)3_fixed powder_M(T)_zfc_5T) without the file type: ')
#type = input('Enter the file type of the SQUID data file (e.g. .dat): ')

filename = 'C:\\Users\\j111\\Box Sync\\Klingeler_Masterarbeit\\howardevansite\\NaCuFe2(VO4)3 powder\\SQUID\\18 Juni 2019_M(T)\\NaCuFe2VO43_18062019_MT5T_zfc.dc'
type = '.dat'


# mass of the sample in mg
#mass = float(input('enter the mass of the sample in mg: '))*10**(-3)
mass = 58.32*10**(-3)
#mass = 53.96*10**(-3)

# molar masses of selected elements in g/mol
Na = 22.98976928
Cu = 63.546
Fe = 55.845
V = 50.9415
O = 15.999
Li = 6.941

# MOLECULAR MASS OF THE COMPOUND
molarmass = Na+Cu+2*Fe+3*(V+4*O)

# magnetic field in Oe
b=[]
# temperature in K
t=[]
# long moment in erg
m=[]
# standard deviation of long moment
deltam=[]

f = open(filename+type, 'r')
f.readline()
for line in f:
    line=line.strip()
    line=line.split()
    b.append(float(line[0]))
    t.append(float(line[1]))
    m.append(float(line[2]))
    deltam.append(float(line[3]))   

t = np.array(t)
b = np.array(b)[t.argsort()]
m = np.array(m)[t.argsort()]
deltam = np.array(deltam)[t.argsort()]
t = np.array(sorted(t))

# since two measurements are taken at the same temperature we will average over those
B = (b[::2]+b[1::2])/2
T = (t[::2]+t[1::2])/2
# Xi in erg/(Oe mol)
Xi = (m[::2]+m[1::2])/2/mass/np.average(B) * molarmass
deltaXi = (deltam[::2]+deltam[1::2])/2/mass/np.average(B) * molarmass

xit = m/mass/np.average(b) * t* molarmass
XiT = (xit[::2]+xit[1::2])/2



# take a discrete derivative of Xi(T) and XiT(T)
derivativeXi = []
for i in np.arange(len(B)):
    if i ==0:
        derivativeXi.append((Xi[i+1]-Xi[i])/(T[i+1]-T[i]))
    elif 0 < i and i < len(B)-1:
        derivativeXi.append(((Xi[i]-Xi[i-1])/(T[i]-T[i-1]) +(Xi[i+1]-Xi[i])/(T[i+1]-T[i]))/2)
    else:
        derivativeXi.append((Xi[i]-Xi[i-1])/(T[i]-T[i-1]))

derivativeXi = np.array(derivativeXi)


derivativeXiT = []
for i in np.arange(len(B)):
    if i ==0:
        derivativeXiT.append((XiT[i+1]-XiT[i])/(T[i+1]-T[i]))
    elif 0 < i and i < len(B)-1:
        derivativeXiT.append(((XiT[i]-XiT[i-1])/(T[i]-T[i-1])+(XiT[i+1]-XiT[i])/(T[i+1]-T[i]))/2)
    else:
        derivativeXiT.append((XiT[i]-XiT[i-1])/(T[i]-T[i-1]))

derivativeXiT = np.array(derivativeXiT)



# write the data into a new file or overwrite an existing file
newfilename=filename+'_processed'+type

if os.path.isfile(newfilename) == True:
    x='w'
else:
    x='x'

with open(newfilename, x) as g:
    g.write('Temperature'+'\t'+'Field'+'\t'+'Static Susceptibility'+'\t'+'Long Scan Std Dev'+'\t'+'dXi/dT'+'\t'+'Xi*T'+'\t'+'d(XiT)/dT'+'\t'+'1/Xi'+'\n')
    g.write('K'+'\t'+'G'+'\t'+'erg/(G^2 mol)'+'\t'+'erg/(G^2 mol)'+'\t'+'erg/(G^2 mol K)'+'\t'+'emu*K/mol'+'\t'+'emu/mol'+'\t'+'mol/emu'+'\n')
    for j in np.arange(len(B)):
        g.write(str(T[j])+'\t'+str(B[j])+'\t'+str(Xi[j])+'\t'+str(deltaXi[j])+'\t'+str(derivativeXi[j])+'\t'+str(XiT[j])+'\t'+str(derivativeXiT[j])+'\t'+str(1/Xi[j])+'\n')