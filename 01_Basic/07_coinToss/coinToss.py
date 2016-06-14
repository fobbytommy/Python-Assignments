# You're going to create a program that simulates tossing a coin 5,000 times. Your program should display how many times the head/tail appears.
#
# Sample output should be like the following:
#
#           Starting the program...
#
# Attempt #1: Throwing a coin... It's a head! ... Got 1 head(s) so far and 0 tail(s) so far
# Attempt #2: Throwing a coin... It's a head! ... Got 2 head(s) so far and 0 tail(s) so far
# Attempt #3: Throwing a coin... It's a tail! ... Got 2 head(s) so far and 1 tail(s) so far
# Attempt #4: Throwing a coin... It's a head! ... Got 3 head(s) so far and 1 tail(s) so far
# ........
# Attempt #5000: Throwing a coin... It's a head! ... Got 2412 head(s) so far and 2588 tail(s) so far
#
# Ending the program, thank you!

import random

def coinToss():
	headCount = 0
	tailCount = 0
	for count in range(1, 5001):
		ranNum = round(random.random())
		if ranNum == 1:
			headCount += 1
			print "Attempt #{}: Throwing a coin... It's a head!... Got {} head(s) so far and {} tail(s) so far".format(count, headCount, tailCount)
		else:
			tailCount += 1
			print "Attempt #{}: Throwing a coin... It's a tail!... Got {} head(s) so far and {} tail(s) so far".format(count, headCount, tailCount)

coinToss()
