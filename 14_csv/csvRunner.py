# CSV (Comma Separated Values)

import csv

# openning the CSV file
with open('us-500.csv', 'rU') as csvfile:
	showReader = csv.reader(csvfile)
	# obtaining the subject of each columns: first_name, last_name, company_name, etc.
	subject = showReader.next()
	# this empty list will be nesting row of information
	info = []
	for row in showReader:
		info += [row]
	# printing the csv data
	for count in range(0, len(info)):
		print info[count][0], info[count][1]
		for index in range(0, len(subject)):
			print subject[index]+": "+info[count][index]
		print "---------------------------------------------"
