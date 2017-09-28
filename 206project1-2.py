import os
import filecmp
import csv
from collections import Counter
from datetime import datetime

def getData(file):	
	with open(file, 'r') as f:
		d_list= []
		reader = csv.DictReader(f)
		for row in reader:
			d_list.append(row)
		return d_list
	
#Input: file name
#Ouput: return a list of dictionary objects where 
#the keys will come from the first row in the data.

#Note: The column headings will not change from the 
#test cases below, but the the data itself will 
#change (contents and size) in the different test 
#cases.

	#Your code here:
	#pass

#Sort based on key/column
def mySort(data,col):
#Input: list of dictionaries
#Output: Return a string of the form firstName lastName
	sort_list = sorted(data, key = lambda x:x[col])
	first_name = sort_list[0].get('First')
	last_name = sort_list[0].get('Last')
	string = first_name + ' ' + last_name
	return string

#Create a histogram
def classSizes(data):
# Input: list of dictionaries
# Output: Return a list of tuples ordered by
# ClassName and Class size, e.g 
# [('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)]
	freshman_count = 0
	sophomore_count = 0
	junior_count = 0
	senior_count = 0

	for x in data:
		if x.get('Class') == 'Freshman':
			freshman_count += 1
		if x.get('Class') == 'Sophomore':
			sophomore_count += 1
		if x.get('Class') == 'Junior':
			junior_count += 1
		elif x.get('Class') == 'Senior':
			senior_count += 1

	class_count = [('Freshman',freshman_count),('Sophomore',sophomore_count),('Junior',junior_count),('Senior',senior_count)]
	sorted_list = sorted(class_count, key = lambda x:x[1], reverse=True)
	return(sorted_list)
	
	#Your code here:
	#pass



# Find the most common day of the year to be born
def findDay(a):
	day_count = []
	for days in a:
		d = days.get('DOB')
		day_count.append(d)
		#print(day_count)

	list_day = []
	for date in day_count:
		x = date.split('/')
		i = x[1]
		list_day.append(i)
	#print(list_day)

	sorted_days = sorted(list_day)
	#print(sorted_days)

	count = Counter(sorted_days)
	return int(count.most_common(1)[0][0])




# Input: list of dictionaries
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB
	
	
	#Your code here:
	#pass


# Find the average age (rounded) of the Students
def findAge(a):
	L = []
	new_list =[]
	today = datetime.today()
	for day in a:
		dates = day['DOB']
		L.append(dates)
	#print(L)
	for d in L:
		bd = datetime.strptime(d,"%m/%d/%Y")
		age_days = (today - bd)
		new_list.append(age_days.days / 365)

	average = sum(new_list)/len(new_list)
	return int(average)

	
# Output: Return the day of month (1-31) that is the
# most often seen in the DOB

	#Your code here:
	#pass

#Similar to mySort, but instead of returning single
#Student, all of the sorted data is saved to a csv file.
def mySortPrint(a,col,fileName):
	sort_list = sorted(a, key = lambda x:x[col])
	with open('newfile.csv', 'w') as out_file:
		fieldnames = a[0].keys()
		writer = csv.DictWriter(out_file, fieldnames=fieldnames)
		#writer = csv.writer(out_file)
		for line in sort_list:
			#writer = csv.DictWriter(out_file, fieldnames=fieldnames)
			#writer.writeheader()
			writer.writerow(({'First':line['First'],'Last':line['Last'],'Email':line['Email']}))


		#for row in sort_list

#Input: list of dictionaries, key to sort by and output file name
#Output: None

	#Your code here:
	#pass



################################################################
## DO NOT MODIFY ANY CODE BELOW THIS
################################################################

## We have provided simple test() function used in main() to print what each function returns vs. what it's supposed to return.
def test(got, expected, pts):
  score = 0;
  if got == expected:
    score = pts
    print(" OK ",end=" ")
  else:
    print (" XX ", end=" ")
  print("Got: ",got, "Expected: ",expected)
  return score


# Provided main() calls the above functions with interesting inputs, using test() to check if each result is correct or not.
def main():
	total = 0
	print("Read in Test data and store as a list of dictionaries")
	data = getData('P1DataA.csv')
	data2 = getData('P1DataB.csv')
	total += test(type(data),type([]),40)
	print()
	print("First student sorted by First name:")
	total += test(mySort(data,'First'),'Abbot Le',15)
	total += test(mySort(data2,'First'),'Adam Rocha',15)

	print("First student sorted by Last name:")
	total += test(mySort(data,'Last'),'Elijah Adams',15)
	total += test(mySort(data2,'Last'),'Elijah Adams',15)

	print("First student sorted by Email:")
	total += test(mySort(data,'Email'),'Hope Craft',15)
	total += test(mySort(data2,'Email'),'Orli Humphrey',15)

	print("\nEach grade ordered by size:")
	total += test(classSizes(data),[('Junior', 28), ('Senior', 27), ('Freshman', 23), ('Sophomore', 22)],10)
	total += test(classSizes(data2),[('Senior', 26), ('Junior', 25), ('Freshman', 21), ('Sophomore', 18)],10)

	print("\nThe most common day of the year to be born is:")
	total += test(findDay(data),13,10)
	total += test(findDay(data2),26,10)
	
	print("\nThe average age is:")
	total += test(findAge(data),39,10)
	total += test(findAge(data2),41,10)

	print("\nSuccessful sort and print to file:")
	mySortPrint(data,'Last','results.csv')
	if os.path.exists('results.csv'):
		total += test(filecmp.cmp('outfile.csv', 'results.csv'),True,10)


	print("Your final score is: ",total)
# Standard boilerplate to call the main() function that tests all your code.
if __name__ == '__main__':
    main()

