# animal

# parent class
class Animal(object):
	def __init__(self, name):
		self.name = name
		self.health = 100
	def walk(self):
		if self.health-1 < 0:
			self.health = 0
		else:
			self.health -= 1
		return self
	def run(self):
		if self.health-5 < 0:
			self.health = 0
		else:
			self.health -= 5
		return self
	def displayHealth(self):
		print "Name: {}".format(self.name)
		print "Health: {}".format(self.health)
		return self
# instacne of Animal class
animal = Animal('Bigfoot')
animal.walk().walk().walk().run().run().displayHealth()

# Dog: subclass of Aniaml class
class Dog(Animal):
	def __init__(self, *args):
		super(Dog, self).__init__(*args)
		self.health = 150
	def pet(self):
		self.health += 5
		return self
# instance of a Dog class
dog = Dog('Doggy')
dog.walk().walk().walk().run().run().pet().displayHealth()

# Dragon: another subclass of Animal class
class Dragon(Animal):
	def __init__(self, *args):
		super(Dragon, self).__init__(*args)
		self.health = 170
	def fly(self):
		if self.health-10 < 0:
			self.health = 0
		else:
			self.health -= 10
		return self
	def displayHealth(self):
		print "This is a dragon!"
		super(Dragon, self).displayHealth()
# instance of a Dragon class
dragon = Dragon('Tommy')
dragon.walk().walk().walk().run().run().fly().fly().displayHealth()
