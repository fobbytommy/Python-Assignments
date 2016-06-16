# MathDojo

class MathDojo(object):
	def __init__(self):
		self.sum = 0
	def add(self, *kwargs):
		for arg in kwargs:
			if isinstance(arg, list) or isinstance(arg, tuple):
				for num in arg:
					self.sum += num
			else:
				self.sum += arg
		return self
	def subtract(self, *kwargs):
		for arg in kwargs:
			if isinstance(arg, list) or isinstance(arg, tuple):
				for num in arg:
					self.sum -= num
			else:
				self.sum -= arg
		return self
	def result(self):
		print self.sum

# instance called part 1
part1 = MathDojo()
part1.add(2).add(2, 5).subtract(3, 2).result()

# instance called part 2
part2 = MathDojo()
part2.add([1], 3, 4).add([3, 5, 7, 8],[2, 4.3, 1.25]).subtract(2, [2, 3], [1.1, 2.3]).result()

# instance called part 3
part3 = MathDojo()
part3.add([1], (3), 4).add([3, 5, 7, 8],[2, 4.3, 1.25]).subtract((2), [2, 3], [1.1, 2.3]).result()
