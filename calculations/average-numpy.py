# -----------------------------------------------------------
# calculate the arithmetic mean of a list of integers using NumPy
#
# (C) 2016 Frank Hofmann, Berlin, Germany
# Released under GNU Public License (GPL)
# email frank.hofmann@efho.de
# -----------------------------------------------------------

# requirements:
# * Python 3.x
# * NumPy for Python 3 (http://www.numpy.org/)

# import external NumPy module
import numpy as np

# define a list of values
valueList = np.array([1, 6, 3, 4, 5])

# check for empty lists, first
if valueList.any():
	mean = np.mean(valueList)

	# Note:
	# for Python 2.x, the average value is 3.7999999999999998
	# for Python 3.x, the average value is 3.8 (float value)

	# output average value
	print ("The arithmetic average value is:", mean)
else:
	print ("The list is empty.")

