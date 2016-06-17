# underscore
class Underscore(object):
	def map(self, arr, callback):
		arrNew = []
		for data in arr:
			arrNew.append(callback(data))
		return arrNew
	def reduce(self, arr, callback, initial = None):
		it = iter(arr)
		if initial is None:
			try:
				initial = next(it)
			except StopIteration:
				raise TypeError('reduce() of empty sequence with no initial value')
		reduced = initial
		for data in it: # starts from idx of 0 or 1 depends on initial was None or not.
			reduced = callback(reduced, data)
		return reduced
	def find(self, arr, callback):
		for data in arr:
			if callback(data) == True:
				return data
		return None
	def filter(self, arr, callback):
		arrNew = []
		for data in arr:
			if callback(data) == True:
				arrNew.append(data)
		return arrNew
	def reject(self, arr, callback):
		arrNew = []
		for data in arr:
			if callback(data) == False:
				arrNew.append(data)
		return arrNew

testList = [1,2,3,4,5,6] # this should be untouched
_ = Underscore()

# evens = _.filter(testList, lambda x: x % 2 == 0)
# print testList
# print evens

# addTwo = _.map(testList, lambda x: x+2)
# print testList
# print addTwo

# sum = _.reduce(testList, lambda x, y: x+y, 2)
# print testList
# print sum

# firstEven = _.find(testList, lambda x: x % 2 == 0)
# print testList
# print firstEven

notEvens = _.reject(testList, lambda x: x % 2 == 0)
print testList
print notEvens
