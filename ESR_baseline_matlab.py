from tkinter import filedialog
from tkinter import *

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import os.path
import sys


root = Tk()
root.withdraw()

filename =  filedialog.askopenfilename(initialdir = "C:\\Users\\j111\\Nextcloud\\Klingeler_Masterarbeit\\howardevansite\\NaCuFe2(VO4)3 powder\\data fixed powder\\TempDep263p3\\",title = "Select file",filetypes = (("all files","*.*"),("all files","*.*")))
filename = filename.replace('/','\\')

namefile = filename[::-1]
position = namefile.find('\\')
file = filename[-position:]

if file[4] == '-':
	namefile = filename[::-1]
	position = namefile.find('\\')
	file = filename[-position:]

	fb = file.find('F')
	fe = file.find('G')
	Tb = file.find('T')
	Te = file.find('K')

	comment = file[Tb+1:Te]+'K '+file[fb+1:fe]+'GHz'
	
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

mask = []
for i in phasecorr:
    if np.isnan(i) == True:
        mask.append(False)
    else:
        mask.append(True)

field = field[mask]
amp = amp[mask]
phase = phase[mask]
temp = temp[mask]
real = real[mask]
imaginary = imaginary[mask]
phasecorr = phasecorr[mask]
spec = spec[mask]
easySpin = easySpin[mask]


def polynomial(x, a, b, c, d, e, f, g, h, i, j):
    return (a*x**9 + b*x**8 + c*x**7 + d*x**6 + e*x**5 + f*x**4 + g*x**3 + h*x**2 + i*x + j)

def fitpolynomial(n, xmin, xmax, amp, field):
    mask = np.array([[any([(field<xmin[j])[i],(field>xmax[j])[i]]) for i in np.arange(len(field))] for j in np.arange(len(xmax))])
    mask = [all([mask[j,i] for j in np.arange(len(xmax))]) for i in np.arange(len(field))]
    fieldcut = field[mask]
    ampcut = amp[mask]

    if n == 9:
        def fct(x, a, b, c, d, e, f, g, h, i, j):
            return polynomial(x, a, b, c, d, e, f, g, h, i, j)
        parameters, pcov = curve_fit(fct, fieldcut, ampcut)
        fit = fct(field, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6], parameters[7], parameters[8], parameters[9])
           
    elif n==8:
        def fct(x, b, c, d, e, f, g, h, i, j):
            return polynomial(x, 0, b, c, d, e, f, g, h, i, j)
        parameters, pcov = curve_fit(fct, fieldcut, ampcut)
        fit = fct(field, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6], parameters[7], parameters[8])
           
    elif n==7:
        def fct(x, c, d, e, f, g, h, i, j):
            return polynomial(x, 0, 0, c, d, e, f, g, h, i, j)
        parameters, pcov = curve_fit(fct, fieldcut, ampcut)
        fit = fct(field, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6], parameters[7])
         
    elif n==6:
        def fct(x, d, e, f, g, h, i, j):
            return polynomial(x, 0, 0, 0, d, e, f, g, h, i, j)
        parameters, pcov = curve_fit(fct, fieldcut, ampcut)
        fit = fct(field, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5], parameters[6])
               
    elif n==5:
        def fct(x, e, f, g, h, i, j):
            return polynomial(x, 0, 0, 0, 0, e, f, g, h, i, j)
        parameters, pcov = curve_fit(fct, fieldcut, ampcut)
        fit = fct(field, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4], parameters[5])
               
    elif n==4:
        def fct(x, f, g, h, i, j):
            return polynomial(x, 0, 0, 0, 0, 0, f, g, h, i, j)
        parameters, pcov = curve_fit(fct, fieldcut, ampcut)
        fit = fct(field, parameters[0], parameters[1], parameters[2], parameters[3], parameters[4])
              
    elif n==3:
        def fct(x, g, h, i, j):
            return polynomial(x, 0, 0, 0, 0, 0, 0, g, h, i, j)
        parameters, pcov = curve_fit(fct, fieldcut, ampcut)
        fit = fct(field, parameters[0], parameters[1], parameters[2], parameters[3])
        
    elif n==2:
        def fct(x, h, i, j):
            return polynomial(x, 0, 0, 0, 0, 0, 0, 0, h, i, j)
        parameters, pcov = curve_fit(fct, fieldcut, ampcut)
        fit = fct(field, parameters[0], parameters[1], parameters[2])
                        
    elif n==1:
        def fct(x, i, j):
            return polynomial(x, 0, 0, 0, 0, 0, 0, 0, 0, i, j)
        parameters, pcov = curve_fit(fct, fieldcut, ampcut)
        fit = fct(field, parameters[0], parameters[1])
            
    ampsubtract = amp - fit
    return (ampsubtract, fit)

