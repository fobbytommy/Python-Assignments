# selectionSort
import random
import time

# obtaining 100 "psuedo" random values and store them in a variable called 'baseCase'
baseCase = random.sample(range(0, 10000), 100)

# function for selection sort method
def selectionSort(listCase):
	itrStart = 1 # initializing starting index to compare
	count = 0 # counting the number of steps for selection sort
	# for every data in the list
	for data in baseCase:
		# remember the index of the current data we are on
		currentIndex = listCase.index(data)
		# initialize that current data to be a "minimum" number
		minIndex = listCase.index(data)
		# running thorough every index that will be compared to the current data
		for index in range(itrStart, len(baseCase)):
			count +=1
			# if we find the smaller number,
		 	if listCase[minIndex] > listCase[index]:
				# that number becomes the new "minimum" number
				minIndex = index
				count +=1
			else:
				count +=1
		# selected minimum number will be swap place with the current data
		[listCase[currentIndex], listCase[minIndex]] = [listCase[minIndex], listCase[currentIndex]]
		itrStart += 1 # since farthest left has been sorted, no need for redundancy
		count +=1
	return (listCase, count) # return both sorted list and steps

print "\nSorted List (using selection sort):\n"
# start time
startTime = time.time()
solution = selectionSort(baseCase)
print "\t", solution[0], "\n"
# record time of this selection sort
print "selection sort time: {} seconds".format(time.time() - startTime)
# proof of efficiency: N^2
print "# of steps to sort: {} steps\n".format(solution[1])
