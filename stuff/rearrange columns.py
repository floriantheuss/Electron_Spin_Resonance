import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit
import math
import os.path


file_1 = input('Part of the filename that a lot of files have in common (start: C:\\Users\\F25_1.307_b\\Nextcloud\\Klingeler_Masterarbeit\\...): ')
file_2 = input('Part of the filename that distinguishes most files: ')

file = open(file_1+file_2, 'r')
header = f.readline()
header = header.strip()
header = header.split()
for line in f:
    line=line.strip()
    line=line.split()
    temp.append(float(line[0]))
    field.append(float(line[1]))
    amp.append(float(line[2]))
    phase.append(float(line[3]))
    real.append(float(line[4]))
    imaginary.append(float(line[5]))


print (header)

order = input('Enter a series of numbers which give the number of the final column: ')