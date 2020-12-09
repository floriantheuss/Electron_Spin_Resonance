from tkinter import filedialog
from tkinter import *

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import os.path


root = Tk()
root.withdraw()

filename =  filedialog.askopenfilename(initialdir = "C:\\Users\\j111\\Nextcloud\\Klingeler_Masterarbeit\\howardevansite\\NaCuFe2(VO4)3 powder\\data fixed powder\\4K\\",title = "Select file",filetypes = (("all files","*.*"),("all files","*.*")))
filename = filename.replace('/','\\')

type = input('is this a temperature dependent or an individual measurement? [t/i] ')

namefile = filename[::-1]
position = namefile.find('\\')
file = filename[-position:]

if type == 't':
	fb = file.find('F')
	fe = file.find('G')
	Tb = file.find('T')
	Te = file.find('K')

	comment = file[Tb+1:Te]+'K '+file[fb+1:fe]+'GHz'
	
	F047p4T04K-d
else:
	F = file.find('F')
	p = file.find('p')
	T = file.find('T')
	K = file.find('K')
	
	if file[F+1] == '0':
		frequency = file[F+2:p]+'.'+file[p+1:T]+'GHz'
	else:
		frequency = file[F+1:p]+'.'+file[p+1:T]+'GHz'
	
	if file[T+1] == '0':
		Temp = file[T+2:K+1]
	else:
		Temp = file[T+1:K+1]
	
	comment = Temp+' '+frequency




# field in T
field = []
# amplitude in db
amp=[]
# phase in °
phase = []
# temperature in K
temp=[]
# real part
real=[]
# imaginary part
imaginary=[]
# phase corrected signal
phasecorr = []
# SPEC
spec = []
# easy Spin fit
easySpin = []



f = open(filename, 'r')
f.readline()
f.readline()
for line in f:
    line=line.strip()
    line=line.split()
    field.append(float(line[0]))
    amp.append(float(line[1]))
    phase.append(float(line[2]))
    real.append(float(line[3]))
    imaginary.append(float(line[4]))
    temp.append(float(line[5]))
    phasecorr.append(float(line[6]))
    spec.append(float(line[7]))
    easySpin.append(float(line[8]))

field = np.array(field)
amp = np.array(amp)
phase = np.array(phase)
temp = np.array(temp)
real = np.array(real)
imaginary = np.array(imaginary)
phasecorr = np.array(phasecorr)
spec = np.array(spec)
easySpin = np.array(easySpin)

with open(filename, 'w') as g:
	g.write('Field'+'\t'+'Amp'+'\t'+'Phase'+'\t'+'RealPart'+'\t'+'ImaginaryPart'+'\t'+'T2'+'\t'+'PhaseCorr'+'\t'+'SPEC'+'\t'+'easySpinFit'+'\n')
	g.write('T'+'\t'+'dB'+'\t'+'°'+'\t'+''+'\t'+''+'\t'+'K'+'\t'+'dB'+'\t'+''+'\t'+''+'\n')
	g.write(''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+comment+'\t'+''+'\t'+''+'\n')
	for i in np.arange(len(field)):
		g.write(str(field[i])+'\t'+str(amp[i])+'\t'+str(phase[i])+'\t'+str(real[i])+'\t'+str(imaginary[i])+'\t'+str(temp[i])+'\t'+str(phasecorr[i])+'\t'+str(spec[i])+'\t'+str(easySpin[i])+'\n')