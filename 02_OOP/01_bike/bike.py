# bike OOP

class Bike(object):
	def __init__(self, name, price, max_speed, miles=0):
		self.name = name
		self.price = price
		self.max_speed = max_speed
		self.miles = miles
	def displayInfo(self):
		print "\n{}".format(self.name)
		print "Price: {} dollars".format(self.price)
		print "Maximum Speed: {} mph".format(self.max_speed)
		print "Total Miles:", self.miles, "\n"
	def ride(self):
		print "Riding {}!".format(self.name)
		self.miles += 10
	def reverse(self):
		print "Reversing {}!".format(self.name)
		if (self.miles-5) < 0:
			self.miles = 0
		else:
			self.miles -= 5

# bike 1
bike1 = Bike("bike one", 200, 25)
bike1.ride()
bike1.ride()
bike1.ride()
bike1.reverse()
bike1.displayInfo()

# bike 2
bike2 = Bike("bike two", 1000, 40)
bike2.ride()
bike2.ride()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()

# bike 3
bike2 = Bike("bike three", 800, 35)
bike2.reverse()
bike2.reverse()
bike2.reverse()
bike2.displayInfo()
