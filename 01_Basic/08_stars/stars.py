# Part 1
# Create a function called  draw_stars() that takes a list of numbers and prints out  *.
#
# Part 2
# Modify the function above. Allow a list containing integers and strings to be passed to the  draw_stars() function. When a string is passed, instead of  displaying *, display the first letter of the string according to the example below. You may use the .lower() string method for this part.

x = [4, 6, 1, 3, 5, 7, 25]
y = [4, "Tom", 1, "Michael", 5, 7, "Jimmy Smith"]

def draw_stars(arr):
	for thing in arr:
		if isinstance(thing, int): 		# check if the list contains integer
			print "*" * thing
		else:
			word = thing.lower() 		# changes the string to all lowercase
			newWord = word[0] 			# new string with the first letter of the word only
			for i in range(1,len(word)):	# loop thorough each char in string starting from index of 1
				temp = word.replace(word[i], word[0])	# replace the char to first char of the string
			 	newWord += temp[i]		# add each char to the new word
			print newWord

draw_stars(y)
