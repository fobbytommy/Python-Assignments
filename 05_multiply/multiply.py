# Create a function called 'multiply' that reads each value in the list (e.g. a = [2, 4, 10, 16]) and returns a list where each value has been multiplied by 5.
#
# The function should multiply each value in the list by the second argument. For example, let's say:
#
# a = [2,4,10,16]

a = [2,4,10,16]

def multiply (arr, multi_num):
	newArray = []
	for num in arr:
		num = num * multi_num
		newArray.append(num)
	return newArray

b = multiply(a,5)
print b
