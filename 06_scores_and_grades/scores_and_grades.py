# knowns:
# Collect 10 scores from the user
# Scores must be number between 60 and 100
# Print corresponding letter grade for scores

# unknowns:
# User input

scores = []

def printGrades(grades):
	for grade in grades:
		if grade < 70:
			print "Your score is {}; your letter grade is D.".format(grade)
		elif grade < 80:
			print "Your score is {}; your letter grade is C.".format(grade)
		elif grade < 90:
			print "Your score is {}; your letter grade is B.".format(grade)
		else:
			print "Your score is {}; your letter grade is A.".format(grade)

def getScores():
	while (len(scores) < 10):
		try:
			userinput = int(raw_input("Please enter a grade between 60 and 100: "))
		except ValueError:
			print "Please provide a whole number input!"
		else:
			if not 60 <= userinput <= 100:
				print "Please provide a whole number between 60 and 100!"
			else:
				scores.append(userinput)
				print("Score added")
	printGrades(scores)

getScores()
