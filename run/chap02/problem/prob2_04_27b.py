import ast
from inspect import currentframe
import math
import numpy as np
from typing import List, Tuple  # Any, Dict, Set

import matplotlib.pyplot as plt

def prob2_04_27b(self):
	"""Page 228
	Linear Systems and Signals, Lathi
	Prob 2.4-27 (b) Find and sketch c(t) = x1(t) * x2(t) for the pairs of functions
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


	# Define time vector (from -10 to 10 seconds for a wide enough range)
	t = np.linspace(-6, 6, 1000)

	# u_t = np.heaviside(t, 1)  # np.heaviside returns 1 for t >= 0 and 0 for t < 0
	# Define signal 1: pulse from 3 to 5 sec
	sig1:np.ndarray = np.heaviside(t-3, 0) - np.heaviside(t-5, 0)

	# Define signal 2: pulse from -5 to -3 sec
	sig2:np.ndarray = np.heaviside(t+5, 0) - np.heaviside(t+3, 0)
	print( f"type(sig2): {type(sig2)}" )

	# Compute the convolution of the two signals
	conv_mode:str = 'same'
	conv_result:np.ndarray = \
		np.convolve( sig1, sig2, mode=conv_mode ) * (t[1] - t[0])  # Multiply by delta t for correct scaling

	# Plot the pulses and their convolution
	plt.figure(figsize=(10, 6))

	# Plot signal 1
	plt.subplot(3, 1, 1)
	plt.plot(t, sig1, label='x1(t)', color='blue')
	plt.title('x1(t)')
	plt.xlabel('Time (seconds)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot signal 2
	plt.subplot(3, 1, 2)
	plt.plot(t, sig2, label='x2(t)', color='r')
	plt.title('x2(t)')
	plt.xlabel('Time (seconds)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot the Convolution of signal 1 and signal 2
	plt.subplot(3, 1, 3)
	plt.plot(t, conv_result, label='Convolution', color='purple')
	plt.title('Convolution of x1(t) and x2(t)')
	plt.xlabel('Time (seconds)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	plt.tight_layout()
	plt.show()


