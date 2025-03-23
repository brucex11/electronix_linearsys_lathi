from inspect import currentframe
import numpy as np

import matplotlib.pyplot as plt


def heaviside(self):
	"""
	Build any unit-pulse using 2 unit-steps and plot using matplotlib.
	"""
	fcn_name:str = currentframe().f_code.co_name
	print( f"ENTRYPOINT: Module: '{__name__}'; Class: '{self.__class__.__name__}'" )
	print( f"            Ctor: '{self.__class__.__init__}'; function: '{fcn_name}'" )

	print( 'XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX' )
	pnum:str = f"{self.prob_str}"
	print( f"Problem: '{pnum}'" )
	print( f"{self.problem_txt}" )
	# print( f"{self.problem_ans}" )
	print( '-----------------------------------------------\nNotes:' )


	# Define time vector:
	x_time_start:float = -1  # 'actual' second in time to start the time-span
	x_time_sec:float = 4    # total num 'actual' seconds to time-span
	x_time_tics:int = 1000  # num array elements in time-span
	x_time_delta_tau:float = 1/x_time_tics
	print( f"delta-tau = time-span step-size = {x_time_delta_tau}" )
	t_sig = np.linspace( x_time_start, x_time_sec, x_time_tics )

	#                       0   if x1 < 0
	# heaviside(x1, x2) =  x2   if x1 == 0, where x2 = midpoint of step amplitude: 0 | 0.5 | 1
	#                       1   if x1 > 0
	# Define x1(t): 
	# 'actual' time in seconds:
	#   * positive is delay (earlier in time)
	#   * negative is advance (later in time)
	#   * MUST fall within time-span
	x1_t_start_sec:float = -.1
	x1_t:np.ndarray = np.heaviside( t_sig - x1_t_start_sec, 0.5 )
	# x1_t = np.heaviside(t_sig, 0) - np.heaviside(t_sig - 2, 0)

	# Define x2(t):
	# x2_t_start_sec:float = 1
	# Could also use 'width of pulse' to calc the step-start-time
	pw:float = 2
	x2_t_start_sec:float = pw + x1_t_start_sec
	x2_t:np.ndarray = np.heaviside( t_sig - x2_t_start_sec, 0.5 )

	# Compute the pulse
	pulse:np.ndarray = x1_t - x2_t

	# Plot the pulses and their convolution
	plt.figure(figsize=(10, 6))

	# Plot x1(t)
	plt.subplot(3, 1, 1)
	plt.plot(t_sig, x1_t, label='x1(t)', color='blue')
	plt.title( f"x1(t) = unit-step @ {x1_t_start_sec}s" )
	plt.xlabel('time(s)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot x2(t)
	plt.subplot(3, 1, 2)
	plt.plot(t_sig, x2_t, label='x2(t)', color='r')
	plt.title( f"x2(t) = unit-step @ {x2_t_start_sec}s" )
	plt.xlabel('time(s)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	# Plot the pulse
	plt.subplot(3, 1, 3)
	plt.plot(t_sig, pulse, label='', color='purple')
	plt.title( f"Pulse x1(t) - x2(t), width = {pw}s" )
	plt.xlabel('time(s)')
	plt.ylabel('Amplitude')
	plt.grid(True)

	plt.tight_layout()
	plt.show()
	plt.close()
