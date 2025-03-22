import ast
from inspect import currentframe
import math
import numpy as np
from typing import List, Tuple  # Any, Dict, Set

import matplotlib.pyplot as plt

def prob2_04_27g(self):
	"""Page 228
	Linear Systems and Signals, Lathi
	Prob 2.4-27 (g) Find and sketch c(t) = x1(t) * x2(t) for the pairs of functions
	illustrated in Fig. P2.4-27.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: {pnum}\nSolution" )
	print( f"{self.problem_txt}" )
	print( f"{self.problem_ans}" )
	assert_percentage:float = 2.0
	print( '-----------------------------------------------\nSolution' )


	# ---- chatgpt -------------------
	# Define time vector (from -10 to 10 seconds for a wide enough range)
	t = np.linspace(-4, 4, 1000)

	# Define ramp
	# Create the ramp function: amplitude from 1 to 0 between -1 and 0, and 0 elsewhere
	signal1 = np.where((t >= -1) & (t <= 0), 1 - (t + 1), 0)

	# Define x2(t): value 2 between -5 and -4 seconds, zero elsewhere
	signal2 = np.heaviside(t, 0)  # np.heaviside returns 1 for t >= 0 and 0 for t < 0

	# Compute the convolution of the two pulses
	conv_result = np.convolve(signal1, signal2, mode='same') * (t[1] - t[0])  # Multiply by delta t for correct scaling

	# Plot the pulses and their convolution
	plt.figure(figsize=(10, 6))

	# Plot x1(t)= 1 / (t^2+1 )
	plt.subplot(3, 1, 1)
	plt.plot(t, signal1, label='', color='blue')
	plt.title('x1(t) = ramp')
	plt.xlabel('Time (seconds)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot x2(t)
	plt.subplot(3, 1, 2)
	plt.plot(t, signal2, label='x2(t)', color='r')
	plt.title('x2(t)')
	plt.xlabel('Time (seconds)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot the Convolution of x1(t)= 1 / (t^2+1 ) and x2(t)
	plt.subplot(3, 1, 3)
	plt.plot(t, conv_result, label='Convolution', color='purple')
	plt.title('Convolution of x1(t) = ramp and x2(t)')
	plt.xlabel('Time (seconds)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	plt.tight_layout()
	plt.show()


