import numpy as np
import matplotlib.pyplot as plt
import math
import os.path

#position11 = float(input('position of left signal 1: '))
#position12 = float(input('position of right signal 1: '))


#position21 = input('position of left signal 2: ')
#position22 = input('position of right signal 2: ')

#if position21 == '' or position22 == '':
#	position = (position11 + position12)/2
#	error = (abs(position-position11)+abs(position-position12))/2

#else:
#	position21 = float(position21)
#	position22 = float(position22)



#	position1 = (position11 + position12)/2
#	error1 = (abs(position1-position11)+abs(position1-position12))/2

#	position2 = (position21 + position22)/2
#	error2 = (abs(position2-position21)+abs(position2-position22))/2

#	position = (position1 + position2)/2
#	error = np.sqrt(error1**2+error2**2)/2
	
#error = str(error)
#spot = error.find('.')

#if float(error[spot-1]) > 0:

#elif float(error[spot+1]) > 1:
#	position = round(position, 1)
#	error = round(float(error),1)
#elif float(error[spot+1]) == 1:
#	position = round(position, 2)
#	error = round(float(error),2)
#else:
#	if float(error[spot+2]) > 1:
#		position = round(position, 2)
#		error = round(float(error),2)
#	else:
#		position = round(position, 3)
#		error = round(float(error),3)

position1 = float(input('field 1: '))
error1 = float(input('error 1: '))
position2 = float(input('field 2: '))
error2 = float(input('error 2: '))

position = ( position1 + position2 ) / 2
error = np.sqrt( error1**2 + error2**2 ) / 2

print ('position is '+str(position)+' +- '+str(error))