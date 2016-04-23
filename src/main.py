import numpy

class Main:

	def __init__(self, x):
		self.x = x
		self.matrix = numpy.fromfunction(lambda i, j: (j+i*self.x+1), (self.x, self.x), dtype=int)

	def magic_sum(self):
		return self.x*((self.x**2)+1)/2

	def magic_square(self):
		self.print_square()
		return self.matrix

	def magic_row(self):
		row = []
		while numpy.sum(row)!=self.magic_sum():
			row = numpy.random.choice(self.matrix.flatten(), self.x)
		return row

	def print_square(self):
		print('\n')
		print('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.matrix]))

		# STEP1 - select a number (32 - 1 out of 10)
		# STEP1 - make sure that the current total does not exceed 505
		# STEP1 - if it does select another smaller number
		# STEP1 - if is does not continue
		# STEP1 - remove 32 from the pool of numbers to select from
		# STEP1 - check the difference between 505 and this number (473)
		# STEP2 - select another number (44 - 2 out of 10)
		# STEP2 - make sure that the current total does not exceed 505
		# STEP2 - if it does selecr another smaller number
		# STEP2 - if is does not continue
		# STEP2 - remove 44 from the pool of numbers to select from
		# STEP2 - check the difference between 473 and this number (429)
		# .
		# .
		# .
		# STEP9 - when only 1 number remains you need to make sure you rach 505
		# STEP9 - if you don't restart from STEP8