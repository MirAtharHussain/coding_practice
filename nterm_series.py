# 2nd question:

# find the nth term of the series

# 3,8,6, 11, 9, 14, 12, 17, 15, 20,.....

# examples input and output:

#based on position entered by user return the term or number present in that position as output

#input: 6    input: 10     input: 30
#output: 14      output: 20    output: 50



# Answer :  observer every even position +5 is added to previous position number  and every odd position -2  is subtracted from previous number

#! usr/bin/python

def find_number_series(input_no):
	base_no = 3  #As per series first position number is 3
	previous = base_no #As initially previous value we will keep as 3 itself
	current = 0

	if(input_no == 1):
		print(base_no)

	#example if user enter 9 we have to find number of the 9th position so we need loop As we already have 1st position value we start from 2nd position

#1st way

	for i in range(2, input_no+1):
		if(i%2==0):
			base_no += 5
		else:
			base_no -= 2
	print(base_no)

#2nd way of doing it
#	for i in range(2, input_no+1):
#		if(i%2==0):
#			current = previous + 5
#			previous = current
#		else:
#			current = previous - 2
#			previous = current
#	print(current)
		
			
	
	
if __name__ =="__main__":
	user_input = int(input("Enter a number position to find its term"))
	find_number_series(user_input)
	
