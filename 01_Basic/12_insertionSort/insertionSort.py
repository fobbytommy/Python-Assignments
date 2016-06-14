# insertionSort
import random
import time

# obtaining 100 "psuedo" random values and store them in a variable called 'baseCase'
baseCase = random.sample(range(0, 10000), 100)

# function for insertion sort method
def insertionSort(baseCase):
	# call every index starting from index of 1
	for index in range(1, len(baseCase)):
		# initializing currentIndex we will be using
		currentIndex = index
		# initializing how many "jumps" the current value will make to be inserted to a correct spot
		count = 0
		# if index is greater than 1,
		if index > 1:
			while index >= 0:
				if baseCase[currentIndex] < baseCase[index-1] and index-1 != -1:
					count += 1 # counting how many skips or jumps our current value need to make to be inserted to a correct location
				index -= 1 # check next index!
			# temporary store current value
			temp = baseCase[currentIndex]
			# shifting the lists from left to right to make room for the future inserted value
			for i in range(0, count):
				baseCase[currentIndex-i] = baseCase[currentIndex-i-1]
			# insert the value
			baseCase[currentIndex-count] = temp
		# if not, that means we are at index 1
		else:
			# compare value from index 0 and 1
			# if value of index 1 is less than that of index 0, then swap!
			if baseCase[currentIndex] < baseCase[0]:
				[baseCase[currentIndex], baseCase[0]] = [baseCase[0], baseCase[currentIndex]]
	return baseCase

print "\nSorted List (using insertion sort):\n"
# start time
startTime = time.time()
print "\t", insertionSort(baseCase), "\n"
# record time of this insertion sort
print "insertion sort time: {} seconds \n".format(time.time() - startTime)
