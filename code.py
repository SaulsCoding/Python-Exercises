def file_reader():
	arr = []
	file = open("file   .txt", "r")     # File called data.txt must be in the same directory as the number_of_times.py
	
	# Read each line from the file   
	for line in file:
		list = line.split()
		
		# Read each word from a line
		for word in list:
			arr.append(word)         # Add each word to the array
	return arr;


def welcome_user():
	print('Welcome To Number Of Times')
	element = input("Enter Number or Word:")
	return element;


def number_of_times(element, arr):
	count = 0
	
	# Check items in arr that are equal to element
	for word in arr:
		if word == element:
			count = count + 1
	
	# Print results as a statement		
	print(element, 'appears ', count, 'times in the file')
	
	
arr = file_reader()
element = welcome_user()
number_of_times(element, arr)


