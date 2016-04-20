import numpy

class Main:
			
	def __init__(self, x):
		self.x = x;
	
	def magic_square(self):
		return numpy.zeros((self.x, self.x))