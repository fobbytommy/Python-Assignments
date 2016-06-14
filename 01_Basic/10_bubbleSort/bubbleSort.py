# bubbleSort
import random
import time

# obtaining 100 "psuedo" random values and store them in a variable called 'baseCase'
baseCase = random.sample(range(0, 10000), 100)

# function for bubble sort method
def bubbleSort(listCase):
	fullList = len(listCase) # obtaining length of the case list
	# initializing the index numbers (fromt left to right)
	left = 0
	right = left + 1
	while 0 < fullList:
		for i in range(0, fullList):
			if right < fullList:
				# if number on left is less than number on right,
				if listCase[left] > listCase[right]:
					# they will switch positions
					[listCase[left], listCase[right]] = [listCase[right], listCase[left]]
					# iterating to next cases
					left += 1
					right = left + 1
				else:
					# iterating to next cases
					left += 1
					right = left + 1
			else:
				# if index of the right value is NOT less than length of the list,
				# we have positioned the farthest right value in correct place.
				# therefore, break and start from index 0 and 1 again.
				break
		# index reset to 0 and 1
		left = 0
		right = left + 1
		# far right has been sorted already, so minus 1 to avoid redundancy
		fullList -= 1
	return listCase

print "\nSorted List (using bubble sort):\n"
# start time
startTime = time.time()
print "\t", bubbleSort(baseCase), "\n"
# record time of this bubble sort
print "bubble sort time: {} seconds \n".format(time.time() - startTime)
