import numpy

class Magic:

	def __init__(self, dim):
		self.dim = dim
		self.matrix = numpy.fromfunction(lambda i, j: (j+i*self.dim+1), (self.dim, self.dim), dtype=int)
		self.msquare = numpy.zeros([self.dim, self.dim], dtype=int)

	def sum(self):
		return self.dim*((self.dim**2)+1)/2

	def square(self):
		for i in range(0,self.dim):
			self.msquare[i][i]=self.matrix[i][i]
		for i in range(0,self.dim):
			self.msquare[i][self.dim-(i+1)]=self.matrix[i][self.dim-(i+1)]
		if self.dim % 2 == 1:
			for i in range(0,self.dim):
				self.msquare[int(self.dim/2)][i]=self.matrix[int(self.dim/2)][i]
				self.msquare[i][int(self.dim/2)]=self.matrix[i][int(self.dim/2)]

		return self.msquare

	def to_s(self):
		return '\n'+('\n'.join([''.join(['{:4}'.format(item) for item in row]) for row in self.msquare]))



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