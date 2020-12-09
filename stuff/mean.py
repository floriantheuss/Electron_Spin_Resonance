import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate
import math
import os.path

position1 = float(input('position of peak 1: '))
error1 = float(input('error of position of peak 1: '))

position2 = float(input('position of peak 2: '))
error2 = float(input('error of position of peak 2: '))

position = (position1 + position2)/2
error = np.sqrt(error1**2 + error2**2)/2

print ('position is '+str(position)+' +- '+str(error))