fig, ax1 = plt.subplots()

ax1.set_xlabel('field')
ax1.set_ylabel('amp', color = 'red')
ax1.plot(field, phasecorr, color = 'red')
ax1.tick_params(axis='y', labelcolor = 'red')

ax2 = ax1.twinx()

ax2.set_ylabel('phase', color = 'navy')
ax2.plot(field, phase, color = 'navy')
ax2.tick_params(axis='y', labelcolor = 'navy')

fig.tight_layout()
plt.show()


min = input('enter the minimum values of the peaks separated by commas: ')
max = input('enter the maximum values of the peaks separated by commas: ')

xmin = []
xmax = []

for i in np.arange(min.count(',')):
	a = min.find(',')
	b = max.find(',')

	xmin.append(float(min[:a]))
	xmax.append(float(max[:b]))
	
	min = min[a+1:]
	max = max[b+1:]
xmin.append(float(min))
xmax.append(float(max))

happy = 'n'


while happy=='n':
	
	n = float(input('what order polynomial do you want to fit to the data? '))
	
	ampsubtract = fitpolynomial(n, xmin, xmax, phasecorr, field)[0]
	fitpoly = fitpolynomial(n, xmin, xmax, phasecorr, field)[1]

	fig = plt.figure(figsize=[10,3])
	ax1 = fig.add_subplot(1,2,1)
	ax2 = fig.add_subplot(1,2,2)

	ax1.plot(field, phasecorr)
	ax1.plot(field, fitpoly)

	ax2.plot(field, ampsubtract)
	
	plt.show()

	happy = input('are you happy with the subtracted curve? [y/n/end/new]: ')
	
	if happy == 'end':
		break
	
	if happy == 'new':
		fig, ax1 = plt.subplots()

		ax1.set_xlabel('field')
		ax1.set_ylabel('amp', color = 'red')
		ax1.plot(field, phasecorr, color = 'red')
		ax1.tick_params(axis='y', labelcolor = 'red')

		ax2 = ax1.twinx()

		ax2.set_ylabel('phase', color = 'navy')
		ax2.plot(field, phase, color = 'navy')
		ax2.tick_params(axis='y', labelcolor = 'navy')

		fig.tight_layout()
		plt.show()


		min = input('enter the minimum values of the peaks separated by commas: ')
		max = input('enter the maximum values of the peaks separated by commas: ')

		xmin = []
		xmax = []

		for i in np.arange(min.count(',')):
			a = min.find(',')
			b = max.find(',')

			xmin.append(float(min[:a]))
			xmax.append(float(max[:b]))
	
			min = min[a+1:]
			max = max[b+1:]
		xmin.append(float(min))
		xmax.append(float(max))
		
		happy = 'n'
	
	
if happy == 'y':
	
	#namefile = filename[::-1]
	#position = namefile.find('\\')
	#filenamenew = filename[:-position]+'baseline_'+filename[-position:]
	filenamenew = filename[:-4]+'_baseline.txt'
	
	if os.path.isfile(filenamenew) == True:
		x='w'
	else:
		x='x'
	
	with open(filenamenew, x) as g:
		g.write('Field'+'\t'+'Amp'+'\t'+'Phase'+'\t'+'RealPart'+'\t'+'ImaginaryPart'+'\t'+'T2'+'\t'+'PhaseCorr'+'\t'+'SPEC'+'\t'+'easySpinFit'+'\n')
		g.write('T'+'\t'+'dB'+'\t'+'°'+'\t'+''+'\t'+''+'\t'+'K'+'\t'+'dB'+'\t'+''+'\t'+''+'\n')
		g.write(''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+''+'\t'+comment+'\t'+''+'\t'+''+'\n')
		for i in np.arange(len(field)):
			g.write(str(field[i])+'\t'+str(amp[i])+'\t'+str(phase[i])+'\t'+str(real[i])+'\t'+str(imaginary[i])+'\t'+str(temp[i])+'\t'+str(ampsubtract[i])+'\t'+str(spec[i])+'\t'+str(easySpin[i])+'\n')
	
	print('perfect')